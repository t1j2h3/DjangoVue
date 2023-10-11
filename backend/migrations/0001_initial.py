# Generated by Django 4.2.3 on 2023-07-17 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40, verbose_name="班级名字")),
                (
                    "remarks",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="班级备注"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="College",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=40, unique=True, verbose_name="学院名字"),
                ),
                (
                    "remarks",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="学院备注"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HighAdmin",
            fields=[
                (
                    "account",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="账号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="姓名"
                    ),
                ),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "account",
                    models.CharField(
                        max_length=18,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="学号/职工号",
                    ),
                ),
                (
                    "identity_card",
                    models.CharField(max_length=18, unique=True, verbose_name="身份证"),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "大一"), (2, "大二"), (3, "大三"), (4, "大四")],
                        default=1,
                        verbose_name="所处年级",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="姓名")),
                ("gender", models.CharField(max_length=4, verbose_name="性别")),
                ("nation", models.CharField(max_length=20, verbose_name="民族")),
                ("native", models.CharField(max_length=50, verbose_name="籍贯")),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                (
                    "classx",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="年级班级"
                    ),
                ),
                (
                    "job",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="学生工作职位"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="电话"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="邮箱"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="住址"
                    ),
                ),
                (
                    "headmaster",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="班主任"
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.branch",
                        verbose_name="所属班级",
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.college",
                        verbose_name="所属学院",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account", models.CharField(max_length=18, verbose_name="学号/职工号")),
                ("identity_card", models.CharField(max_length=18, verbose_name="身份证")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "大一"), (2, "大二"), (3, "大三"), (4, "大四")],
                        default=1,
                        verbose_name="身份",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="姓名")),
                ("gender", models.CharField(max_length=4, verbose_name="性别")),
                (
                    "nation",
                    models.CharField(default="中国", max_length=20, verbose_name="民族"),
                ),
                ("native", models.CharField(max_length=50, verbose_name="籍贯")),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                (
                    "state",
                    models.SmallIntegerField(
                        choices=[(1, "申请中"), (2, "通过"), (3, "失败")],
                        default=1,
                        verbose_name="申请状态",
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.branch",
                        verbose_name="所属班级",
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.college",
                        verbose_name="所属学院",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MediuAdmin",
            fields=[
                (
                    "account",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="账号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="姓名"
                    ),
                ),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.college",
                        verbose_name="所属学院",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LowAdmin",
            fields=[
                (
                    "account",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="账号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="姓名"
                    ),
                ),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.branch",
                        verbose_name="所属班级",
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.college",
                        verbose_name="所属学院",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="college",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="backend.college",
                verbose_name="所属学院",
            ),
        ),
    ]
