from .models import Log, StudentHelpLog
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test

from .utils import is_on_group_check, getClassFromID

@login_required(redirect_field_name='registration/login/')
def log_action(user, action, details):
    log_entry = Log.objects.create(
        userAction=action,
        details=details,
        user=user
    )
    print(user)


    log_entry.save()



def getLog(request):


    now = datetime.datetime.now()
    print(now)
    logData = Log.objects.all()

    return render(request, 'logs.html', {'Logs': logData})

@user_passes_test(is_on_group_check('teacher'))
def getFullStudentHelpLog(request):
    print('test')
    print(is_on_group_check('teacher'))
    log_data = StudentHelpLog.objects.all()

    return render(request, 'StudentHelpLog.html', {'Logs': log_data})

@user_passes_test(is_on_group_check('teacher'))
def getClassStudentHelpLog(request, classid):
    print(getClassFromID(classid))
    print(classid)
    print(is_on_group_check('teacher'))
    log_data = StudentHelpLog.objects.get(classes=classid)

    return render(request, 'StudentHelpLog.html', {'Logs': log_data})