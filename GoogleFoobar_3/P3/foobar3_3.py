'''
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.
'''
"""
import math
def solution(m,f):
    gm=long(float(m))
    gf=long(float(f))
    ans=maketree(gm,gf)-1
    if(ans<0):
        return 'impossible'
    return str(ans)
def maketree(m,f):
    if(m<1 or f<1):
        return 0
    if(m==1 and f ==1):
        return 1
    val=0
    val=maketree(m-f,f)
    if(val>=1):
        return val+1
    val=maketree(m,f-m)
    if(val>=1):
        return val+1
    return val
"""
"""
#import math
dict={}
def solution(m,f):
    gm=long(float(m))
    gf=long(float(f))
    try:
        ans=dict[(gm,gf)]
    except:
        ans=maketree(gm,gf)
        dict[(gm,gf)]=ans
    #ans-=1
    #print(ans)
    if(ans<=0):
        return 'impossible'
    return str(ans)
'''
#recursive and dictionary use
def maketree(m,f):
    if(m<1 or f<1):
        return 0
    if(m==1 and f ==1):
        return 1
    val=0
    try:
        val=dict[(m,f)]
    except:
        val=maketree(m-f,f)
        if(val>=1):
            dict[(m,f)]=val+1
            return val+1
        val=maketree(m,f-m)
        if(val>=1):
            dict[(m,f)]=val+1
            return val+1
    return val
'''
def maketree(m,f):
    list=[]
    val=0
    while(m>=1 and f>=1):
        #print(m,f)
        if(m==1 and f==1):
            val+=1
            break
        elif(m>=1 and f>=1):
            val+=1
        elif(m<1 or f<1):
            m,f=list.pop()
            continue
        try:
            val+=dict[(m,f)]-1
            break
        except:
            if(m-f>=1):
                list.append((m-f,f))
            if(f-m>=1):
                list.append((m,f-m))
        if not list:
            val=0
            break
        m,f=list.pop()
    return val
"""
'''
#loop way
def maketree(m,f):
    nextcoord=[]
    val=0
    while(m>=1 and f>=1):
        #print(m,f)
        if(m==1 and f==1):
            val+=1
            break
        elif(m>1 and f>1):
            val+=1
        elif(m==1 or f==1):
            val+=max(m,f)
            pairtocycles[(m,f)]=val
            break
        elif(m<1 or f<1):
            m,f=nextcoord.pop()
            continue
        try:
            val+=pairtocycles[(m,f)]-1
            break
        except:
            if(m-f>=1):
                nextcoord.append((m-f,f))
            if(f-m>=1):
                nextcoord.append((m,f-m))
        if not nextcoord:
            val=0
            break
        m,f=nextcoord.pop()
    return val
'''

pairtocycles={}
def solution(m,f):
    gm=long(m)
    gf=long(f)
    try:
        ans=pairtocycles[(gm,gf)]
    except:
        ans=maketree(gm,gf)
        pairtocycles[(gm,gf)]=ans
    ans-=1
    #print(pairtocycles)
    if(ans<0):
        return 'impossible'
    return str(ans)

def maketree(m,f):
    if(m<1 or f<1):
        return 0
    if(m==1 and f ==1):
        return 1
    val=0
    try:
        val=pairtocycles[(m,f)]
    except:
        factor=0
        if(m>f):
            factor=m/f
            if(m%f==0):
                factor-=1
            val=maketree(m-factor*f,f)
            if(val>=1):
                pairtocycles[(m,f)]=factor+val
                return pairtocycles[(m,f)]
        elif(m==f):
            return 0
        else:    
            factor=f/m
            if(f%m==0):
                factor-=1
            val=maketree(m,f-factor*m)
            if(val>=1):
                pairtocycles[(m,f)]=factor+val
                return pairtocycles[(m,f)]
    return val

'''
print(solution("4","7"))
print(solution("2","1"))
print(solution("2","4"))
for x in range(10):
    print(solution("1",str(x)))
'''
import matplotlib.pyplot as plt
import timeit
X=[]
Y=[]
x=1
bound=10**4
interval=10**1
while x<bound:
    start = timeit.default_timer()
    solution("1",str(x))
    #print(solution(x))
    stop = timeit.default_timer()
    print(solution("1",str(x)))
    x+=interval
    #print('Time: ', stop - start)
    X.append(x)
    Y.append(stop-start)
    plt.plot(X,Y)
    plt.draw()
    plt.pause(0.01)
plt.show()
