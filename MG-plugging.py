from  twisted.web.client import getPage,defer
from  twisted.internet import reactor

num = 0
a = 0
b = 0
def stop_loop(arg):
    print('总执行次数%s,放行总次数%s,封堵失败总次数%s,封堵成功总次数%s'%(i,a,num,b))
    reactor.stop()

def get_response(contents,url):
    if url in pass_list:
        global a
        a +=1
        print('放行总次数%s,%s'%(a,url))
    else:
        global num
        num +=1
        print('封堵失败总次数%s'%(num),url)
def errorHandler(failure,url):
    global b
    b +=1
    print('封堵成功%s'%(url),failure)


deferred_list=[]

###封堵列表#####
url_list=[
    'http://www.baidu.com/',
    'https://www.cnblogs.com/',
    'https://www.cnblogs.com/news/',
    'https://cn.bing.com/',
    'https://stackoverflow.com/',
]

###放行列表#####
pass_list=[
    'http://www.baidu.com/',
]

i=0
while i<10:
    for url in url_list:
        deferred=getPage(bytes(url,encoding='utf-8'))
        deferred.addCallback(get_response,url)
        deferred.addErrback(errorHandler,url)
        deferred_list.append(deferred)
        i +=1

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(stop_loop)
reactor.run()
