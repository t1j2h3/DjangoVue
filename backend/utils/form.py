from django import forms
from app01 import models
from rest_framework import serializers

class registerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["account", "name", "gender", "nation", "identity_card", "password", "native", "branch", "college"]

class registerModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["account", "name", "gender", "nation", "identity_card", "password", "native", "branch", "college"]

class baseModelForm(forms.ModelForm):
    class meta:
        model = models.User
        fields = ["name", "gender", "nation", "identity_card", "phone", "email", "native", "classx", "headmaster",
                  "job", "address"]

class applicationModelForm(forms.ModelForm):
    class meta:
        model = models.User
        fields = ["First_application", "semester", "talking_date", "talker"]

# form = baseModelForm(data=request.POST,instance=row_object)
# if form.is_valid():
#     form.save()
#     path = os.path.join("Files", f"{ac}")
#     if os.path.exists(path) == False:
#         os.mkdir(path)
# else:
#     for k, v in form.errors.items():
#         for t in v:
#             datae.add(f"学号{ac}的{str(k)}：" + str(t))