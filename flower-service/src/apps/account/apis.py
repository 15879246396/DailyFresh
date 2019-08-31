# coding=utf-8
import requests
from rest_framework import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from base.exceptions import LogicException, ValidateException
from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view

from account.models import MyUser
from account.utils import str2md5
from common.decorator import common_api
from social_django.utils import load_strategy

from common.utils import generate_access_token

PROVIDER = '_WEAAPP'
strategy = load_strategy()
SOCIAL_AUTH_STORAGE = strategy.storage

class WEAAPPAuthAPI(APIView):
    URL = 'https://api.weixin.qq.com/sns/jscode2session'

    @common_api
    def post(self, request):
        code = request.data.get("code")
        if not code:
            raise ValidateException().add_message('error:param', 'Incomplete Params!')

        params = {
            'appid': settings.WEAAPP_KEY,
            'secret':settings.WEAAPP_SECRET,
            'js_code': code,
            'grant_type': 'authorization_code',
        }
        data = requests.post(self.URL, data=params, timeout=600)
        json_data = data.json()
        openid = json_data['openid']
        unionid = json_data.get('unionid', '')
        # MyUser.objects.get_or_create(provider='_WEAAPP', uid=openid, unionid=unionid)
        social = SOCIAL_AUTH_STORAGE.user.get_social_auth(PROVIDER, openid)
        if social:
            user = social.user
        else:
            user, _created = MyUser.objects.get_or_create(
                openid=openid,
                unionid=unionid,
                provider='_WEAAPP',
            )
            SOCIAL_AUTH_STORAGE.user.create_social_auth(user, openid, PROVIDER)

        login(request, user)
        access_token = generate_access_token(user)
        result = {
            'data': {
                'openid': openid,
                'unionid': unionid,
                # 'is_staff': user.is_staff,
                'nick_name': user.nick_name,
                'pic': user.pic,
                'access_token': access_token.token,
            }
        }
        return Response(result)


@api_view(['POST'])
@common_api
def log_in(request):
    user_data = request.data
    name = user_data.get('username', None)
    pwd = user_data.get('password', None)

    if not all((name, pwd)):
        raise LogicException('error:error', 'Incomplete Params!')
    try:
        kjzd_user = KjzdUser.objects.using('kjzd').get(tel=name)
    except Exception:
        raise LogicException('error:error', 'User Not Found')

    if kjzd_user.password == str2md5(str(pwd)):
        user, _ = MyUser.objects.get_or_create(kjzd_user_id=kjzd_user.id,
                                               defaults={'email': kjzd_user.email,
                                                         'name': kjzd_user.nick,
                                                         'phone': kjzd_user.tel,
                                                         'password':kjzd_user.password})
        login(request, user)
        user_info = {
            'nickname': user.name,
            'phone': user.phone,
            'kjzd_user_id': user.kjzd_user_id,
            'is_manager': False
        }
        if user.has_perm('account.can_login_cms'):
            user_info['is_manager'] = True

        return Response(user_info)
    else:
        # raise LogicException('error:error', 'Password Not Right')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')