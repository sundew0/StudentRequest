"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from accounts import views as accountsViews
from StudentSupport import views as studentViews
from StudentSupport import logger as Logger
from django.contrib.auth.decorators import login_required # type: ignore
from accounts.classes import getClassinfo, getClass, Create_New_Class, Create_New_Subject


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("joinclass/", accountsViews.JoinClass, name="JoinClass"),
    path('', accountsViews.Home, name="home"),
    path('addLog/', studentViews.addToLog, name='addStudentLog'),
    path('getLog/', Logger.getLog),
    path('fullStudentLog/', Logger.getFullStudentHelpLog),
    path('ClassStudentLog/<int:classid>', Logger.getClassStudentHelpLog),
    path('class/<int:id>', getClass),
    path('test/', accountsViews.testing),
    path('createClass/', Create_New_Class),
    path('createSubjects/', Create_New_Subject)
    
    ]
