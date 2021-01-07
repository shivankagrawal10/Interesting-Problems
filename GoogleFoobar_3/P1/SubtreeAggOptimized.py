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

import timeit
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