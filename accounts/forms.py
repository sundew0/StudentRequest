from django import forms#type: ignore
from django.contrib.auth.forms import UserCreationForm#type: ignore
from django.contrib.auth import get_user_model#type: ignore

class CustomUserCreationForm(UserCreationForm):
    IsTeacher = forms.BooleanField()

    Grade = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('IsTeacher', 'Grade')


class JoinClassForm(forms.Form):
    class_code = forms.CharField(label='Class Code', max_length=20)

class CreateNewClass(forms.Form):
    Classname = forms.CharField(label='Class Name', max_length=100)
    Subject = forms.CharField(label='Class Subject', max_length=50)


#    ClassName = models.CharField(max_length=100, null=True)
#    Subject = models.CharField(max_length=50, null=True)
#    id = models.AutoField(primary_key=True)
#    ClassCode = models.CharField(max_length=6, null=True, verbose_name="Class Code")
#    ClassJoinCode = models.CharField(max_length=6, null=True, unique=True, verbose_name="join Code")
