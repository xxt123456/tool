import numpy as np

def sortNum(n):
    i=1
    while i <=n:
        i +=1
        for x in range(0,n+1-i):
            print(" ",end="")
        for y in range(1,i):
            print(y,end="")
        for z in range(1,i-1):
            print(i-1-z,end="")
        print("")


def rotateNum(n):
    i=0
    j=n-1
    num=1
    myarry=np.zeros((n,n),dtype=np.int16)
    myarry[i][j]=1
    while num<(n*n):
        while (i+1<n and myarry[i+1][j]==0):
            i +=1
            num +=1
            myarry[i][j]=num
        while (j-1>=0 and myarry[i][j-1]==0):
            j -=1
            num +=1
            myarry[i][j]=num
        while (i-1>=0 and myarry[i-1][j]==0):
            i -=1
            num +=1
            myarry[i][j]=num
        while (j+1<n and myarry[i][j+1] ==0):
            j +=1
            num +=1
            myarry[i][j]=num
    print(myarry)

s=rotateNum(4)

