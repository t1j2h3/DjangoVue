from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_200_OK

from backend.models import HighAdmin,College
from backend.utils.time import TimeEncry
from backend.utils.encrypt import md5

# 校管理员序列化器
class HighAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = HighAdmin
        fields = '__all__'

# 校管理员登陆
class login(APIView):
    @csrf_exempt
    def post(self,request):
        d = request.data
        if ("account" in d.keys()) and ("password" in d.keys()):
            # d["password"] = md5(d["password"])
            x = HighAdmin.objects.filter(account=d["account"]).first()
            if x==None:
                ans={"status":False, "errors":"没有该用户"}
                return Response(ans)
            if x.password != d["password"]:
                ans = {"status": False, "errors": "密码不正确"}
                return Response(ans)
            token = TimeEncry()
            ans = {"status": True, "rank": 4, "token": token}
            return Response(data=ans, status=status.HTTP_200_OK)
        else:
            ans = {"status": False, "errors": "参数错误"}
            return Response(ans)

# 校管理员修改
class update(UpdateModelMixin,GenericAPIView):
    queryset = HighAdmin.objects.all()
    serializer_class = HighAdminSerializers
    @csrf_exempt
    def put(self, request, pk):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        return self.update(request)

# 学院序列化器
class CollegeSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="title", allow_null=True, allow_blank=True)
    class Meta:
        model = College
        exclude = ['title']

# 学院增删改查找
class college_listcreate(ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializers
class college_retrieveupdatedestroy(RetrieveUpdateDestroyAPIView):
    # 删除成功没有返回，除非改源码
    queryset = College.objects.all()
    serializer_class = CollegeSerializers

# 密码修改
class password_put(APIView):
    @csrf_exempt
    def put(self, request, pk):
        old = request.data.get("oldpassword")
        check = request.data.get("checkpassword")
        if not old or not check:
            return Response(status=HTTP_202_ACCEPTED, data={"entail": "参数错误"})
        # old = md5(old)
        # check = md5(check)
        password = HighAdmin.objects.filter(account=pk).first().password
        if password == old:
            if len(check)>100:
                return Response(status=HTTP_202_ACCEPTED,data={"entail":"新密码过长"})
            HighAdmin.objects.filter(account=pk).update(password=check)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_202_ACCEPTED, data={"entail":"旧密码错误"})




