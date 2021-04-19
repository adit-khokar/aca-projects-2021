import numpy as np
import time as tm
i1=int(input("number of rows, you desire in the matrix 1="))
j1=int(input("Similarly, number of cols in matrix 1= "))
j2=int(input("number of cols for matrix 2="))
a=np.random.rand(i1,j1)
b=np.random.rand(j1,j2)
c=np.zeros((i1,j2))
c=np.array(c).astype(float)
print("random matrix A= \n",a,"\nRandom matrix B= \n",b)
print("A*B, using for loops= ")
t11=tm.time()
for q in range(0,i1):
    for e in range(0,j2):
        for w in range(0,j1):
            c[q][e]=c[q][e]+a[q][w]*b[w][e]
t10=tm.time()
t1=t10-t11
print(c)
print("A*B using np.dot =")
t21=tm.time()
d=np.dot(a,b)
t20=tm.time()
t2=t20-t21
print(d)
print("time taken for for loops= ",t1,"\ntime taken for np.dot",t2)
    
