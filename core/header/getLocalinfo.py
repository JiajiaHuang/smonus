import json
import time
import geoip2.database
from wx_sdk import wx_sdk
import datetime,pytz

from SMONU import settings


def ip2city(ip):
    """
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    content = urllib.request.urlopen(apiurl).read()
    data = json.loads(content)['data']
    code = json.loads(content)['code']
    if code == 0:
        return data["country"], data["region"], data["city"]
    """
    read = geoip2.database.Reader(settings.CITY_DB)  # mmdb文件路径，提前在settings文件中配置好
    c = read.city(ip)  # 放入需要检测的IP
    target_country = c.country.names.get("en")
    target_city = c.city.names.get("en")
    location_time_zone = c.location.time_zone
    target = dict()
    target['target_country'] = target_country
    target['target_city'] = target_city
    target['location_time_zone'] = location_time_zone
    now = datetime.datetime.now()
    tz = pytz.timezone('Asia/Shanghai')  # 东八区

    t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone(location_time_zone)).strftime('%A,%B\t%d')
    target['location_data'] = t


    #target['location_data'] = t.replace(tzinfo=(timezone('America/Los_Angeles')))
    return target


def city2weather(citydata, APPKEY):
    url = 'https://way.jd.com/he/freeweather'
    params = {
        'city': citydata,
        'appkey': APPKEY
    }
    response = wx_sdk.wx_post_req(url, params)
    HeWeather = json.loads(response.text)
    HeWeatherDict = dict()
    HeWeatherDict['code'] = HeWeather['result']['HeWeather5'][0]['now']["cond"]['code']
    HeWeatherDict['tmp'] = HeWeather['result']['HeWeather5'][0]['now']["tmp"]
    return HeWeatherDict
