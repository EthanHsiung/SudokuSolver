# -*- coding:UTF-8 -*-
#!usr/bin/env python
import numpy as np 
import time

def nine(data):
    nine_blocks = np.zeros([3,3,3,3], dtype = int)
    for i in range(3):
        for j in range(3):
            nine_blocks[i,j] = data[3*i:3*(i+1),3*j:3*(j+1)]
    return nine_blocks

def numSet(data,nine_blocks):
    numPickSet = {}
    for i in range(9):
        for j in range(9):
            if data[i,j] == 0:
                impossibleNum = set(data[i,:])|set(data[:,j])|set(nine_blocks[i//3,j//3].ravel())
                numPickSet[str(i)+str(j)] = set(np.array(range(10))) - impossibleNum
    return numPickSet               #dictionary

def TryInsert(data):
    time1 = time.time()
    insertStep = []
    while True:

        numPickSet = numSet(data,nine(data))
        if len(numPickSet) == 0:
            break
        pickSort = sorted(numPickSet.items(),key = lambda x:len(x[1]))
        itemMin = pickSort[0]
        position = itemMin[0]
        value = list(itemMin[1])
        insertStep.append((position,value))
        if len(value) != 0:
            data[int(position[0]),int(position[1])] = value[0]
        else:
            insertStep.pop()
            for x in range(len(insertStep)):
                backstep = insertStep.pop()
                position = backstep[0]
                insertNumSet = backstep[1]
                if len(insertNumSet) == 1:
                    data[int(position[0]),int(position[1])] = 0
                else:
                    data[int(position[0]),int(position[1])] = insertNumSet[1]
                    insertStep.append((position, insertNumSet[1:]))
                    break
        time2 = time.time()

    print("Finished!\nUsing time:%f s"%(time2-time1))
    print(data)

data = np.array([[0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0]])
for i in range(9):
    rowNum = input("PLEASE ENTER YOUR NUMBER--LINE%s\n"%(i+1))
    rowNum = rowNum.split()
    while len(rowNum) != 9:
        print("WRONG!PLEASE ENTER AGAIN!")
        rowNum = input("PLEASE ENTER YOUR NUMBER--LINE%s\n"%(i+1))
        rowNum = rowNum.split()
    data[i]=rowNum
print(data)
TryInsert(data)



