from django.db import models
from django.contrib.auth.models import User
from accounts.models import Classes, Account
import datetime
import pytz
# Create your models here.
Reason_lsit = {
    "HAND_UP": 'hand_up',
    "TOILET": 'toilet',
    "WATER": 'water'
}
user_action_list ={
    "JOIN_CLASS_REQUEST":'join class request',
    "CREATE_HELP_LOG_REQUEST": 'create help log requet'
}



class Log(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    datelogged = models.DateTimeField("Date Logged", default=pytz.utc.localize(datetime.datetime.now()))
    userAction = models.CharField(max_length=50, choices=user_action_list)
    details = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.userAction} - {self.datelogged}"


class StudentHelp(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField("date posted", auto_now_add=True)
    classid = models.ForeignKey(Classes, on_delete=models.CASCADE)
    reason = models.CharField(max_length=9, choices=Reason_lsit)

class StudentHelpLog(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    datelogged = models.DateTimeField("Date Logged", default=pytz.utc.localize(datetime.datetime.now()))
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    reason = models.CharField(max_length=9, choices=Reason_lsit)

    def __str__(self):
        return f"{self.classes} - {self.datelogged}"
