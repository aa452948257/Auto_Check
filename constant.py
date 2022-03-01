import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
    "ismoved": 0,
    "jhfjrq": "",
    "jhfjjtgj": "",
    "jhfjhbcc": "",
    "sfxk": 0,
    "xkqq": "",
    "szgj": "",
    "szcs": "",
    "zgfxdq": "0",
    "mjry": "0",
    "csmjry": "0",
    "ymjzxgqk": "已接种",
    "xwxgymjzqk": 3,
    "address": "北京市海淀区北太平庄街道西土城路辅路北京邮电大学海淀校区",
    "area": "北京市  海淀区",
    "bztcyy": "",
    "city": "北京市",
    "geo_api_info": "{\"type\":\"complete\",\"position\":{\"Q\":39.9592054579,\"R\":116.35530354817797,\"lng\":116.355304,\"lat\":39.959205},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":128,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"北下关\",\"id\":\"110108\",\"location\":{\"Q\":39.955976,\"R\":116.33873,\"lng\":116.33873,\"lat\":39.955976}},{\"name\":\"西直门\",\"id\":\"110102\",\"location\":{\"Q\":39.942856,\"R\":116.34666099999998,\"lng\":116.346661,\"lat\":39.942856}},{\"name\":\"小西天\",\"id\":\"110108\",\"location\":{\"Q\":39.957147,\"R\":116.364058,\"lng\":116.364058,\"lat\":39.957147}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"学院南路\",\"streetNumber\":\"44号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"towncode\":\"110108008000\",\"township\":\"北太平庄街道\"},\"formattedAddress\":\"北京市海淀区北太平庄街道西土城路辅路北京邮电大学海淀校区\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
    "glksrq": "",
    "gllx": "",
    "gtjzzfjsj": "",
    "jcbhlx": "",
    "jcbhrq": "",
    "jchbryfs": "",
    "jcjgqr": "0",
    "jcwhryfs": "",
    "province": "北京市",
    "qksm": "",
    "remark": "",
    "sfcxtz": "0",
    "sfcxzysx": "0",
    "sfcyglq": "0",
    "sfjcbh": "0",
    "sfjchbry": "0",
    "sfjcwhry": "0",
    "sfjzdezxgym": 1,
    "sfjzxgym": 1,
    "sfsfbh": 0,
    "sftjhb": "0",
    "sftjwh": "0",
    "sfygtjzzfj": 0,
    "sfyyjc": "0",
    "sfzx": 1,
    "szsqsfybl": 0,
    "tw": "2",
    "xjzd": "北京邮电大学学三1215"
}"""
 

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

