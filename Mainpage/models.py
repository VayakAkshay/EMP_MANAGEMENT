from django.db import models
import datetime
from django import forms
# Create your models here.

class Profiles(models.Model):
    profile_id = models.IntegerField(default=0)
    profile_img = models.ImageField(upload_to="profile_img")
    full_name = models.TextField(max_length=100,default="")
    email_id = models.EmailField(max_length=100,default="")
    mobile_no = models.IntegerField(default=0)
    department_name = models.TextField(max_length=100,default="")
    dateofbirth = models.DateField(default=datetime.date.today)
    dateofjoin = models.DateField(default=datetime.date.today)
    salary = models.IntegerField(default=0)
    gender = models.TextField(max_length=15,default="")
    address = models.TextField(max_length=300,default="")
    role = models.TextField(max_length=50,default = "")

    def __str__(self):
        return str(self.profile_id) + " - " + self.full_name

class TaskManager(models.Model):
    task_id = models.AutoField
    task_name = models.TextField(max_length=100,default="")
    task_detail = models.TextField(max_length=5000,default="")
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    status = models.TextField(max_length=50,default="Remaining")
    priority = models.IntegerField(default=0)
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return self.task_name + " - " + str(self.emp_id)
    
LEAVE_CHOICES = (
    ("In Waiting", "In Waiting"),
    ("Approved", "Approved"),
    ("Rejected","Rejected"),
)

class LeaveManager(models.Model):
    leave_id = models.AutoField
    leave_type = models.TextField(max_length=500,default="")
    leave_reason = models.TextField(max_length=5000,default="")
    start_date = models.DateField(default = datetime.date.today)
    end_date = models.DateField(default = datetime.date.today)
    status = models.TextField(max_length=30,choices=LEAVE_CHOICES,default = 'In Waiting')
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.emp_id)

class attendacemanager(models.Model):
    attendance_id = models.AutoField
    attendance_date = models.DateField(default=datetime.date.today)
    arrival_time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S")) # type: ignore
    attendance_desc = models.TextField(max_length=30,default="")
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.emp_id)

class Roles(models.Model):
    role_id = models.AutoField
    role_name = models.TextField(max_length=50,default="")
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.emp_id) + self.role_name

class SalaryTable(models.Model):
    salary_id = models.AutoField
    emp_id = models.IntegerField(default=0)
    months = models.TextField(max_length=50,default="")
    gross_salary = models.IntegerField(default=0)
    PF = models.IntegerField(default=0)
    PT = models.IntegerField(default=0)
    gross_deduct = models.IntegerField(default=0)
    Net = models.IntegerField(default=0)
    status = models.TextField(max_length=30,default="")

    def __str__(self):
        return str(self.emp_id) + " - " + self.months

class DepartmentList(models.Model):
    department_id = models.AutoField
    department_name = models.TextField(max_length=200,default="")

    def __str__(self):
        return self.department_name