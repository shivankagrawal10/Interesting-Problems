"""
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(3)
Output:
    1

Input:
Solution.solution(200)
Output:
    487067745

-- Python cases --
Input:
solution.solution(200)
Output:
    487067745

Input:
solution.solution(3)
Output:
    1
"""

'''
#brute force, build up stair case and count ones that work
total=0
def solution(n):
    global total
    total=n
    return count(0,0)
def count(currlev,currtot):
    if(currtot==total and currlev!=currtot):
        return 1
    elif(currtot>total):
        return 0
    x=0
    tempdiff=total-currtot
    for stair in range(currlev+1,tempdiff+1):
        x+=count(stair,currtot+stair)
    return x
'''

"""
# Slight optimization - does not explore unnecessary options
total=0
lim=0
def solution(n):
    global total, lim
    total=n
    
    return count(0,0)
def count(currlev,currtot):
    if(currtot==total and currlev!=currtot):
        return 1
    elif(currtot>total):
        return 0
    x=0
    ret=0
    prevx=x
    tempdiff=total-currtot
    lim=int(tempdiff/2)
    if(lim%2==0):
        lim-=1
    
    for stair in range(currlev+1,tempdiff+1,1):#range(tempdiff,currlev,-1):
        if(stair>lim):
            x+=1
            break
        #print(stair,currtot+stair)
        ret=count(stair,currtot+stair)
        #print(ret)
        prevx=x
        x+=ret

    return x

#print(solution(150))
"""
"""
def solution(n):
    global total, lim
    total=n
    
    return count(0,n)
def count(currlev,currtot):
    '''New Approach - find number of pair sums where val greater than currlev and sum =currtot
    Counts the branches of tree 
    formula for number of children = currtot/2 - currlev (-1 if currtot is even)

    '''
    lim=0
    lim=int(currtot/2)
    if(currtot%2==0):
        lim-=1
    num=lim-currlev
    #print(num)
    if(num<=0):
        return 0
    tempcount=0
    for i in range(num+1):
        stair=currlev+i+1
        temp=currtot-stair
        #print(stair,temp)
        tempcount=count(stair,temp)
        if(tempcount==0):
            break
        num+=tempcount
    return num
#print(solution(10))
"""


import timeit



dictionary={}
total=0
def solution(n):
    global total
    total=n
    #dictionary.clear()
    return count(0,n)

def count(currlev,currtot):
    '''New Approach - find number of pair sums where val greater than currlev and sum =currtot
    Counts the branches of tree 
    formula for number of children = currtot/2 - currlev (-1 if currtot is even)

    '''
    lim=0
    lim=int(currtot/2)
    if(currtot%2==0):
        lim-=1
    num=lim-currlev
    #if((currlev,currtot) in dictionary):
    #    return num 
    dictionary[(currlev,currtot)]=num
    
    if(num<=0):
        dictionary[(currlev,currtot)]=0
        #print(currlev+1,'\nnew stair')
        return 0
    #else:
    #    print(num)
    tempcount=0
    for i in range(num+1):
        stair=currlev+i+1
        temp=currtot-stair
        #print(stair)
        #print(stair,temp)
        
        try:
            tempcount=dictionary[(stair,temp)]
        except:
            tempcount=count(stair,temp)
        
        if(tempcount==0):
            break
        num+=tempcount
    dictionary[(currlev,currtot)]=num #important to update dict in end so that aggregates all branches under not just immediate children
    #print(dictionary)
    #print(num)
    return num




import matplotlib.pyplot as plt
X=[]
Y=[]
for x in range(3,200,1):
    start = timeit.default_timer()
    solution(x)
    #print(solution(x))
    stop = timeit.default_timer()
    #print('Time: ', stop - start)
    X.append(x)
    Y.append(stop-start)
    plt.title("Measure of Algo Effeciency: Subtree Aggregation Optimized")
    plt.xlabel("Input Variable")
    plt.ylabel("Machine Runtime")
    plt.plot(X,Y)
    plt.draw()
    plt.pause(0.01)
plt.show()
