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

import timeit
import matplotlib.pyplot as plt
X=[]
Y=[]
for x in range(3,100,1):
    start = timeit.default_timer()
    solution(x)
    #print(solution(x))
    stop = timeit.default_timer()
    #print('Time: ', stop - start)
    X.append(x)
    Y.append(stop-start)
    plt.title("Measure of Algo Effeciency: Brute Force")
    plt.xlabel("Input Variable")
    plt.ylabel("Machine Runtime")
    plt.plot(X,Y)
    plt.draw()
    plt.pause(0.01)
plt.show()