import sys
import logging
import random
import time
import socket
from urllib import request
from urllib import error,parse

#创建日志的实例
logger=logging.getLogger('basicSpider')
#定制logger的输出格式
formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#创建日志:日志文件
file_handler=logging.FileHandler('basicSpider.log')
file_handler.setFormatter(formatter)
#创建日志:终端显示
consle_handler=logging.StreamHandler(sys.stdout)
consle_handler.setFormatter(formatter)

#设置默认日志记录级别
logger.setLevel(logging.INFO)

#把日志文件和终端日志添加到日志处理器中
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

# logger.warning('sss')设置日志
minRangeForProxy=1
maxRangeForProxy=10
minSleeptime=1
maxSleeptime=3

def downloadHtml(url,headers=[],proxy={},useProxyRate=6,timeout=socket._GLOBAL_DEFAULT_TIMEOUT,decodeInfo='utf-8',try_num=5):
    html = None
    if random.randint(minRangeForProxy,maxRangeForProxy) > useProxyRate:
        proxy=None #不使用代理

    #创建proxy handler
    proxy_handler=request.ProxyHandler(proxy)
    #创建opener
    opener=request.build_opener(proxy_handler)
    #设置headers
    opener.addheaders=headers
    #把opener安装到urllib库中
    request.install_opener(opener)

    try:
        res=request.urlopen(url,timeout=timeout)
        html=res.read().decode(decodeInfo)
    except UnicodeDecodeError as e:
        logger.error("UnicodeDecodeError %s"%e)
    except error.URLError or error.HTTPError as e:
        logger.error("urllib error %s"%e)
        if try_num>0:
            time.sleep(random.randint(minSleeptime,maxRangeForProxy))
            if hasattr(e,'code') and  500<=e.code <600:
                html=downloadHtml(url,headers,proxy,useProxyRate=6,timeout=timeout,decodeInfo='utf-8',try_num=try_num-1)
    except Exception as e:
        logger.error(e)
    return html


if __name__ == '__main__':
    url = "http://www.wwwqqqq.com/6666.html"
    headers = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/66.0.3359.181 Safari/537.36")]
    proxy = {"http": "182.129.243.84:9000"}
    ss=downloadHtml(url=url,headers=headers)
    print(ss)
logger.removeHandler(file_handler)
logger.removeHandler(consle_handler)
