from django.contrib import admin
from .models import Profiles,LeaveManager,TaskManager,attendacemanager,SalaryTable,Roles,DepartmentList

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ["profile_id","full_name","department_name","role","mobile_no","email_id","salary","dateofjoin"]

class TaskManagerAdmin(admin.ModelAdmin):
    list_display = ["emp_id","username","task_name","start_date","end_date","status","priority"]

class LeaveManagerAdmin(admin.ModelAdmin):
    list_display = ["emp_id","username","leave_type","start_date","end_date","status","leave_reason"]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["emp_id","username","arrival_time","attendance_date"]

class SalaryTableAdmin(admin.ModelAdmin):
    list_display = ["emp_id","username","months","gross_salary","gross_deduct","Net","status"]

class RolesAdmin(admin.ModelAdmin):
    list_display = ["emp_id","username","department_name","role_name"]

class DepartmentListAdmin(admin.ModelAdmin):
    list_display = ["department_name"]

admin.site.register(Profiles,ProfilesAdmin)
admin.site.register(TaskManager,TaskManagerAdmin)
admin.site.register(LeaveManager,LeaveManagerAdmin)
admin.site.register(attendacemanager,AttendanceAdmin)
admin.site.register(SalaryTable,SalaryTableAdmin)
admin.site.register(Roles,RolesAdmin)
admin.site.register(DepartmentList,DepartmentListAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ["profile_id","profile_img"]
