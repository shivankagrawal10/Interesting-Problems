"""
Queue To Do
===========

You're almost ready to make your move to destroy the LAMBCHOP doomsday device, but the security checkpoints that guard the underlying systems of the LAMBCHOP are going to be a problem. You were able to take one down without tripping any alarms, which is great! Except that as Commander Lambda's assistant, you've learned that the checkpoints are about to come under automated review, which means that your sabotage will be discovered and your cover blown - unless you can trick the automated review system.

To trick the system, you'll need to write a program to return the same security checksum that the guards would have after they would have checked all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the checkpoint guards have found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the guards instead go over everyone in line while noting their security IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time but recording the security IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
0 1 2 /
3 4 / 5
6 / 7 8
where the guards' XOR (^) checksum is 0^1^2^3^4^6 == 2.

Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
17 18 19 20 /
21 22 23 / 24
25 26 / 27 28
29 / 30 31 32
which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.

With this information, write a function solution(start, length) that will cover for the missing security checkpoint by outputting the same checksum the guards would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.
"""
'''
import math
def solution(start,length):
    templen=length
    tempstart=start
    sub=0
    last=0
    check=0
    ans=0
    pow2=0
    while(templen>1):
        #print('new')
        sub=math.floor(tempstart/4)*4
        last=tempstart+templen-1-sub
        pow2=2**(math.floor(math.log(last+sub,2)))==last+sub
        #print(tempstart,sub,sub+last,ans)
        if(tempstart%4>=1):
            lim=min(4,templen+1)+sub
            if(templen<4):
                lim=tempstart+templen
            for temp in range(tempstart,lim):
                #print(temp)
                ans^=temp
        if(templen<4):
            tempstart+=length
            templen-=1
            continue
        #print(ans)
        check=(last)%4
        if(check==0):
            ans^=last+sub
            #if(pow2):
            #    ans^=last+sub
            #else:
            #    ans^=last # only remainder part would be left
        elif(check==1):
            ans^=1    
        elif(check==2):
            if(templen>=4):
                ans^=last+sub+1 # as per rule should be n+1
            else:
                ans^=last+1
            #if(tempstart==sub):
            #    ans^=sub
        else:
            if(templen>=4):
                ans^=0
            else:
                ans^=0+sub #when remainder ==3, the xors cancel, leaving highest multiple of 4
        #print(tempstart,sub,sub+last,ans)
        temp=0
        #for i in range(tempstart,sub+last+1):
        #    print(i,end=", ")
        #    temp^=i
        #print(temp)
        tempstart+=length
        templen-=1
    #print(ans,tempstart)
    ans^=tempstart #scenario where only one number left
    return ans

#print(solution(0,3))#2
#print(solution(0,6))
print(solution(17,4))#14
'''
'''
import math
def solution(start,length):
    templen=length
    tempstart=start
    sub=0
    last=0
    check=0
    ans=0
    
    while(templen>1):
        sub=int(tempstart/4)*4
        last=tempstart+templen-1-sub
        if(sub==0 and last>=4):
            for temp in range(tempstart,4):
                ans^=temp
        check=(last)%4
        if(check==0):
            ans^=last
        elif(check==1):
            ans^=1
        elif(check==2):
            ans^=last+1#+sub
        else:
            ans^=0+sub #when remainder ==3, the xors cancel, leaving highest multiple of 4
        #print(check,sub,last,ans)
        tempstart+=length
        templen-=1
    #print(ans,tempstart)
    ans^=tempstart #scenario where only one number left
    return ans
'''

"""
import math
def solution(start,length):
    templen=length
    tempstart=start
    sub=0
    last=0
    check=0
    ans=0
    pow2=0
    while(templen>0):
        sub=math.floor(tempstart/4)*4
        last=tempstart+templen-1-sub
        #pow2=2**(math.floor(math.log(last+sub,2)))==last+sub
        if(tempstart%4>=1 or tempstart==0):
            lim=min(4,templen+1)+sub
            if(templen<4):
                lim=tempstart+templen
            for temp in range(tempstart,lim):
                #print(temp)
                ans^=temp
        #print(tempstart,sub,sub+last,ans,templen)
        if(templen<4):
            tempstart+=length
            templen-=1
            continue
        check=(last)%4
        if(check==0):
            ans^=last+sub
        elif(check==1):
            ans^=1    
        elif(check==2):
            if(templen>=4):
                ans^=last+sub+1 # as per rule should be n+1
            else:
                ans^=last+1
        else:
            if(templen>=4):
                ans^=0
            else:
                ans^=0+sub #when remainder ==3, the xors cancel, leaving highest multiple of 4
        #print(tempstart,sub,sub+last,ans,templen)
        tempstart+=length
        templen-=1
    #ans^=tempstart #scenario where only one number left
    return ans
"""
"""
import math
def getxor(start,len,ans):
    if(len==0):
        return ans
    sub=0
    last=0
    check=0
    #ans=0
    pow2=0
    sub=long(math.floor(start/4)*4)
    last=start+len-1-sub
    #pow2=2**(math.floor(math.log(last+sub,2)))#==last+sub
    check=(last)%4
    if(check==0):
        ans^=last+sub
    elif(check==1):
        ans^=1    
    elif(check==2):
        #print("check",math.floor((last+sub)/4)*4+3)
        ans^=long(math.floor((last+sub)/4)*4+3)
    else:
        ans^=0
    #print(ans)
    return ans^getxor(sub,start-sub,0)

def solution(start,length):
    templen=length
    tempstart=start
    ans=0
    while(templen>0):
        ans=getxor(tempstart,templen,ans)
        #print(tempstart,templen,ans)
        tempstart+=length
        templen-=1
    return ans
"""

import math
'''
Final Solution
O(n) algo where n is the number of rows created
this approach uses the mod 4 rules for xor and 
reduces number of xor operations from O(length^2)
to 1 (sometimes 2) per row
'''
def getxor(start,len,ans):
    if(len==0):
        return ans
    sub=0
    last=0
    check=0
    sub=long(math.floor(start/4)*4)
    last=start+len-1-sub
    check=(last)%4
    if(check==0):
        ans^=last+sub
    elif(check==1):
        ans^=1    
    elif(check==2):
        ans^=long(math.floor((last+sub)/4)*4+3)
    else:
        ans^=0
    return ans^getxor(sub,start-sub,0)
    #Second getxor is to adjust the calculated row 
    #based on how far number starts from multiple of 4

def solution(start,length):
    templen=length
    tempstart=start
    ans=0
    while(templen>0):
        ans=getxor(tempstart,templen,ans)
        tempstart+=length
        templen-=1
    return ans
#solution(17,4)
print(solution(0,3))
#print(solution(17,4))
#print(solution(0,6))
'''
import matplotlib.pyplot as plt
import timeit
X=[]
Y=[]
for x in range(1,2*10**7,100):
    start = timeit.default_timer()
    solution(0,x)
    #print(solution(x))
    stop = timeit.default_timer()
    #print('Time: ', stop - start)
    X.append(x)
    Y.append(stop-start)
    plt.plot(X,Y)
    plt.draw()
    plt.pause(0.01)
plt.show()
'''