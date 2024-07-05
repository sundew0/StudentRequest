from django.shortcuts import render, redirect # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views import generic # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib import messages # type: ignore

from accounts.models import ClassList, Classes, Account
from .models import StudentHelp
from .logger import log_action

@login_required(redirect_field_name='registration/login/')
def addToLog(request):
    reasonList = {
        'C91G9': 'TOILET',
        '3CJ77': 'HAND_UP',
        'YP8NW': 'WATER',
    }
    reason_code = request.GET.get('reason', None)
    reason = reasonList.get(reason_code)
    if reason is None:
        messages.error(request, "Invalid reason code.")
        return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))

    user = request.user
    classGroup = request.GET.get('class', None)
    try:
        class_instance = Classes.objects.get(id=classGroup)
    except Classes.DoesNotExist:
        messages.error(request, "Class not found.")
        return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))

    try:
        user_instance = Account.objects.get(user=user)
    except Account.DoesNotExist:
        messages.error(request, "User account not found.")
        return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))

    try:
        AlreadyLogged = StudentHelp.objects.get(user=user_instance, classid=class_instance, reason=reason)
    except StudentHelp.DoesNotExist:
        AlreadyLogged = None

    if not AlreadyLogged:
        ininclass = ClassList.objects.filter(UserID=user_instance, ClassID=class_instance).exists()
        if ininclass:
            newLog = StudentHelp(classid= class_instance,reason=reason, user=user_instance)
            newLog.save()

            log_action(user_instance, 'CREATE_HELP_LOG_REQUEST', f'Successfully created a help request with reason: {reason}, in class id {class_instance.id}')
            messages.success(request, "Help request created successfully.")
        else:
            messages.error(request, "You are not in this class.")
    else:
        log_action(user_instance, 'CREATE_HELP_LOG_REQUEST', f'Failed to create due to already being logged')
        messages.error(request, "Already logged.")

    return redirect(request.META.get('HTTP_REFERER', 'default-view-name'))
