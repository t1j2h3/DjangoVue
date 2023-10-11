from datetime import datetime
import base64

timepower = (31536000, 2592000, 86400, 3600, 60, 1)
# secret_KEY = '`k(psi$q^c!@iacytr>?hzx-*#j^+s&)d'

def TimeCal():
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    trans = now.split('-')
    ans = int(0)
    # 计算现在时间值
    for i in range(len(trans)):
        ans += int(trans[i]) * timepower[i]
    return ans

def TimeEncry():
    t = TimeCal()
    # 加密
    stri = str(t)
    code = (base64.b64encode(stri.encode('utf-8')))
    return code.decode('utf-8')

def TimeDecry(code):
    # 解密
    try:
        byt = code.encode('utf-8')
        a = base64.decodebytes(byt)
        ans = a.decode()
        return int(ans)
    except Exception:
        return -10000000


def TimeSub(now, before):
    # 一天86400, 半天43200
    if now-before < 43200 and now-before >= 0:
        return True
    else:
        return False