from django.contrib import admin#type: ignore
from django.contrib.auth.models import User#type: ignore
from django.contrib.auth.admin import UserAdmin#type: ignore
# Register your models here.
from .models import Classes, ClassList, Account

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class CustomUserAdmin (UserAdmin):
    inlines = (AccountInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Account)
admin.site.register(Classes)
admin.site.register(ClassList)
