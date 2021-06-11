from django.utils.deprecation import MiddlewareMixin

from SMONU.settings import FREEWEATHER, LANGUAGE_CODE
from core.header.getLocalinfo import ip2city, city2weather


class SetRemoteAddrFromForwardedFor(MiddlewareMixin):
    """
    如果部署了代理，使用此中间件获取远程客户端IP。
    在settings中注册该中间件。
    """

    def process_request(self, request):
        if request.session.get('ip2country', None):
            #print(request.session.keys())
            return
        try:
            if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
                real_ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                real_ip = request.META['REMOTE_ADDR']

            if '_language' not in request.META.keys():
                request.session['_language'] = LANGUAGE_CODE

        except KeyError as err:
            print(err)
        else:
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip
            print(real_ip)
            if real_ip=="127.0.0.1":
                request.META['REMOTE_ADDR'] = '169.235.24.133'
            real_ip = request.META['REMOTE_ADDR']
            # print(real_ip)
            request.session.get('ip2country', None)
            request.session['ip2country'] = ip2city(real_ip)
            # print(1, request.session.keys())
            if 'weather' not in request.session.keys():
                request.session['weather'] = city2weather(real_ip, FREEWEATHER)
