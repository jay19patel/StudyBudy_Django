from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from main_app.models import *
from django.contrib.auth.decorators import login_required

def HomePage(request):
    try:
        data= Room.objects.all()
        context={'data':data}
        return render(request,'Home.html',context)
    except:
        return render(request,'Home.html')

def RoomPage(request,id):
    room_data= Room.objects.get(id=id)
    context={'room':room_data}
    return render(request,'Room.html',context)

def LoginPage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            print('username is valid',user)
        except:
            print('enter corrrect user and password')

        user= authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            print("login sucessfulyy")
            return redirect('HomePage')
        else:
            print('username or password not exist')
    return render(request,'Login.html')

def Logout(request):
    logout(request)
    print("logout")
    return redirect('HomePage')

def RegistrationPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).first():
            print("Username already exists")
            return redirect("registerPage")
        else:
            a = User.objects.create_user(username,password1,password2)
            a.save()
            if a:
                user = authenticate(username=username,password=password1)
                if user is not None:
                    login(request,user)
                    print("Registration Successfuly")
                    return redirect('Update_Profile')
    return render(request,'Registration.html')

def Update_Profile(request):
    if request.method == 'POST':
        user = request.user
        full_name = request.POST['full_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        profile = request.FILES['profile']
        skills = request.POST['skills']
        bio = request.POST['bio']
        city = request.POST['city']

        data = Profilemodel.objects.create(
            user=user,full_name=full_name,email=email,phone_no=mobile_number,location=city,skills=skills,image=profile,bio=bio
            )
        data.save()
        return redirect('HomePage')
    user_data = Profilemodel.objects.filter(id=request.user.id)
    context={'room':user_data}
    return render(request,'full_Registration.html',context)


# ROOM 


@login_required(login_url ='LoginPage')
# jyre bhi koy kam karvanu hoy to login reva j joyye ena mate decoreter vapray  and login ni rey to login url thi login page ma jay rey
def CreatRoom(request):
    if request.method == 'POST':
        auther_name = request.user
        topic_name = request.POST.get('topic_name')
        room_name = request.POST.get('room_name')
        topic = Topic.objects.create(name=topic_name)
        room = Room.objects.create(auther_name=auther_name, topic_name=topic, room_name=room_name)
        print("Room is Created ")
        return redirect('HomePage')

    return render(request,'Create_Room.html')


@login_required(login_url ='LoginPage')
def DeleteRoom(request,id):
    room=Room.objects.get(id=id)
    print("delete valu")
    room.delete()
    return redirect('HomePage')


def Main_RoomPage(request,id):
    room_data= Room.objects.get(id=id)
    context={'room':room_data}
    return render(request,'Room_main.html',context)


@login_required
def join_room(request,id,auther): # here id atle room id and auther atle room no auther 
#   JOin GOroup
    request.user.following.add(Room.objects.get(id=id))
    room = get_object_or_404(Room, id=id)
    follower = room.follower.all()
    
#  Chat With Gourp
    room= Room.objects.get(id=id)
    room_messages = room.message_set.all()

    if request.method=='POST':
        message= Message.objects.create(
            room=room,
            sender=request.user,
            Messages=request.POST.get('Message'))
        return redirect('join_room',id =room.id,auther=room.auther_name)


    # room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    # sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages',null=True)
    # receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages',null=True)
    # Messages = models.TextField(null=True)


    context={"room_subs":follower,"id":id,"auther":auther,"room_messages":room_messages,"room":room}
    return render(request,'Room_main.html',context)


# def Chat_all(request,id):
#     room= Room.objects.get(id=id)
#     room_messages = room.message_set.all()

#     if request.method=='POST':
#         message= Message.objects.create(
#             user=request.user,
#             room=room,
#             body=request.POST.get('Message'))
#         return redirect('room',pk=room.id)

    # context= {'room':room,'room_messages':room_messages}
    # return render(request,'Chat.html',context)
