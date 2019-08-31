import requests
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from service_mart import settings

from account.models import KjzdUser, MyUser


class IsLogin(permissions.BasePermission):
    def has_permission(self, request, view):
        sessionId = request.META.get("HTTP_SESSIONID")
        token = request.META.get("HTTP_TOKEN")        

        if not sessionId or not token:
            return False
        url = settings.GATEWAY_URL
        data = {
            "sessionId": sessionId,
            "token": token,
        }
        res = requests.post(url, headers=data).json()
        if res.get("code", True):
            return False
        user_info = res["data"]["userInfo"]
        tel = user_info.get("mobile")
        try:
            kjzd_user = KjzdUser.objects.using('kjzd').get(tel=tel)
        except Exception:
            return False
        user, _ = MyUser.objects.get_or_create(kjzd_user_id=kjzd_user.id,
                                               defaults={'email': kjzd_user.email,
                                                         'name': kjzd_user.nick,
                                                         'phone': kjzd_user.tel,
                                                         'password': kjzd_user.password})
        if not IsAuthenticated().has_permission(request, view):
            login(request, user)
        return True

