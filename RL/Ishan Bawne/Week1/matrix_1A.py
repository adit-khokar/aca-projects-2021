import numpy as np


def Check(result, result_numpy):
    if (result == result_numpy).all():
        print("Both the results are same.\n\n")
    else:
        print("Both the results are different.\n\n")

def Checkbycomp_sq(result, result_numpy, threshold):
    if result_numpy.shape != result.shape:
        return 0

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if abs(result[i,j]-result_numpy[i,j]) > threshold:
                return 0
    
    return 1

class Matrix:
    def __init__(self, rows, coloumns):
        self.rows = rows
        self.coloumns = coloumns
        self.__array__ = [[0 for i in range(coloumns)] for j in range(rows)]

    def set(self, row, coloumn,value):
        self.__array__[row][coloumn] = value
        return value

    def get(self, row, coloumn):
        return self.__array__[row][coloumn]

    def getColoumn(self,coloumn):
        col = []
        for i in range(self.rows):
            col.append(self.get(i,coloumn))
        return col

    def getRow(self, row):
        rows = []
        for i in range(self.coloumns):
            rows.append(self.get(row, i))
        return rows

    def getArray(self):
        return self.__array__

    def setArray(self,array):
        flag = True
        if len(array) == self.rows:
            for i in range(len(array)):
                if len(array[i]) != self.coloumns:
                    flag = False
        else:
            flag = False
        
        if flag :
            self.__array__ = array
        else:
            print("Not a proper array.")

    def Transpose(self):
        res = Matrix(self.coloumns, self.rows)
        for i in range(self.rows):
            for j in range(self.coloumns):
                res.set(j,i,self.get(i,j))
        return res

    def getMinor( self, row, coloumn):
        if self.rows != self.coloumns:
            print("Can't get minor of non square matrix.")
            return Matrix(1,1).set(0,0,0)

        else:
            res = Matrix(self.rows-1, self.coloumns-1)
            r_ind = 0; col_ind = 0
            for i in range(self.rows):
                if i== row:
                    continue
                else:
                    for j in range(self.coloumns):
                        if j == coloumn:
                            continue
                        else:
                            res.set(r_ind, col_ind, self.get(i,j))
                            col_ind+=1
                    r_ind+=1
                    col_ind = 0
            return res
    
    def Determinant(self):
        if self.rows != self.coloumns:
            print("Can't find Determinant of non square matrix.")
            return -1
        else:
            if self.rows == 2:
                return ((self.get(0,0)*self.get(1,1)) - (self.get(0,1)*self.get(1,0)))
            else:
                det = 0
                for i in range(self.coloumns):
                    minor = self.getMinor(0,i)
                    det += self.get(0,i) * minor.Determinant()*((-1)**(i))
                return det


    def Inverse(self):
        det = self.Determinant()
        if self.rows != self.coloumns:
            print("Can't find Inverse of non square matrix.")
            return Matrix(1,1).set(0,0,0)
        elif det == 0:
            print("Singular Matrix can not have inverse.")
            return Matrix(1,1).set(0,0,0)
        else:
            res = Matrix(self.rows, self.coloumns)
            for i in range(self.rows):
                for j in range(self.coloumns):
                    res.set(i,j,((-1)**(i+j)*self.getMinor(i,j).Determinant()/det))
            res = res.Transpose()
            return res


    @staticmethod
    def Multiply(matrixL, matrixR) :
        if matrixL.coloumns != matrixR.rows:
            print("Multiplication not Possible.")
            result = Matrix(1,1)
            result.set(0,0,0)
            return result
        else:
            result = Matrix(matrixL.rows, matrixR.coloumns)
            for i in range(matrixL.rows):
                for j in range(matrixR.coloumns):
                    su = 0
                    ith = matrixL.getRow(i)
                    jth = matrixR.getColoumn(j)
                    for k in range(len(ith)):
                        su += ith[k]*jth[k]
                    result.set(i,j,su)
            return result

    @staticmethod
    def Add(matrix1, matrix2) :
        if (matrix1.rows != matrix2.rows) or (matrix1.coloumns != matrix2.coloumns) :
            print("Addition is not Possible.")
            result = Matrix(1,1)
            result.set(0,0,0)
            return result
        else:
            result = Matrix(matrix1.rows, matrix1.coloumns)
            for i in range(matrix1.rows):
                for j in range(matrix1.coloumns):
                    result.set(i,j,matrix1.get(i,j) + matrix2.get(i,j))
            return result


#____Main____

limit = int(input("Enter Limit : "))

mat_first_row = np.random.randint(1,limit)

mat_common_ind = np.random.randint(1,limit)

mat_second_col = np.random.randint(1,limit)

# Multiplication

matrix1 = Matrix(mat_first_row,mat_common_ind)
matrix2 = Matrix(mat_common_ind,mat_second_col)

for i in range(mat_first_row):
    for j in range(mat_common_ind):
        matrix1.set(i,j,np.random.randint(1,limit))

for i in range(mat_common_ind):
    for j in range(mat_second_col):
        matrix2.set(i,j,np.random.randint(1,limit))

print("------Multiplication------\n")
result = Matrix.Multiply(matrix1,matrix2)
result = np.array(result.getArray())
print("Result by Programmed Method is : \n",result)
result_numpy = np.dot(matrix1.getArray(), matrix2.getArray())
print("Result by Numpy is : \n", result_numpy)
Check(result, result_numpy)


# Addition

matrix1 = Matrix(mat_first_row,mat_common_ind)
matrix2 = Matrix(mat_first_row,mat_common_ind)

for i in range(mat_first_row):
    for j in range(mat_common_ind):
        matrix1.set(i,j,np.random.randint(1,limit))
        matrix2.set(i,j,np.random.randint(1,limit))

print("------Addition------\n")
result = Matrix.Add(matrix1, matrix2)
result = np.array(result.getArray())
print("Result by Programmed Method is : \n",result)
result_numpy = np.array(matrix1.getArray()) + np.array(matrix2.getArray())
print("Result by Numpy is : \n", result_numpy)
Check(result, result_numpy)


# Inverse of Matrix


matrix1 = Matrix(mat_common_ind, mat_common_ind)

for i in range(mat_common_ind):
    for j in range(mat_common_ind):
        matrix1.set(i,j,np.random.randint(1,limit))

print("------Inverse------\n")
inverse = matrix1.Inverse()
inv_np = np.linalg.inv(matrix1.getArray())
print("Result by Programmed Method is : \n",np.array(inverse.getArray()))
print("Result by Numpy is : \n",inv_np)

if(Checkbycomp_sq(np.array(inverse.getArray()), inv_np, 0.0001)):
    print("Both the results are same,\n")
else:
    print("Both the results are not same.\n")
