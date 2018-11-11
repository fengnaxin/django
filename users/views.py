from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("hello world")


def weather(request, city, year):
    # 通过正则表达式提取参数的方法从URL中获取请求参数
    return HttpResponse("%s年%s天气,晴朗" % (year, city))


def get_param(request):
    # 获取到?后面的字符串参数
    # GET与客户端的请求方式无关
    a = request.GET.get("a")
    b = request.GET.get("b")
    a_list = request.GET.getlist("a")
    print("a的值为%s\nb的值为%s" % (a, b))
    return HttpResponse("a的值为%s\t b的值为%s a_list=%s" % (a, b, a_list))
