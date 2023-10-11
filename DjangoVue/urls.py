"""
URL configuration for DjangoVue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from backend.views import highadmin, mediuadmin, registration, user, lowadmin, dfiles

urlpatterns = [
    path("admin/", admin.site.urls),
    #相关接口

    # HighAdmin 学校
    path('highadmin/login/', highadmin.login.as_view()),
    re_path('highadmin/update/(?P<pk>.+)', highadmin.update.as_view()),
    re_path('highadmin/password/(?P<pk>.+)',highadmin.password_put.as_view()),# 密码

    # college  学院
    path('college/all/',highadmin.college_listcreate.as_view()),
    re_path('college/all/(?P<pk>\d+)',highadmin.college_retrieveupdatedestroy.as_view()),


    # class  班级
    path('branch/all/', mediuadmin.branch_listcreate.as_view()),
    re_path('branch/all/(?P<pk>\d+)', mediuadmin.branch_retrieveupdatedestroy.as_view()),
    re_path('branch/find/(?P<id>\d+)', mediuadmin.branch_find.as_view()),

    # registration  注册
    path('registration/all/',registration.list.as_view()),
    re_path('registration/all/(?P<pk>\d+)',registration.retrievedestroy.as_view()),
    re_path('registration/update/(?P<pk>\d+)', registration.update.as_view()),
    path('registration/create/', registration.create.as_view()),
    re_path('registration/college/(?P<id>\d+)', registration.college.as_view()),
    re_path('registration/branch/(?P<id>\d+)', registration.branch.as_view()),

    # user
    path('user/login/', user.login.as_view()),
    path('user/create/', user.user_create.as_view()),
    re_path('user/list/(?P<status>[1-5])', user.user_s.as_view()),
    re_path('user/all/(?P<pk>\d+)', user.user_retrieveupdate.as_view()),
    path('user/manyput/', user.manyput.as_view()),  # 批量改
    re_path('user/delete/(?P<pk>\d+)', user.user_destroy.as_view()),
    re_path('user/college_all/(?P<id>\d+)', user.user_college.as_view()),
    re_path('user/college/(?P<status>[1-5])/(?P<id>\d+)', user.user_college_s.as_view()),
    re_path('user/branch_all/(?P<id>\d+)', user.user_branch.as_view()),
    re_path('user/branch/(?P<status>[1-5])/(?P<id>\d+)', user.user_branch_s.as_view()),
    re_path('user/get1/(?P<pk>\d+)', user.user_get1.as_view()),  # 个人信息
    re_path('user/put1/(?P<pk>\d+)', user.user_put1.as_view()),
    re_path('user/get2/(?P<pk>\d+)', user.user_get2.as_view()),  # 入党申请人
    re_path('user/put2/(?P<pk>\d+)', user.user_put2.as_view()),
    re_path('user/get3/(?P<pk>\d+)', user.user_get3.as_view()),  # 入党积极分子
    re_path('user/put3/(?P<pk>\d+)', user.user_put3.as_view()),
    re_path('user/get4/(?P<pk>\d+)', user.user_get4.as_view()),  # 发展对象
    re_path('user/put4/(?P<pk>\d+)', user.user_put4.as_view()),
    re_path('user/get5/(?P<pk>\d+)', user.user_get5.as_view()),  # 预备党员
    re_path('user/put5/(?P<pk>\d+)', user.user_put5.as_view()),
    re_path('user/get6/(?P<pk>\d+)', user.user_get6.as_view()),  # 党员
    re_path('user/password/(?P<pk>\d+)', user.password_put.as_view()),  # 密码修改
    re_path('user/pwdreset/(?P<pk>\d+)', user.password_reset.as_view()),  # 密码重置

     # lowadmin
    path('lowadmin/login/', lowadmin.login.as_view()),
    path('lowadmin/all/',lowadmin.lowadmin_listcreate.as_view()),
    re_path('lowadmin/all/(?P<pk>.+)',lowadmin.lowdmin_retrieveupdatedestroy.as_view()),
    re_path('lowadmin/college/(?P<id>\d+)',lowadmin.lowadmin_college.as_view()),
    re_path('lowadmin/collegehh/(?P<id>\d+)',lowadmin.lowadmin_collegehh.as_view()), # 没用框架的
    re_path('lowadmin/branch/(?P<id>\d+)',lowadmin.lowadmin_branch.as_view()),
    re_path('lowadmin/password/(?P<pk>.+)',lowadmin.password_put.as_view()),# 密码

    # mediuadmin
    path('mediuadmin/login/', mediuadmin.login.as_view()),
    path('mediuadmin/all/',mediuadmin.mediuadmin_listcreate.as_view()),
    re_path('mediuadmin/all/(?P<pk>.+)',mediuadmin.mediuadmin_retrieveupdatedestroy.as_view()),
    re_path('mediuadmin/password/(?P<pk>.+)',mediuadmin.password_put.as_view()),# 密码

    # 其他文件操作
    re_path('files/apply_letter/(?P<pk>\d+)',dfiles.apply_letter.as_view()),
    re_path('files/investigation_registration/(?P<pk>\d+)',dfiles.investigation_registration.as_view()),
    re_path('files/voluntary_letter/(?P<pk>\d+)',dfiles.voluntary_letter.as_view()),
    path('files/publicity/',dfiles.publicity_upload.as_view()),
    re_path('files/publicity/(?P<pk>\d+)',dfiles.publicity_download.as_view()),
    re_path('files/publicity_college/(?P<id>\d+)',dfiles.publicity_college.as_view()),

    path(r'', TemplateView.as_view(template_name="index.html")),
]
