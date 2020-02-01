import os
import hashlib
from multiprocessing import Pool
from multiprocessing import Manager
#通过hash判断文件是否copy完整
CHUCKSIZE=265
def hashFile(fileName):
    h=hashlib.sha256()
    with open(fileName,'rb') as f:
        while True:
            chuck=f.read(CHUCKSIZE)
            if not chuck:
                break
            h.update(chuck)
    return h.hexdigest()
#复制文件
def copyFile(fileName,srcPath,destPath,q):
    srcFileName=srcPath + '/'+ fileName
    destFileName=destPath + '/'+ fileName
    with open(srcFileName,'rb') as fs:
        with open(destFileName,'wb') as fb:
            for i in fs:
                fb.write(i)
    #向进程池队列中加入当前完成的文件名
    q.put(fileName)
    return True
#判断目录是否存在
def copyFile_exit(fileName,srcPath,destPath,q):
    if not os.path.exists(srcPath):
        print('该%s路径下无对应文件'%srcPath)
        return None

    if not os.path.exists(destPath):
        try:
            os.mkdir(destPath)
        except Exception as e:
            print('%s创建失败'%destPath)
            return None
    return copyFile(fileName,srcPath,destPath,q)


if __name__== "__main__":
    srcPath=input('请输入需要copy的目录')
    try:
        if os.path.exists(srcPath):
            allFileName = os.listdir(srcPath)
        destsrcPath=srcPath+'-副本'
        # 判断目的目录是否已存在，如果存在，则进行第二次命名
        while os.path.isdir(destsrcPath):
            destsrcPath = destsrcPath + '-副本'
        fileNum=len(allFileName)
        #copy 文件数
        num=0
        #创建进程池
        pool=Pool(processes=3)
        #进程池通信队列
        q=Manager().Queue()

        for i in allFileName:
            pool.apply_async(func=copyFile_exit ,args=(i,srcPath,destsrcPath,q))
        pool.close()
        while num < fileNum:
            fileName=q.get() #如果get不到，会阻塞
            num +=1
            rate= num/fileNum *100
            scrFileName=srcPath+'/'+fileName
            destFileName=destsrcPath+'/'+fileName
            if (hashFile(scrFileName) == hashFile(destFileName)):
                print('%s copy OK'%scrFileName)
            else:
                print('%s copy Failed'%scrFileName)
            print('当前进度%1.f%%'%rate)
        pool.join()
        print('复制完成')
    except Exception as e :
        print('该%s路径下无对应文件'%srcPath)


