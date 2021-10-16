from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('registration', views.registration,name="registration"),
    path('progress', views.progress,name="progress"),
    path('fee', views.fee_record, name="fee"),
    path('student_record', views.student_record, name="student_record"),
    path('account_record', views.account_record, name="account_record"),
    path('expense', views.expense, name="expense"),
]
