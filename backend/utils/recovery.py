from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from app01.models import College, Branch, HighAdmin, MediuAdmin, LowAdmin, User

# 恢复数据
class recovery_college(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                College.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})
class recovery_branch(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                Branch.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})
class recovery_highadmin(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                HighAdmin.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})
class recovery_mediuadmin(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                MediuAdmin.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})
class recovery_lowadmin(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                LowAdmin.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})
class recovery_user(APIView):
    @csrf_exempt
    def post(self, request):
        d = request.data
        try:
            for obj in d:
                User.objects.create(**obj)
            return Response(data={"ok": "true"})
        except Exception:
            return Response(status=202, data={"error": "failed"})