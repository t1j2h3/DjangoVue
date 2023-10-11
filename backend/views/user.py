import os
import shutil

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import GenericAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.mixins import UpdateModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_200_OK,HTTP_204_NO_CONTENT

from backend.models import User,Registration
from backend.utils.time import TimeEncry
from backend.utils.encrypt import md5

# 用户序列化器
class UserSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="branch", allow_null=True, allow_blank=True)
    class Meta:
        model = User
        fields = "__all__"

# 用户登陆
class login(APIView):
    @csrf_exempt
    def post(self,request):
        d = request.data
        # print(d)
        if ("account" in d.keys()) and ("password" in d.keys()):
            # d["password"] = md5(d["password"])
            x = User.objects.filter(account=d["account"]).first()
            if x==None:
                register = Registration.objects.filter(account=d["account"]).first()
                if register and register.state==1:
                    ans = {"status": False, "errors": "你已经提交注册申请，管理员在审核中"}
                else:
                    ans={"status":False, "errors":"没有该用户，或您的注册没通过"}
                return Response(ans)
            if x.password != d["password"]:
                ans = {"status": False, "errors": "密码不正确"}
                return Response(ans)
            token = TimeEncry()
            state = x.status   # state = x.get_status_display()
            from_branch, from_college = x.branch_id, x.college_id
            ans = {"status": True, "rank": 1, "state": state, "token": token, "from_branch": from_branch,
                   "from_college": from_college}
            return Response(ans)
        else:
            ans = {"status": False, "errors": "参数错误"}
            return Response(ans)

# 用户增删改查找
class user_create(APIView):
    @csrf_exempt
    def post(self, request):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        request.data['college_title'], request.data['branch_title'] = 0, 0     # 防止title影响
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            path = os.path.join("Files", f"{request.data['account']}")
            if os.path.exists(path) == False:
                os.mkdir(path)
            serializer.save()
            return Response(serializer.data)
        return Response(data=serializer.errors, status=HTTP_202_ACCEPTED)
class user_retrieveupdate(RetrieveModelMixin,UpdateModelMixin,GenericAPIView):
    # 删除成功没有返回，除非改源码
    queryset = User.objects.all()
    serializer_class = UserSerializers
    def get(self, request, pk):
        return self.retrieve(request)
    @csrf_exempt
    def put(self,request, pk):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        return self.update(request)
class user_destroy(APIView):
        @csrf_exempt
        def delete(self, request, pk):
            obj = User.objects.filter(pk=pk).first()
            if obj:
                obj.delete()
                path = os.path.join("Files", f"{pk}")
                if os.path.exists(path) == True:
                    shutil.rmtree(path)
                return Response(status=HTTP_204_NO_CONTENT)
            else:
                return Response(status=HTTP_202_ACCEPTED,data={"entail": "没有该用户"})

# 用户序列化器，按顺序get列
class UserSerializerGet(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="branch", allow_null=True, allow_blank=True)
    class Meta:
        model = User
        fields = ["account", "name", "college_title", "branch_title", "First_application", "semester", "talking_date",
                  "talker", "apply_letter", "courses_for_activists", "activists_remarks", "activists_grade",
                  "activists_appraising", "activists_appraising", "activists_date", "contacts1", "contacts2",
                  "investigation_registration", "courses_for_developer", "developer_remarks", "developer_grade",
                  "developer_appraising", "developer_graduation", "developer_date", "introducer1", "introducer2",
                  "number", "mass_discussion", "probation_date", "voluntary_letter", "probation_date", "formal_date"]

# 用户根据身份status查找
class user_s(APIView):
    def get(self,request,status):
        user_list = User.objects.filter(status=status).all()
        serializer = UserSerializerGet(instance=user_list, many=True)
        return Response(serializer.data)

# 用户根据学院查找
class user_college(APIView):
    def get(self,request,id):
        user_list = User.objects.filter(college_id=id).all()
        serializer = UserSerializers(instance=user_list, many=True)
        return Response(serializer.data)

# 用户根据学院查找身份status
class user_college_s(APIView):
    def get(self,request,status,id):
        user_list = User.objects.filter(college_id=id,status=status).all()
        serializer = UserSerializerGet(instance=user_list, many=True)
        return Response(serializer.data)

# 用户根据支部查找
class user_branch(APIView):
    def get(self,request,id):
        user_list = User.objects.filter(branch_id=id).all()
        serializer = UserSerializers(instance=user_list, many=True)
        return Response(serializer.data)

# 用户根据支部查找身份status
class user_branch_s(APIView):
    def get(self,request,status,id):
        user_list = User.objects.filter(branch_id=id,status=status).all()
        serializer = UserSerializerGet(instance=user_list, many=True)
        return Response(serializer.data)

# 个人信息get序列器
class UserSerializers1get(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="branch", allow_null=True, allow_blank=True)
    class Meta:
        model = User
        fields = ["account", "name", "gender", "nation", "phone", "classx", "identity_card", "native", "college_title",
                  "branch_title", "job", "email", "address", "headmaster"]

# 个人信息get
class user_get1(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers1get

# 个人信息put序列器
class UserSerializers1put(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["account", "name", "gender", "nation", "phone", "classx", "identity_card", "native", "job", "email",
                  "address", "headmaster"]

# 个人信息put
class user_put1(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers1put

# 入党申请人get序列器
class UserSerializers2get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["First_application", "semester", "talking_date", "talker", "apply_letter"]

# 入党申请人get
class user_get2(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers2get

# 入党申请人put序列器
class UserSerializers2put(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["talker", "apply_letter", "talking_date"]

# 入党申请人put
class user_put2(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers2put
    @csrf_exempt
    def put(self,request,pk):
        file_path = None
        # 合理就保存文件
        if request.FILES:
            file_obj = request.FILES.get("apply_letter")
            if file_obj:
                file_path = os.path.join("Files", f"{pk}", "入党申请书.pdf")
                f = open(file_path, mode='wb')
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
                request.data["apply_letter"] = file_path
        # 判断是否符合序列化器要求
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 没有更新，删除文件
        if file_path and os.path.exists(file_path) == True:
            os.remove(file_path)
        return Response(serializer.errors)

# 入党积极分子get序列器
class UserSerializers3get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["courses_for_activists", "activists_date", "activists_graduation", "activists_grade",
                  "activists_remarks", "activists_appraising", "contacts1", "contacts2", "investigation_registration"]

# 入党积极分子get
class user_get3(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers3get

# 入党积极分子put序列器
class UserSerializers3put(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["contacts1", "contacts2", "investigation_registration"]

# 入党积极分子put
class user_put3(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers3put
    @csrf_exempt
    def put(self,request,pk):
        file_path = None
        # 合理就保存文件
        if request.FILES:
            file_obj = request.FILES.get("investigation_registration")
            if file_obj:
                file_path = os.path.join("Files", f"{pk}", "积极分子考察登记表.pdf")
                f = open(file_path, mode='wb')
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
                request.data["investigation_registration"] = file_path
        # 判断是否符合序列化器要求
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 没有更新，删除文件
        if file_path and os.path.exists(file_path) == True:
            os.remove(file_path)
        return Response(serializer.errors)

# 发展对象get序列器
class UserSerializers4get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["courses_for_developer","developer_date","developer_graduation","developer_grade",
                  "developer_remarks","developer_appraising", "introducer1", "introducer2"]

# 发展对象get
class user_get4(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers4get

# 发展对象put序列器
class UserSerializers4put(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["introducer1", "introducer2"]

# 发展对象put
class user_put4(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers4put

# 预备党员get序列器
class UserSerializers5get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["number","mass_discussion","probation_date","probation_remarks","voluntary_letter"]

# 预备党员get
class user_get5(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers5get

# 预备党员put序列器
class UserSerializers5put(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["number","mass_discussion","voluntary_letter"]

# 预备党员put
class user_put5(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers5put
    @csrf_exempt
    def put(self, request, pk):
        file_path = None
        # 合理就保存文件
        if request.FILES:
            file_obj = request.FILES.get("voluntary_letter")
            if file_obj:
                file_path = os.path.join("Files", f"{pk}", "入党志愿书.pdf")
                f = open(file_path, mode='wb')
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
                request.data["voluntary_letter"] = file_path
        # 判断是否符合序列化器要求
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 没有更新，删除文件
        if file_path and os.path.exists(file_path) == True:
            os.remove(file_path)
        return Response(serializer.errors)

# 党员get序列器
class UserSerializers6get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["probation_date","formal_date"]

# 党员get
class user_get6(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers6get

# 密码修改
class password_put(APIView):
    @csrf_exempt
    def put(self, request, pk):
        old = request.data.get("oldpassword")
        check = request.data.get("checkpassword")
        if not old or not check:
            return Response(status=HTTP_202_ACCEPTED, data={"entail": "参数错误"})
        old = md5(old)
        check = md5(check)
        password = User.objects.filter(account=pk).first().password
        if password == old:
            if len(check)>100:
                return Response(status=HTTP_202_ACCEPTED,data={"entail":"新密码过长"})
            User.objects.filter(account=pk).update(password=check)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_202_ACCEPTED, data={"entail":"旧密码错误"})
# 密码重置
class password_reset(APIView):
    @csrf_exempt
    def post(self, request, pk):
        obj = User.objects.filter(account=pk).first()
        if obj==None:
            return Response(status=HTTP_202_ACCEPTED, data={"entail":"没有该账号"})
        if len(obj.identity_card) > 6:
            User.objects.filter(account=pk).update(password=md5(obj.identity_card[-6:]))
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_202_ACCEPTED, data={"entail":"身份证有问题，或者其他错误"})

# 用户批量修改序列化器
class UserSerializerManyPut(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["identity_card", "gender", "nation", "native", "password", "college", "branch"]
class manyput(APIView):
    @csrf_exempt
    def put(self, requset):
        cnt = 0
        allres = {}
        for data in requset.data:
            account = data.get("account")
            if not account:
                continue
            obj = User.objects.filter(account=account).first()
            if obj:
                serializer = UserSerializerManyPut(data=data, instance=obj)
                if serializer.is_valid():
                    serializer.save()
                    cnt += 1
                else:
                    derror = []
                    # print(serializer.errors[0])
                    for k,v in serializer.errors.items():
                        for t in v:
                            derror.append(str(k)+"："+str(t))
                    allres[f"{account}\'s errors"] = derror  # 批量修改中的错误
            else:
                allres[f"{account}\'s errors"] = ["没有该账号"]
        allres["entail"] = f"成功更新{cnt}条数据"
        return Response(data=allres)





