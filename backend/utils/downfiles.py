import os

from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED

def pdf_download(file_path, file_name):
    if not file_path:
        return HttpResponse(status=202, content="没有上传文件")
    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/pdf"
        response['Content-Disposition'] = "attachment; filename=" + file_name
        return response
    except Exception:
        return HttpResponse(status=202, content="后端：文件错误")

def streaming_download(file_path, file_name):
    if not file_path:
        return HttpResponse(status=202, content="没有上传文件")
    try:
        response = StreamingHttpResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = "attachment; filename=" + file_name
        return response
    except Exception:
        return HttpResponse(status=202, content="后端：文件错误")

def updatex(self, request, basef, pathf, wayf, *args, **kwargs):
    """
    :param basef: 文件在数据库的列名
    :param pathf: 文件路径字符串
    :param wayf: 保存文件在后端方法
    """
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    # 判断是否有account
    account = request.data.get["account"]
    if not account:
        return Response(status=HTTP_202_ACCEPTED, data={"entail": "没有account参数"})
    # 路径保存在数据库中
    request.data[basef] = os.path.join("Files", f"user_{account}", wayf)
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    # 保存文件在后端
    wayf()

    if getattr(instance, '_prefetched_objects_cache', None):
        # If 'prefetch_related' has been applied to a queryset, we need to
        # forcibly invalidate the prefetch cache on the instance.
        instance._prefetched_objects_cache = {}

    return Response(serializer.data)