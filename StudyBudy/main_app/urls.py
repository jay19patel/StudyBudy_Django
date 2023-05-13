from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="HomePage"),
    path("RoomPage/<str:id>/", views.RoomPage, name="RoomPage"),
    path("LoginPage", views.LoginPage, name="LoginPage"),
    path("Logout", views.Logout, name="Logout"),
    path("RegistrationPage", views.RegistrationPage, name="RegistrationPage"),
    path("Update_Profile", views.Update_Profile, name="Update_Profile"),


    path("CreatRoom", views.CreatRoom, name="CreatRoom"),
    path("DeleteRoom/<str:id>/", views.DeleteRoom, name="DeleteRoom"),

    path("Main_RoomPage/<str:id>/", views.Main_RoomPage, name="Main_RoomPage"),
    path("join_room/<str:id>/<str:auther>/", views.join_room, name="join_room")


    

]
