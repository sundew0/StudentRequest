from django.db import models#type: ignore
from django.contrib.auth.models import User#type: ignore

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    IsTeacher = models.BooleanField("Is Teacher", default=False)
    Grade = models.IntegerField('Grade', null=True)
    def __str__ (self):
        return f"username: {self.user},  Teacher: {self.IsTeacher}"



class Classes(models.Model):
    ClassName = models.CharField(max_length=100, null=True)
    Subject = models.CharField(max_length=50, null=True)
    id = models.AutoField(primary_key=True)
    ClassCode = models.CharField(max_length=6, null=True, verbose_name="Class Code")
    ClassJoinCode = models.CharField(max_length=6, null=True, unique=True, verbose_name="join Code")
    Teachers = models.ManyToManyField(User)

    def __str__(self):
        return f"id: {self.id}, Class name: {self.ClassName},  Subject: {self.Subject}, Teachers: {self.Teachers}"


class ClassList(models.Model):
    UserID = models.ForeignKey(Account, on_delete=models.CASCADE)
    ClassID = models.ForeignKey(Classes, on_delete=models.CASCADE)  #
    Teacher = models.BooleanField("IsTeacher")

    def __str__(self):
        return f"{self.UserID} {self.ClassID}: {self.Teacher}"
