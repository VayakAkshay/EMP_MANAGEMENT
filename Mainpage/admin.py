from django.contrib import admin
from .models import Profiles,LeaveManager,TaskManager,attendacemanager,SalaryTable,Roles,DepartmentList
# Register your models here.
admin.site.register(Profiles)
admin.site.register(TaskManager)
admin.site.register(LeaveManager)
admin.site.register(attendacemanager)
admin.site.register(SalaryTable)
admin.site.register(Roles)
admin.site.register(DepartmentList)


class ImageAdmin(admin.ModelAdmin):
    list_display = ["profile_id","profile_img"]