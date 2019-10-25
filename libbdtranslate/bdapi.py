import http.client
import hashlib
import urllib
import random
import json


class Instance:
    def __init__(self, appid, key):
        self._appid = appid
        self._key = key

    # 临时的 fake translator，此处需要加入对 百度翻译API 的 restful 调用
    # 此函数的功能是将 word 翻译成中文，以字符串形式返回
    # 修改功能后，需要去掉静态方法修饰器
    @staticmethod
    def translate(word):
        return "中文"

    def translatew(self, word, fromLang, toLang):
        salt = random.randint(32768,65536)
        sign = self._appid + word + str(salt)+self._key
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = '/api/trans/vip/translate'
        url += '?appid=' + self._appid + '&q=' + urllib.parse.quote(word)\
            + '&from=' + fromLang + '&to=' + toLang + '&salt='\
            + str(salt) + '&sign=' + sign
        try:
            http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
            http_client.request('GET', url)
            response = http_client.getresponse()
            result_all = response.read().decode("UTF-8")
            result = json.loads(result_all)
            print(result)
        except Exception as e:
            print(e)
        finally:
            if http_client:
                http_client.close()
