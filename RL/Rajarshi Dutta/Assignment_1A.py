import  numpy as np
import time
print('Enter 1. Calculate the sum of two different matrices')
print('Enter 2. Calculate the pproduct of two different matrices')
print('Enter 3. Calculate the inverse of a given matrix')
x=int(input('Enter your Choice:  '))

if(x==1):
    n=int(input('Enter the number of rows:  '))
    m=int(input('Enter the number of columns:  '))
    arr1=(np.random.rand(n,m)).tolist()
    arr2=(np.random.rand(n,m)).tolist()
    start1=time.time()
    
    res=[[ 0 for i in range(m)] for i in range(n)] 
    for i in range(n):
        for j in range(m):
           res[i][j]=arr1[i][j] + arr2[i][j]
    for r in res:
        print(r) 
    c1=time.time()-start1
    start1=time.time()
    
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    arr3=np.add(arr1, arr2)
    print(arr3)
    print()
    c2=time.time()-start1
    print('Time taken by lists is {} seconds'.format(c1))
    print('Time taken by numpy arrays is {} seconds'.format(c2))

elif(x==2):
    n1=int(input('Enter the number of rows of first matrix:  '))
    m1=int(input('Enter the number of columns of frist matrix:  '))
    n2=int(input('Enter the number of rows of second matrix:  '))
    m2=int(input('Enter the number of columns of second matrix:  '))
    res=[[0 for i in range(m2)] for i in range(n1)]
    if(m1==n2):
        print('Matrix multiplication is compatible')
        arr1=(np.random.rand(n1,m1)).tolist()
        arr2=(np.random.rand(n2,m2)).tolist()
        start1=time.time()
        print('the product of the two matrices:  ')  
        for i in range(n1):
           sum=0
           for j in range(m2):
               for k in range(n2):
                  res[i][j]=res[i][j]+arr1[i][k]*arr2[k][j]
        for r in res:
            print(r)
        c1=time.time()-start1
        start1=time.time()

        arr1=np.array(arr1)
        arr2=np.array(arr2)
        arr3=np.matmul(arr1,arr2)
        c2=time.time()-start1
        print('Time taken by lists is {} seconds'.format(c1))
        print('Time taken by numpy arrays is {} seconds'.format(c2))
    elif(m1!=n2):
        print('Matrix Multiplication is not compatible')  
else:
    n=int(input('Enter the number of rows:  '))
    mat=np.random.rand(n,n)
    start1=time.time()
    invarr=np.linalg.inv(mat)
    c2=time.time()-start1
    start1=time.time()
    print(invarr)
    
    adj=np.zeros((n,n)).astype(float)
    def determinant(matrix, n):
        sh=np.shape(matrix)
        if(sh==(1,1)):
            return matrix[0][0]
        elif(sh==(2,2)):
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        else:
            matrix=matrix.T
            det=0
            for i in range(0,sh[0]):
                submat=np.concatenate((matrix[0:i],matrix[i+1:n]),axis=0)
                submat=submat[:,1:n]
                det=det+((-1)**i)*matrix[i][0]*determinant(submat,n)
        return det

    for i in range(n):
        for j in range(n):
            submat=np.concatenate((mat[0:i],mat[i+1:n]),axis=0)
            submat=np.concatenate((submat[:,0:j],submat[:,j+1:n]), axis=1)
            adj=(-1)**(i+j)*determinant(submat,n)
    adj=adj.T    
    d=determinant(mat,n)
    mat=mat.tolist()
    c1=time.time()-start1
    print(d)
    print('Time taken by numpy array is {}'.format(c2))
    print('Time taken by list is {}'.format(c1))


