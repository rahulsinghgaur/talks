from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Friend,Messages
from .serializer import MessageSerializer,FriendSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        friendlist = []
        friendlist = Friend.objects.filter(username=request.user)
        friendlist = friendlist[0].friends.split(":")
        dic={"friend":friendlist}
        return render(request,"index.html",dic)

    else:
        return redirect("/signin")



def signup(request):
    if request.method == "POST":
        n = request.POST["name"]
        first_name, last_name = n.split()
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        date = datetime.now()
        user = User.objects.create_user(username,email,password,first_name=first_name,last_name=last_name,date_joined = date)
        frnd = Friend(username=username)
        if user is not None:
            user.save()
            frnd.save()
            return redirect("/signin")
        return HttpResponse("Register Fail")
    return render(request,"signup.html")

def signin(request):
    if request.method== "POST":
        username = request.POST.get("username")
        password = request.POST["password"]
        user = authenticate(request,username= username, password= password)
        if user != None:    
            login(request,user)
            return redirect("/",user)                  
        else:
            return HttpResponse("Login Fail")
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect("/signin")





@csrf_exempt
def messagelist(request,id=None):
    if request.method == 'GET':
        msg = Messages.objects.filter(key=id)
        serializer = MessageSerializer(msg,many=True)
        # json_data = JSONOpenAPIRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Data Entered"}
            jdata = JSONOpenAPIRenderer().render(res)
            return HttpResponse(jdata,content_type = 'application/json')
        return JsonResponse(serializer.errors)

@csrf_exempt
def friendlist(request,id=None):
    if request.method =='GET':
        frnd = Friend.objects.filter(username__startswith=id)
        serializer = FriendSerializer(frnd,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == "POST":
        data =JSONParser().parse(request)
        friendlist = Friend.objects.filter(username=data['r'])
        sfriendlist = Friend.objects.filter(username=data['s'])
        friendlist = friendlist[0].friends
        sfriendlist = sfriendlist[0].friends
        if friendlist == "":
            friendlist=data['s']
            f = Friend.objects.get(username=data['r'])
            f.friends=friendlist
            f.save()
            if sfriendlist=="":
                sfriendlist = data['r']
                s = Friend.objects.get(username=data['s'])
                s.friends=sfriendlist
                s.save()
            else:
                sfriendlist = data['r']+":"+sfriendlist
                s = Friend.objects.get(username=data['s'])
                s.friends=sfriendlist
                s.save()
        else:
            friendlist=data['s']+":"+friendlist
            f = Friend.objects.get(username=data['r'])
            f.friends=friendlist
            f.save()
            if sfriendlist=="":
                sfriendlist = data['r']
                s = Friend.objects.get(username=data['s'])
                s.friends=sfriendlist
                s.save()
            else:
                sfriendlist = data['r']+":"+sfriendlist
                s = Friend.objects.get(username=data['s'])
                s.friends=sfriendlist
                s.save()

        return JsonResponse(friendlist,safe=False)
