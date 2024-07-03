from django.shortcuts import render, redirect#type: ignore
from django.urls import reverse_lazy#type: ignore
from django.views import generic#type: ignore
from .forms import CustomUserCreationForm, JoinClassForm
from django.contrib.auth.decorators import login_required#type: ignore
from django.http import HttpResponse#type: ignore
from .models import Classes, ClassList, Account
from StudentSupport.logger import log_action
from StudentSupport.models import Log#type: ignore
from django.template import loader#type: ignore
from django.contrib import messages #type: ignore



#class SignUpView(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("login")
#    template_name = "registration/signup.html"

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        user.profile.IsTeacher = form.cleaned_data.get('IsTeacher')
        user.profile.Grade = form.cleaned_data.get('Grade')

        user.profile.save()
        return response

@login_required(redirect_field_name='registration/login/')
def JoinClass(request):

    class_code = request.GET.get('code', None)
    user = request.user
    user_instance = Account.objects.get(user=user)
    if class_code:

        # Check if a class with the given code exists
        try:

            class_instance = Classes.objects.get(ClassJoinCode=class_code)



            inclass = ClassList.objects.filter(UserID = user_instance, ClassID=class_instance).exists()
            if not inclass:
                NewClass = ClassList(UserID = user_instance, ClassID=class_instance, Teacher=False)
                NewClass.save()
                log_action(user_instance, 'JOIN_CLASS_REQUEST',
                           f'Joined Class id: {class_instance.id}')
                messages.error(request, f"Joined Class id: {class_instance.id}")
            else:
                log_action(user_instance, 'JOIN_CLASS_REQUEST',
                           f'Failed to join Class id: {class_instance.id}, Already in class')
                messages.error(request, "already in class.")
        except Classes.DoesNotExist:
            log_action(user_instance, 'JOIN_CLASS_REQUEST',
                       f'Failled to join Class ID: {class_code}, class does not exist')
            messages.error(request, "Class doesnt exist.")
    else:
        log_action(user_instance, 'JOIN_CLASS_REQUEST', f'Failled to join Class, no class code provided')

        messages.error(request, "No Class code.")

    return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))
@login_required(redirect_field_name='registration/login/')
def Home(request):
    user = request.user

    class_lists = ClassList.objects.filter(UserID__id=user.id)


    #return render(request, 'home.html', context)
    if request.method == 'POST':
        form = JoinClassForm(request.POST)
        if form.is_valid():
            class_code = form.cleaned_data['class_code']
            return redirect(f'/joinclass/?code={class_code}')
    else:
        form = JoinClassForm()
    context = {
        'class_list': class_lists,
        'form': form
    }
    return render(request, 'home.html', context=context)
