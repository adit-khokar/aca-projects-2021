import numpy as np
a=int(input("number of rows in matrix= "))
b=int(input("no. of cols in matrix = "))
m1=np.random.rand(a,b)
m2=np.random.rand(a,b)
ans=m1+m2
print("sumation f the 2 matrix is =\n",ans)