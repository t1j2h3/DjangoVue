from django.db import models
import hashlib
""" 注意: 如果未设置主键, 则默认生成 id = models.BigAutoField(primary_key=True) """

# 校管理员
class HighAdmin(models.Model):
    account = models.CharField(verbose_name='账号', max_length=100, unique=True, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, blank=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=100)

    def save(self, *args, **kwargs):
        # 对密码进行加密
        self.password = self.encrypt_password(self.password)
        super().save(*args, **kwargs)

    @staticmethod
    def encrypt_password(password):
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        encrypted_password = md5.hexdigest()
        return encrypted_password

# 学院
class College(models.Model):
    title = models.CharField(verbose_name='学院名字', max_length=40, unique=True)
    remarks = models.CharField(verbose_name="学院备注", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.title

# 院管理员
class MediuAdmin(models.Model):
    account = models.CharField(verbose_name='账号', max_length=100, unique=True, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, blank=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=100)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)

# 班级
class Branch(models.Model):
    title = models.CharField(verbose_name='班级名字', max_length=40)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)
    remarks = models.CharField(verbose_name="班级备注", max_length=100, null=True, blank=True)
    def __str__(self):
        return self.title

# 班级管理员
class LowAdmin(models.Model):
    account = models.CharField(verbose_name='账号', max_length=100, unique=True, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, blank=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=100)
    branch = models.ForeignKey(verbose_name='所属班级', to="Branch", to_field="id", on_delete=models.CASCADE)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)

# 用户
class User(models.Model):
    account = models.CharField(verbose_name='学号/职工号', max_length=18, unique=True , primary_key=True)
    identity_card = models.CharField(verbose_name='身份证', max_length=18, unique=True)
    status_choices = (
        (1, "大一"),
        (2, "大二"),
        (3, "大三"),
        (4, "大四"),
    )
    status = models.SmallIntegerField(verbose_name="所处年级", choices=status_choices, default=1)
    name = models.CharField(verbose_name="姓名", max_length=50)
    gender = models.CharField(verbose_name="性别", max_length=4)
    nation = models.CharField(verbose_name="民族", max_length=20)
    native = models.CharField(verbose_name="籍贯", max_length=50)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)
    branch = models.ForeignKey(verbose_name='所属班级', to="Branch", to_field="id", on_delete=models.CASCADE)
    password = models.CharField(verbose_name='密码', max_length=100)
    classx = models.CharField(verbose_name="年级班级", max_length=50, null=True, blank=True)
    job = models.CharField(verbose_name="学生工作职位", max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name="电话", max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name="邮箱", max_length=50, null=True, blank=True)
    address = models.CharField(verbose_name="住址", max_length=100, null=True, blank=True)
    headmaster = models.CharField(verbose_name="班主任", max_length=50, null=True, blank=True)



# 用户注册申请
class Registration(models.Model):
    account = models.CharField(verbose_name='学号/职工号', max_length=18)
    identity_card = models.CharField(verbose_name='身份证', max_length=18)
    status_choices = (
        (1, "大一"),
        (2, "大二"),
        (3, "大三"),
        (4, "大四"),
    )
    status = models.SmallIntegerField(verbose_name="身份", choices=status_choices, default=1)
    name = models.CharField(verbose_name="姓名", max_length=50)
    gender = models.CharField(verbose_name="性别", max_length=4)
    nation = models.CharField(verbose_name="民族", max_length=20, default="中国")
    native = models.CharField(verbose_name="籍贯", max_length=50)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)
    branch = models.ForeignKey(verbose_name='所属班级', to="Branch", to_field="id", on_delete=models.CASCADE)
    password = models.CharField(verbose_name='密码', max_length=100)
    state_choices = (
        (1, "申请中"),
        (2, "通过"),
        (3, "失败"),
    )
    state = models.SmallIntegerField(verbose_name="申请状态", choices=state_choices, default=1)

# 公示文件
class FilesB(models.Model):
    title = models.CharField(verbose_name='文件名字/标题', max_length=75)
    path = models.CharField(verbose_name="文件存储路径", max_length=100)
    college = models.ForeignKey(verbose_name='所属学院', to="College", to_field="id", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="时间")