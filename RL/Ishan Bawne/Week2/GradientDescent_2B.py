import numpy as np
import random

class GradientDescent:
    def __init__(self, dimension, data_feat, data_exp, alpha, threshold):
        self.dimension = dimension
        self.data_feat = data_feat
        self.data_exp = data_exp
        self.data_feat = data_feat
        self.data_exp = data_exp
        self.features = [1 for i in range(dimension)]
        self.alpha = alpha
        self.threshold = threshold

    ## This cost method needs to be overridden in subclass of GradientDescent.
    def cost(self,feature):
        return 0


    def derivative_partial(self, independent):
        step = list(self.features)
        #print("Step: {}, Featue: {}".format(step, self.features))
        step[independent] = step[independent] + self.threshold
        #print("step :{}, Features:{} , Cost step :{}, Cost Feature: {} ".format(step,self.features, self.cost(step),self.cost(self.features)))
        derivative = (self.cost(step) - self.cost(self.features))/self.threshold
        #print("Derivative : ", derivative)
        return derivative

    def descent(self, iteration):
        for i in range(iteration):
            newset = []
            for j in range(self.dimension):
                new = self.features[j] - self.alpha * self.derivative_partial(j)
                newset.append(new)
            #print("****************************************************")
            self.features = newset

        return self.features

