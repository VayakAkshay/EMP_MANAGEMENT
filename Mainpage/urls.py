from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home,name="Home"),
    path('about/',views.aboutpage,name="aboutpage"),
    path('tasks/',views.taskpage,name="taskpage"),
    path('taskdetails/',views.taskdetail,name = "taskdetail"),
    path('complete/',views.completetask,name="completetask"),
    path('profile/',views.profilepage,name="profilepage"),
    path('logout/',views.logout_page,name="logout_page"),
    path('edit-profile/',views.edit_profile,name="edit_profile"),
    path('leaves/',views.Leaves_page,name="Leaves_page"),
    path('salary-slip/',views.salary_slip,name="salary_slip"),
    path('attendance/',views.attendance,name="attendance"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)