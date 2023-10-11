from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin,ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_200_OK

from backend.models import LowAdmin,Branch
from backend.utils.time import TimeEncry
from backend.utils.encrypt import md5

# 支部管理员序列化器
class LowAdminSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="branch", allow_null=True, allow_blank=True)
    class Meta:
        model = LowAdmin
        fields = '__all__'

# 班级管理员登陆
class login(APIView):
    @csrf_exempt
    def post(self,request):
        d = request.data
        if ("account" in d.keys()) and ("password" in d.keys()):
            # d["password"] = md5(d["password"])
            x = LowAdmin.objects.filter(account=d["account"]).first()
            if x==None:
                ans={"status":False, "errors":"没有该用户"}
                return Response(ans)
            if x.password != d["password"]:
                print(33)
                ans = {"status": False, "errors": "密码不正确"}
                return Response(ans)
            token = TimeEncry()
            ans = {"status": True, "rank": 2, "token" : token, "from_branch": x.branch.id, "from_college": x.college.id}
            return Response(ans)
        else:
            print(88)
            ans = {"status": False, "errors": "参数错误"}
            return Response(ans)

# 支部管理员增删改查找
class lowadmin_listcreate(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = LowAdmin.objects.all()
    serializer_class = LowAdminSerializers
    def get(self, request):
        return self.list(request)
    @csrf_exempt
    def post(self,request):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        return self.create(request)
class lowdmin_retrieveupdatedestroy(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    # 删除成功没有返回，除非改源码
    queryset = LowAdmin.objects.all()
    serializer_class = LowAdminSerializers
    def get(self, request, pk):
        return self.retrieve(request)
    @csrf_exempt
    def put(self,request, pk):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        return self.update(request)
    @csrf_exempt
    def delete(self,request, pk):
        return self.destroy(request)

# 支部管理员根据学院查找, 没用框架的
class lowadmin_collegehh(APIView):
    def get(self,request,id):
        branch_list = Branch.objects.filter(college_id=id).all()
        branch_id = set()
        for x in branch_list:
            branch_id.add(x)
        ans = []
        for obj in branch_id:
            admin_list = LowAdmin.objects.filter(branch_id=obj).all()
            for x in admin_list:
                jsonx = {
                    "account": x.account,
                    "password": x.password,
                    "branch": x.branch.id,
                    "college": x.branch.college.id,
                    "branch_title": x.branch.title,
                    "college_title": x.branch.college.title,
                }
                ans.append(jsonx)
        return Response(ans)

# 支部管理员根据学院查找
class lowadmin_college(APIView):
    def get(self,request,id):
        admin_list = LowAdmin.objects.filter(college_id=id).all()
        serializer = LowAdminSerializers(instance=admin_list, many=True)
        return Response(serializer.data)

# 支部管理员根据支部查找
class lowadmin_branch(APIView):
    def get(self,request,id):
        admin_list = LowAdmin.objects.filter(branch_id=id).all()
        serializer = LowAdminSerializers(instance=admin_list, many=True)
        return Response(serializer.data)

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
        password = LowAdmin.objects.filter(account=pk).first().password
        if password == old:
            if len(check)>100:
                return Response(status=HTTP_202_ACCEPTED,data={"entail":"新密码过长"})
            LowAdmin.objects.filter(account=pk).update(password=check)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_202_ACCEPTED, data={"entail":"旧密码错误"})