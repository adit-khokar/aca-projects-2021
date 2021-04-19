import numpy as np
import time
def det(m):
    if np.shape(m)==(1,1):
        return(m[0][0])
    elif np.shape(m)==(2,2):
        return(m[0][0]*m[1][1]-m[0][1]*m[1][0])
    else:
        [a,b]=np.shape(m)
        d=0
        for i in range(0,a):
            n=np.concatenate((m[0:i],m[i+1:a]),axis=0)
            n=n[:,1:b]
            d=d+((-1)**i)*(m[i,0]*det(n))
        return(d)
        

a=int(input("number of rowsor cols of the desired matrix= "))
t1=time.time()
m=np.random.rand(a,a)
M=np.array(m).astype(float)
print("the choosen matrix is = \n", m)
for i in range(0,a):
    for j in range(0,a):
        n=np.concatenate((m[0:i],m[i+1:a]),axis=0)
        n=np.concatenate((n[:,0:j],n[:,j+1:a]),axis=1)
        M[i][j]=((-1)**(i+j))*det(n)
M=M.T
a=det(m)
inv=M/a
t1=time.time()-t1
print("inverse of the matrix is =\n",inv)
t2=time.time()
invm=np.linalg.inv(m)
t2=time.time()-t2
print("time taken by for loop method =",t1)
print("time taken by np.linalg.inv= ",t2)