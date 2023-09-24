import time
import numpy as np
import matplotlib.pyplot as plt
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,10):
        start=time.time()
        a=np.random.randint(1000,size=i*1000)
        insertionsort(a)
        end=time.time()
        times.append(end-start)
        print("insertion sort sorted",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="insertion sort")
plt.grid()
plt.legend()
plt.show()
