import os

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.generics import ListAPIView,GenericAPIView,RetrieveDestroyAPIView
from rest_framework.mixins import UpdateModelMixin,CreateModelMixin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from backend.models import Registration, User
from backend.views.user import UserSerializers
from backend.utils.encrypt import md5

# 注册序列化器
class RegistrationSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    branch_title = serializers.CharField(source="branch", allow_null=True, allow_blank=True)
    class Meta:
        model = Registration
        fields = '__all__'

# 注册序列化器2
class RegistrationSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

# 注册增删改查找
class list(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers
class retrievedestroy(RetrieveDestroyAPIView):
    # 删除成功没有返回，除非改源码
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer2

class create(CreateModelMixin,GenericAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers

    @csrf_exempt
    def post(self, request):
        if request.data.get("password"):
            request.data["password"] = md5(request.data["password"])
        request.data["college_title"] = "学院"
        request.data["branch_title"] = "班级"
        if User.objects.filter(account=request.data["account"]).first():
            return Response({"entail": "已存在该学号!"})
        if User.objects.filter(identity_card=request.data["identity_card"]).first():
            return Response({"entail": "已存在该身份证!"})
        obj = Registration.objects.filter(account=request.data["account"]).first()
        if obj and obj.state == 1:
            return Response({"entail": "你已经提交注册申请，管理员在审核，注意如果管理员没同意，你需要再次申请注册，申请没通过不会返回此消息"})
        return self.create(request)


class update(UpdateModelMixin,GenericAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers

    @csrf_exempt
    def put(self, request, pk):
        obj = Registration.objects.filter(pk=pk).first()
        request.data["college_title"] = "学院"
        request.data["branch_title"] = "班级"
        if obj==None:
            return self.update(request)
        if "state" not in request.data.keys():
            return self.update(request)
        if request.data["state"] == 3:
            Registration.objects.filter(pk=pk).first().delete()
            return Response({"enatil": "已不同意该注册申请"})
        if request.data["state"] == 2:
            serializer1 = RegistrationSerializers(data=request.data)
            if serializer1.is_valid():
                Registration.objects.filter(pk=pk).first().delete()
            else:
                return Response(serializer1.errors)
            serializer2 = UserSerializers(data=request.data)
            if serializer2.is_valid():
                path = os.path.join("Files", f"{obj.account}")
                if os.path.exists(path) == False:
                    os.mkdir(path)
                serializer2.save()
                return Response(serializer2.data)
            return Response(serializer2.errors)
        # 没有返回错误原因，除非改源码
        return self.update(request)

# 管理员根据学院收到注册申请
class college(APIView):
    def get(self,request,id):
        m_list = Registration.objects.filter(college=id, state=1).all()
        serializer = RegistrationSerializers(instance=m_list, many=True)
        return Response(serializer.data)

# 管理员根据支部收到注册申请
class branch(APIView):
    def get(self,request,id):
        m_list = Registration.objects.filter(branch=id, state=1).all()
        serializer = RegistrationSerializers(instance=m_list, many=True)
        return Response(serializer.data)