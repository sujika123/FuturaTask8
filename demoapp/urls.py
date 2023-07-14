from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginview', views.loginview, name='loginview'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('register', views.register, name='register'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('studenthome', views.studenthome, name='studenthome'),
    path('studentview', views.studentview, name='studentview'),
    path('approve_student/<int:id>/', views.approve_student, name='approve_student'),
    path('reject_student/<int:id>/', views.reject_student, name='reject_student'),
    path('addnotification', views.addnotification, name='addnotification'),
    path('viewnotification', views.viewnotification, name='viewnotification'),
    path('sviewnotification', views.sviewnotification, name='sviewnotification'),
    path('complaint_add_student', views.complaint_add_student, name='complaint_add_student'),
    path('complaint_studentview', views.complaint_studentview, name='complaint_studentview'),
    path('stdntcomplaint_view', views.stdntcomplaint_view, name='stdntcomplaint_view'),
    path('reply_studntcomplaint/<int:id>/',views.reply_studntcomplaint, name='reply_studntcomplaint'),



]