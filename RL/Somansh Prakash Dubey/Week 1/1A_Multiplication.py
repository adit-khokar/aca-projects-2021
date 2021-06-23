import numpy as np
X=[[12,7,3],
[4,5,6],
[7,8,9]]

Y=[[5,8,1],
[6,7,3],
[4,5,9]]

resultm = [[0,0,0],[0,0,0],[0,0,0]]
resulta = [[0,0,0],[0,0,0],[0,0,0]]
resulti = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            resultm[i][j] += X[i][k]*Y[k][j]

result = np.array(resultm)
A=np.array(X)
B=np.array(Y)
C=np.dot(X,Y)

if(C.all() == result.all()):
    print("SAME")
else:
    print("NOT SAME")