from django.contrib import admin

# Register your models here.
from .models import StudentHelp, Log, StudentHelpLog

admin.site.register(StudentHelp)
admin.site.register(Log)
admin.site.register(StudentHelpLog)