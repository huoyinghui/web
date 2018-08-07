from django.shortcuts import render
# Django自带的用户验证,login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q

from .forms import LoginForm
from .models import UserProfile
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
    pass