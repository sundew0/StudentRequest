

from django.http import HttpResponse#type: ignore
from django.contrib.auth.decorators import login_required, user_passes_test#type: ignore
from django.shortcuts import render#type: ignore
from StudentSupport.utils import is_on_group_check, getClassFromID, is_user_in_class#type: ignore

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