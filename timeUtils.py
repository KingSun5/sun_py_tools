import time
from datetime import datetime

# 时间戳转YY-MM-DD HH:MM:SS
def toFormatTimeStr(secTime):
    timeArray = time.localtime(secTime)
    checkpoint = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return checkpoint


# 输出当前格式化时间 例：2020-06-26
def getNowFormatTime():
    dt01 = datetime.today()
    return dt01.date()
