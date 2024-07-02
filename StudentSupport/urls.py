from django.urls import path, include

from . import views as studentViews
from . import logger as Logger
urlpatterns = [
    path('addLog/', studentViews.addToLog),
    path('getLog/', Logger.getLog),
    path('fullStudentLog/', Logger.getFullStudentHelpLog),
    path('class/<int:id>', Logger.getClassStudentHelpLog)
]