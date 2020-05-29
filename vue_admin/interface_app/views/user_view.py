import json

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods

from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from interface_app.froms.user_form import UserForm
from interface_app.libs.response import response_failed, response_success, ErrorCode



@require_http_methods(['POST'])
def loginHttpMethods(request,*args,**kwargs):
    """
    登录
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    body = request.body
    data = json.loads(body,encoding='utf-8')

    user_form = UserForm(data)
    if not user_form.is_valid():
        # if not user_form.cleaned_data["username"]:
        #     return response_failed(message="用户名或密码不能为空")
        # if not user_form.cleaned_data["password"]:
        #     return response_failed(message="用户名或密码不能为空")

        return response_failed(message="用户名或密码不能为空")


    user = authenticate(username=user_form.cleaned_data["username"],password=user_form.cleaned_data["password"])
    if not user:
        return response_failed(code=ErrorCode.auth,message="用户名或密码错误")
    else:
        login(request,user) #登录持久化，告诉浏览器每次请求接口，需要带上session给后台
        return response_success()

@require_http_methods(['POST'])
def registerHttpMethods(request,*args,**kwargs):
    """
    注册
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body,encoding='utf-8')
    user_form = UserForm(data)

    if not user_form.is_valid():
        return response_failed(code=ErrorCode.common,message='用户名或密码不能为空')

    if User.objects.filter(username=user_form.cleaned_data["username"]).exists():
        return response_failed(code=ErrorCode.common,message='用户已存在')

    user = User.objects.create_user(username=user_form.cleaned_data["username"]
                                    ,password=user_form.cleaned_data["password"])
    if not user:
        return response_failed(code=ErrorCode.common,message='注册失败')
    else:
        # login(request,user)#登录持久化
        return response_success()


@require_http_methods(['GET'])
def logoutHttpMethods(request,*args,**kwargs):
    """
    注销
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    logout(request)
    return response_success()

@require_http_methods(['GET'])
def getUserInfoHttpMethods(request,*args,**kwargs):
    """
    获取用户登录信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    user = request.user
    if not user:
        return response_failed(code=ErrorCode.auth,message='用户未登录')
    if user.is_authenticated:
        return response_success(
            data={
                'id':user.id,
                'name':user.username
            }
        )
    else:
        return response_failed(code=ErrorCode.auth,message='用户未登录')



