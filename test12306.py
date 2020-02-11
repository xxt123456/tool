from urllib import request
import ssl

#手动添加受信任ssl
context=ssl._create_unverified_context()

url='https://vpn.surfilter.com:8443/index.html'
ua_headers={
   "User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/66.0.3359.181 Safari/537.36"
}
res=request.Request(url)
response=request.urlopen(res,context=context)
with open('12306.html','wb') as f:
    f.write(response.read())

