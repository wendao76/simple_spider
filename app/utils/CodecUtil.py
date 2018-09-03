import base64
import hashlib
from json import JSONDecoder, JSONEncoder


# base64编码
def base64encode(s):
    return base64.b64encode(s)


# base64解码
def base64decode(s):
    return base64.b16decode(s)


#md5编码
def md5(s, charset='utf-8'):
    m5 = hashlib.md5()
    m5.update(s.encode(charset))
    return m5.hexdigest()


je = JSONEncoder()
jd = JSONDecoder()


def json_encode(dic):
    return je.encode(dic)


def json_decode(s):
    return jd.decode(s)
