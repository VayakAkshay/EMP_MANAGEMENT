from django.db import models
import datetime
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
    role = models.TextField(max_length="50",default = "")

    def __str__(self):
        return str(self.profile_id) + " - " + self.full_name

class TaskManager(models.Model):
    task_id = models.AutoField
    task_name = models.TextField(max_length=100,default="")
    task_detail = models.TextField(max_length=5000,default="")
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    status = models.TextField(max_length=50,default="Remaining")
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return self.task_name + " - " + str(self.emp_id)

class LeaveManager(models.Model):
    leave_id = models.AutoField
    leave_reasion = models.TextField(max_length=500,default="")
    start_date = models.DateField(default = datetime.date.today)
    end_date = models.DateField(default = datetime.date.today)
    status = models.TextField(max_length=50,default="In Waiting")
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.leave_id) + " - " + str(self.emp_id)

class attendacemanager(models.Model):
    attendance_id = models.AutoField
    attendance_date = models.DateField(default=datetime.date.today)
    arrival_time = models.TimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))
    attendance_desc = models.TextField(max_length=30,default="")
    emp_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.emp_id)