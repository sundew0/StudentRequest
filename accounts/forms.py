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
