from django.db import models
from django.contrib.auth.models import User
#jaypatel
# jaypatel1911



class Profilemodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
    full_name = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    phone_no = models.CharField(max_length=200,blank=True)
    location = models.CharField(max_length=200,blank=True)
    skills = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to="ProfilePics",blank=True)
    bio = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return f" NAME : {str(self.user)} ID :{str(self.user.id)}"



class Topic(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    auther_name=models.ForeignKey(User,on_delete =models.SET_NULL,null=True)
    topic_name =models.ForeignKey(Topic,on_delete =models.SET_NULL,null=True)
    follower = models.ManyToManyField(User,related_name='following')
    room_name=models.CharField(max_length=100)
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
    


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages',null=True)
    Messages = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Sender : {self.sender} || Room :{self.room}"