from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path("check",views.check,name="index"),
    path("register",views.register,name="register"),
    path("logout",views.logout,name="logout"),
    path("reportincident",views.reportincident,name="reportincident"),
    path("loggedpage",views.loggedpage,name="loggedpage")
]
