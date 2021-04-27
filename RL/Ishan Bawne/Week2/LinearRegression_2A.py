import numpy as np
import GradientDescent_2B as gd
import csv
import matplotlib.pyplot as plt


class LinearRegression(gd.GradientDescent):

    def __init__(self, dimension, data_feat, data_exp, alpha, threshold):
        super().__init__(dimension, data_feat, data_exp, alpha, threshold)
        if self.dimension != len(data_feat[0]):
            raise Exception("Invalid data set.")

    ## Overridden cost function from superclass.
    def cost(self,feature):
        cos = 0

        for i in range(len(self.data_feat)):
            s = 0
            for j in range(len(self.data_feat[i])):
                s += feature[j]*self.data_feat[i][j]
            diff = s - self.data_exp[i]
            diff = diff*diff
            cos += diff

        cos = cos/(2*len(self.data_feat))
        return cos



    def predict(self,feature):
        if len(feature) != len(self.features):
            raise Exception("Unappropriate data.")

        s = 0
        for i in range(len(feature)):
            s+= self.features[i]*feature[i]

        return s


## __Main__

data_feat = []      #Training data set
data_exp = []       #Training expected values

test_feat = []      #Testing dataset
test_exp = []       #Testing Expected values



with open('data.csv') as data:
    csv_reader = csv.reader(data, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
            line_count += 1
        else:
            if line_count < 8000:
                data_feat.append([1, int(row[0])/52, int(row[1])/37937, int(row[2])/5471, int(row[3])/35682, int(row[4])/5189, float(row[5])/15.0001])
                data_exp.append(float(row[6])/500001)
                line_count+=1
            else:
                test_feat.append([1, int(row[0])/52, int(row[1])/37937, int(row[2])/5471, int(row[3])/35682, int(row[4])/5189, float(row[5])/15.0001])
                test_exp.append(float(row[6])/500001)
                line_count+=1



demo = LinearRegression(7,data_feat,data_exp,1,0.01)
n = int(input("Enter number of Iterations (For fast results enter 100) : "))
x = np.arange(0,n,10)
y = []
for i in range(len(x)):
    demo.descent(10)
    y.append(demo.cost(demo.features))

plt.plot(x,y)
plt.ylabel("Cost Function")
plt.xlabel("Number of Iteration")
plt.show()          #To display Variation of Cost function with number of iterations

predicted = demo.predict([1,23,1106,252,790,230,1.8523])*500001

print("Predicted value for featureset {} is : {}".format([1,23,1106,252,790,230,1.8523],predicted))