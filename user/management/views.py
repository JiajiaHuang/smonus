import json
import time

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core.session.ManageSession import getheader_info
from user.models import UserProfile, PersonalProfile


@login_required
def index(request):
    """
    # 管理首页
    :param request:
    :return:
    """
    print('index', request.session.get('is_login'))
    header_info = getheader_info(request)

    return render(request, "backstage/userauth/pagefile/page/index.html", {"header_info": header_info})


class Login(View):
    """
    # 登录页面
    """

    def get(request):
        print(request.session.get('is_login'))
        if request.session.get('is_login', None):
            return HttpResponseRedirect(reverse('management-admin/index.html'))
        else:
            return render(request, "backstage/userauth/pagefile/page/login.html")

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        next = request.GET.get('next', '')

        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        macpw = make_password(pass_word, "importlib", 'pbkdf2_sha256')
        # 实例化用户，然后赋值
        user = auth.authenticate(username=user_name, password=pass_word)
        print(user)
        print('user_name:', user_name, 'pass_word', pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                # 更新最后登录时间
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                user.last_login = now_time
                user.save(force_update=True)
                request.session["user_id"] = user.id
                request.session['is_login'] = True
                request.session['user_name'] = user.username
                request.session.set_expiry(60 * 60 * 2)
                if next == "":
                    return HttpResponseRedirect("index.html")
                else:
                    return HttpResponseRedirect(next)


        return HttpResponseRedirect('/management-admin/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/management-admin/login.html')


@login_required
class PersonalInformation(View):
    def get(request):
        header_info = getheader_info(request)

        return render(request, "backstage/user/page/information.html", {"header_info": header_info})

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        return HttpResponseRedirect('/management-admin/index.html')


@login_required
class ResetPassword(View):
    """
    修改密码
    """

    def get(request):
        header_info = getheader_info(request)
        return render(request, "backstage/user/page/resetpassword.html", {"header_info": header_info})

    @csrf_exempt
    def post(request):
        user_id = request.session.get('user_id')
        try:
            user = UserProfile.objects.get(id=user_id)
        except:
            user = PersonalProfile.objects.get(id=user_id)
        password = request.POST.get("password", "")
        user.password = make_password(password, "importlib", 'pbkdf2_sha256')
        user.save()
        return HttpResponseRedirect("/management-admin/index.html")


@login_required
class ManageAdmin(View):
    """
    用户管理
    """

    def get(request):
        header_info = getheader_info(request)
        user_all = PersonalProfile.objects.all()
        return render(request, "backstage/user/page/changeaccount.html",
                      {"header_info": header_info, "userall": user_all})

    @csrf_exempt
    def post(request):
        try:
            cz = request.POST['cz']
            zh = request.POST['zh']
            mm = request.POST['mm']
        except:
            return HttpResponse(json.dumps({
                "isSuccess": False,
            }))
        try:
            if cz == "add":
                macpw = make_password(mm, "importlib", 'pbkdf2_sha256')
                PersonalProfile.objects.create(username=zh, password=macpw, Clear_Password=mm)
                return HttpResponse(json.dumps({
                    "isSuccess": True,
                    'f': "成功！"
                }))
            elif cz == "xg":
                pp = PersonalProfile.objects.filter(username=zh)
                if len(pp) == 0:
                    return HttpResponse(json.dumps({
                        "isSuccess": False,
                    }))
                macpw = make_password(mm, "importlib", 'pbkdf2_sha256')
                pp.update(password=macpw, Clear_Password=mm)
                return HttpResponse(json.dumps({
                    "isSuccess": True,
                    'f': "成功！"
                }))
            elif cz == "sc":
                pp = PersonalProfile.objects.filter(username=zh)
                if len(pp) == 0:
                    return HttpResponse(json.dumps({
                        "isSuccess": False,
                    }))
                PersonalProfile.objects.get(username=zh).delete()
                return HttpResponse(json.dumps({
                    "isSuccess": True,
                    'f': "成功！"

                }))
            else:
                return HttpResponse(json.dumps({
                    "isSuccess": False,
                }))
        except:
            return HttpResponse(json.dumps({
                "isSuccess": False,
            }))
