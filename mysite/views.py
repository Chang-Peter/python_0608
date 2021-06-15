from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
import random
from mysite.models import Post, Country, City

def index (request):
    posts = Post.objects.all()
        
    myname = "Peter"
    data=[i for i in range(1,43)]
    random.shuffle(data)
    lotto_num = data [0:6]
    special_num = data [6]
    return render(request,'index.html',locals())

def show (request,id):
    try:
        target=Post.objects.get(id=id)   #all全部,filter過濾,get抓單一
    except:
        return redirect('/')  #找不到網址回首頁
    return render(request,"showpost.html",locals())

def logout (request):
    auth.logout(request)
    return redirect("/")

def rank (request):
    cities = City.objects.all()
    return render(request, "rank.html" , locals())

def chart(request):
    cities = City.objects.all()
    return render (request, "chart.html",locals())

def team(request):
    cities = City.objects.all()
    return render (request, "team.html",locals())

def stu(request):
    cities = City.objects.all()
    return render (request, "stu.html",locals())
