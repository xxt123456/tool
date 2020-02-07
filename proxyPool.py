import urllib.request
import re
import http.client

#服务器的请求只支持HTTP/1.0，urllib3中使用了chunk，但是chunk在HTTP/1.1中才会有，传输还没完成连接就中断了

http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
def checkProxy(html,keyWord):
    #keyWord匹配关键字
    pattern = re.compile(keyWord)
    title=re.findall(pattern,html)
    if title:
        return True
    else:
        return False

def uer_http_proxy(proxy_addr,url):
    #构建代理服务器的handler
    proxyH=urllib.request.ProxyHandler({'http':proxy_addr})
    #由proxyH创建http的opener
    opener=urllib.request.build_opener(proxyH,urllib.request.HTTPHandler)
    #将openerz装载进urllib中
    urllib.request.install_opener(opener)
    #获取信息
    try:
        res=urllib.request.urlopen(url,timeout=5)
        data = res.read().decode('utf-8')
        return data
    except Exception as e:
        return str(e)


if __name__=="__main__":
    proxy_addr="139.9.113.234:8080"
    url='http://www.baidu.com'
    data=uer_http_proxy(proxy_addr,url)
    keyWord = '百度一下'
    resu=checkProxy(data,keyWord)
    print(resu)
