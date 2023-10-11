from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import UpdateModelMixin,ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_200_OK

from backend.models import MediuAdmin,Branch
from backend.utils.time import TimeEncry
from backend.utils.encrypt import md5

# 院管理员序列化器
class MediuAdminSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    class Meta:
        model = MediuAdmin
        fields = '__all__'

# 院管理员登陆
class login(APIView):
    @csrf_exempt
    def post(self,request):
        d = request.data
        if ("account" in d.keys()) and ("password" in d.keys()):
            # d["password"] = md5(d["password"])
            x = MediuAdmin.objects.filter(account=d["account"]).first()
            if x==None:
                ans={"status":False, "errors":"没有该用户"}
                return Response(ans)
            if x.password != d["password"]:
                ans = {"status": False, "errors": "密码不正确"}
                return Response(ans)
            token = TimeEncry()
            ans = {"status": True, "rank": 3, "token":token, "from_college": x.college.id}
            return Response(ans)
        else:
            ans = {"status": False, "errors": "参数错误"}
            return Response(ans)

# 院管理员增删改查找
class mediuadmin_listcreate(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = MediuAdmin.objects.all()
    serializer_class = MediuAdminSerializers
    def get(self, request):
        return self.list(request)
    @csrf_exempt
    def post(self,request):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        return self.create(request)
class mediuadmin_retrieveupdatedestroy(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    # 删除成功没有返回，除非改源码
    queryset = MediuAdmin.objects.all()
    serializer_class = MediuAdminSerializers
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

# 支部序列化器
class BranchSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="title", allow_null=True, allow_blank=True)
    class Meta:
        model = Branch
        exclude = ['title']

# 支部增删改查找
class branch_listcreate(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers
class branch_retrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    # 删除成功没有返回，除非改源码
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers

# 支部根据学院查找
class branch_find(APIView):
    def get(self,request,id):
        # 构建序列化对象器
        branch_list = Branch.objects.filter(college_id=id).all()
        serializer = BranchSerializers(instance=branch_list,many=True)
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
        password = MediuAdmin.objects.filter(account=pk).first().password
        if password == old:
            if len(check)>100:
                return Response(status=HTTP_202_ACCEPTED,data={"entail":"新密码过长"})
            MediuAdmin.objects.filter(account=pk).update(password=check)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_202_ACCEPTED, data={"entail":"旧密码错误"})