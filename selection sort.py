import time
import numpy as np
import matplotlib.pyplot as plt
def selectionsort(array):
    i=0
    while i<len(array):
        j=i
        k=i+1
        while k<len(array):
            if array[k]<array[j]:
                j=k
            k=k+1
        array[i],array[j]=array[j],array[i]
        i=i+1
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel('list length')
plt.ylabel('time complexity')
times=list()
for i in range(1,10):
        start=time.time()
        a=np.random.randint(1000,size=i*1000)
        selectionsort(a)
        end=time.time()
        times.append(end-start)
        print("selection sort sorted",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="selection sort")
plt.grid()
plt.legend()
plt.show()
