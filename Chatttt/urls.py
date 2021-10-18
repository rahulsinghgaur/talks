from django.contrib import admin
from django.urls import path
from Chatttt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("msg/<str:id>",views.messagelist,name ="messagelist"),
    path("msg/",views.messagelist,name ="messagelist"),
    path("frnd/<str:id>",views.friendlist,name ="friendlist"),
    path("frnd/",views.friendlist,name ="friendlist"),
]