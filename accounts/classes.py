

from django.http import HttpResponse#type: ignore
from django.contrib.auth.decorators import login_required, user_passes_test#type: ignore
from django.shortcuts import render, redirect#type: ignore
from StudentSupport.utils import is_on_group_check, getClassFromID, is_user_in_class#type: ignore
from .forms import CreateNewClass
from .models import Classes, Account
from .backendFunctions import id_generator

def getClassinfo(request, id):
    user = request.user

    if user.account.IsTeacher:


        return HttpResponse('teacher: ' + str(id))
    else:
        return HttpResponse('test: ' + str(id))


def getClass(request, id):
    if (is_user_in_class(id)):
        if request.method == 'POST':
            print('test')
        else:
            classinfo = getClassFromID(id)

            context = {
                'classinfo': classinfo,

            }

        return render(request, 'class.html', context = context)
    return HttpResponse('wrong class')

def Create_New_Class(request):
    user = request.user
    user_instance = Account.objects.get(user=user)
    if request.method == 'POST':
        form = CreateNewClass(request.POST)
        if form.is_valid():
            ClassName = form.cleaned_data['Classname']
            print(ClassName)
            ClassSubject = form.cleaned_data['Subject']
            print(ClassSubject)
            ClassCode = form.cleaned_data['Class Code']
            

            if not Classes.objects.filter(ClassName=ClassName, Subject=ClassSubject).exists():
                newClass = Classes(ClassName=ClassName, Subject=ClassSubject, ClassCode = ClassCode, ClassJoinCode=id_generator())
                newClass.save()
                newClass.Teachers.add(user_instance.user)
                
 
 
 
            return redirect('home')
    else:
        form = CreateNewClass()

    context = {
        'form': form   
    }
    return render(request, 'CreateClass.html',context=context)