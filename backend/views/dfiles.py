import os

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from django.views.decorators.csrf import csrf_exempt

from backend.models import User, FilesB, College
from backend.utils.downfiles import pdf_download, streaming_download

class apply_letter(APIView):
    def get(self, request, pk):
        obj = User.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse(status=404)
        file_path = obj.apply_letter
        return pdf_download(file_path=file_path, file_name="入党申请书.pdf")

class investigation_registration(APIView):
    def get(self, request, pk):
        obj = User.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse(status=404)
        file_path = obj.investigation_registration
        return pdf_download(file_path=file_path, file_name="积极分子考察登记表.pdf")

class voluntary_letter(APIView):
    def get(self, request, pk):
        obj = User.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse(status=404)
        file_path = obj.voluntary_letter
        return pdf_download(file_path=file_path, file_name="入党志愿书.pdf")

class FileBSerializers(serializers.ModelSerializer):
    college_title = serializers.CharField(source="college", allow_null=True, allow_blank=True)
    class Meta:
        model = FilesB
        fields = "__all__"   # 不是all那么college_title则有问题

class publicity_upload(GenericAPIView):
    queryset = FilesB.objects.all().order_by("-date", "-id")
    serializer_class = FileBSerializers
    @csrf_exempt
    def post(self, request):
        request.data['college_title'] = 0
        title = request.data.get("title")
        if not title:
            return Response(data={"entail": "没有title参数"}, status=HTTP_202_ACCEPTED)
        college = request.data.get("college")
        if not college:
            return Response(data={"entail": "没有college参数"}, status=HTTP_202_ACCEPTED)
        if not College.objects.filter(pk=college).first():
            return Response(data={"entail": "没有该学院"}, status=HTTP_202_ACCEPTED)
        # 合理就保存文件
        if request.FILES:
            file_obj = request.FILES.get("file_obj")
            if file_obj:
                file_path = os.path.join("Files", "publicity", str(college)+title)
                request.data["path"] = file_path
                serializer = self.get_serializer(data=request.data)
                if serializer.is_valid():
                    FilesB.objects.filter(path=file_path).delete()
                    serializer.save()
                    f = open(file_path, mode='wb')
                    for chunk in file_obj.chunks():
                        f.write(chunk)
                    f.close()
                    return Response(serializer.data)
                return Response(serializer.errors, status=HTTP_202_ACCEPTED)
            return Response(data={"entail": "文件参数不对，要参数名为file_obj"}, status=HTTP_202_ACCEPTED)
        return Response(data={"entail": "文件未上传"}, status=HTTP_202_ACCEPTED)
    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

class publicity_download(APIView):
    def get(self, request, pk):
        obj = FilesB.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse(status=404)
        file_path = obj.path
        return streaming_download(file_path=file_path, file_name=obj.title)
    @csrf_exempt
    def delete(self, request, pk):
        obj = FilesB.objects.filter(pk=pk).first()
        if obj:
            path = obj.path
            if os.path.exists(path) == True:
                os.remove(path)
            FilesB.objects.filter(pk=pk).delete()
            return Response({"entail": "删除成功"})
        return HttpResponse(status=404, content="没有该pk")

class publicity_college(APIView):
    def get(self, request, id):
        file_list = FilesB.objects.filter(college_id=id).order_by("-date", "-id")
        serializer = FileBSerializers(instance=file_list, many=True)
        return Response(serializer.data)
