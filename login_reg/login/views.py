from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('你好')

def index(request):
    return render(request, 'index.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    #content = request.GET.get("chat")
    #print(content)
    content = request.POST.get("chat")
    c = len(content)
    return render(request, 'result.html', {'count':c})

def login(request):
    # 以get方式提交过来
    if request.method == 'GET':
        return render(request, 'login.html')
    # 以post方式提交过来
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=='admin' and password == 'admin':
            return render(request, 'index.html',{'username': username})

        else:
            return render(request,'login.html',{'error_msg':'用户名或密码错误！'})
