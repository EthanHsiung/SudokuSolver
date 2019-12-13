# -*- coding:UTF-8 -*-
#!usr/bin/env python
import numpy as np 
def Insert(zero):
    for line in range(9):
        print("请输入第%s行"%(str(line+1)))
        a = input()
        while len(a)!=9:
            print("位数错误！")
            print("请输入第%s行"%(str(line+1)))
            a = input()
        for col in range(9):
            zero[line,col] = a[col]
    return zero
def PossNum(sudu):
    possnum={}
    for i in range(9):
        for j in range(9):
            if sudu[i,j]==0:
                numset1 = set(sudu[i,:])
                numset2 = set(sudu[:,j])
                lblk,cblk=i//3,j//3
                numset3 = set(sudu[lblk*3:lblk*3+3,cblk*3])|set(sudu[lblk*3:lblk*3+3,cblk*3+1])|set(sudu[lblk*3:lblk*3+3,cblk*3+2])
                numpick={0,1,2,3,4,5,6,7,8,9}
                possnum[i,j] =numpick-(numset1|numset2|numset3)
    return possnum            
    
def Trysolve(sudu):
    Steps=[]
    while True:
        #先选出可能值最少的位置（排序）
        possnum = PossNum(sudu)
        if len(possnum)==0:
            break
        sorted_possnum = sorted(possnum.items(),key = lambda x:len(x[1]))
        item = sorted_possnum[0]   #最有可能正确的位置与可能值
        position = item[0]
        pos_value =list(item[1])
        Steps.append((position,pos_value))
        if len(pos_value)!=0:
            sudu[int(position[0]),int(position[1])]=pos_value[0]
        else:     #上一步出错
            Steps.pop()
            for step in range(len(Steps)):
                last_step = Steps.pop()
                position = last_step[0]
                pos_value = last_step[1]
                if len(pos_value)==1:
                    #上一步错误的情况下的唯一解
                    sudu[int(position[0]),int(position[1])]=0
                else:
                    sudu[int(position[0]),int(position[1])]=pos_value[1]
                    Steps.append((position,pos_value[1:]))
                    break
    return sudu
z = np.zeros([9,9])
n = Insert(z)
#n=np.array([[0,2,3,4,5,6,7,8,9],\
# [2,3,4,5,6,7,8,9,1],\
# [3,4,5,6,7,8,9,1,2],\
# [4,5,6,7,8,9,1,2,3],\
# [5,6,7,8,9,1,2,3,4],\
# [6,7,8,9,1,2,3,4,5],\
# [7,8,9,1,2,3,4,5,6],\
# [8,9,1,2,3,4,5,6,7],\
# [9,1,2,3,4,5,6,7,8]])
k=Trysolve(n)
print(k)


