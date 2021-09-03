from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from userblogs.serialiser import UserSerializer,BlogSerializer
from userblogs.models import Users,Blogs
from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

# Create your views here.
@csrf_exempt
def post_create(request):
    getMessage = request.POST.get("message")
    getId = request.session['uid']
    mydata = {"message": getMessage, "userid": getId}
    message_serialise = BlogSerializer(data=mydata)
    if (message_serialise.is_valid()):
        message_serialise.save()
        return HttpResponse("Saved")
    else:
        return HttpResponse(message_serialise.errors())    



@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getUsers = Users.objects.filter(username=getUsername, password=getPassword)
        user_serialiser = UserSerializer(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                getId = i["id"]
                getName = i["name"]
                getUsername = i["username"]
            # Session set 
            request.session['uid'] = getId
            request.session['uname'] = getName
            #Session 
                 
            return render(prof_view)


        else:
            return HttpResponse("Invalid Credentials")        
            
            
    except Users.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")
        


@csrf_exempt
def prof_view(request):

    try:
        getUid = request.session['uid']
        getUsers = Users.objects.get(id=getUid)
        user_serialiser = UserSerializer(getUsers)
         

        return render(request, 'profile.html',{"data":user_serialiser.data})    
    except:
        return HttpResponse("Something went wrong....")      

def loginview(request):
    return render(request, 'login.html')
def regview(request):
    return render(request, 'register.html')

def addpost(request):
    return render(request, 'addpost.html')    

@csrf_exempt
def retrievepost(request):
    try:
        getUid = request.session['uid']
        getPosts = Blogs.objects.filter(userid=getUid)
        message_serialiser = BlogSerializer(getPosts, many=True)
         

        return render(request, 'viewblogs.html',{"data":message_serialiser.data})    
    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def user_create(request):
    if (request.method == "POST"):

        try:
            getUsername = request.POST.get("username")
            getPassword = request.POST.get("password")
            getUsers = Users.objects.filter(username=getUsername)
            user_serialiser = UserSerializer(getUsers, many=True)
            print(user_serialiser.data)
            if (user_serialiser.data):
                
                return HttpResponse("User Already Exists")


            else:
                user_serialize = UserSerializer(data=request.POST)
                if (user_serialize.is_valid()):
                    user_serialize.save()  #Save to Db
                    return redirect(loginview)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
        except Users.DoesNotExist:
            return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")


     
        
   

    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

