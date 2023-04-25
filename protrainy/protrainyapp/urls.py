from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [


    path("create",views.create),
    path('test',views.test),
    path("create", views.create),
    path("read", views.read),
    path("reads", views.reads),
    path("edit", views.edit),
    path("verify", views.verify),
    path("login", views.login),
    path("delete", views.delete),
    path("jsonall", views.jsonall),
    path("noti", views.notification),

    path("check", views.check),
    path("check2", views.check2),



]