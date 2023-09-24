import time
import numpy as np
import matplotlib.pyplot as plt
def bubblesort(array):
    n=len(array)-1
    while n>1:
        i=0
        while i<n:
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
            i=i+1
        n=n-1
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,10):
        start=time.time()
        a=np.random.randint(1000,size=i*1000)
        bubblesort(a)
        end=time.time()
        times.append(end-start)
        print("bubble sort sorted",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="bubble sort")
plt.grid()
plt.legend()
plt.show()
