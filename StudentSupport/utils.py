from accounts.models import Classes, ClassList, Account

def is_on_group_check(*groups):
    def on_group_check(user):
        if user.groups is None:
            return False
        return user.groups.filter(name__in=groups).exists()

    return on_group_check
def is_user_in_class(classid):
    def in_class_check(user):
        class_instance = Classes.objects.get(id=classid)

        user_instance = Account.objects.get(user=user)

        return ClassList.objects.get(UserID=user_instance, ClassID=class_instance).exists()

    return in_class_check

def getClassFromID(id):
    return Classes.objects.get(id=id)
