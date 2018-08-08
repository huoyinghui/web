from django.shortcuts import render
# Django自带的用户验证,login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import UserProfile
from message.models import UserMessage
# Create your views here.


class LogoutView(View):
    """

    """
    def get(self, request):
        # django自带的logout
        logout(request)
        # 重定向到首页,
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    """

    """
    def get(self, request):
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if not login_form.is_valid():
            return render(request, "login.html", login_form)

        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if not user:
            return render(request, "login.html", {"msg": "用户名或密码错误!"})

        if not user.is_active:
            return render(request, 'login.html', {"msg": "用户名未激活! 请前往邮箱进行激活"})

        login(request, user)
        redirect_url = request.POST.get('next', '')
        if not redirect_url:
            return HttpResponseRedirect(reverse("index"))

        return HttpResponseRedirect(redirect_url)


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


# 注册功能的view
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm(request.POST)
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if not register_form.is_valid():
            return render(request, 'register.html', {'register_form': register_form})
        # form ok
        email = request.POST.get("email", "")
        if UserProfile.objects.all().filter(email=email):
            return render(request, 'register.html', {
                'register_form': register_form,
                'msg': '用户已存在',
            })

        password = request.POST.get('password', '')

        try:
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()
        except Exception as e:
            print(e)
            return render(request, '500.html')
        #还原消息
        # user_message = UserMessage()
        # user_message.user
        return render(request, "login.html")
