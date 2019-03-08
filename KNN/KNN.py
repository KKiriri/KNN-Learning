import numpy as np
import pandas as pd
import math
import operator
from __future__ import division

#This is the Euclidean function to calculate distance
def Euclidean(x1, y1, lenght):
    distance = 0
    for i in range(lenght):
        distance += np.square(x1[i]-y1[i])
    return np.sqrt(distance)

#This is the Manhattan function to calculate distance    
def Manhattan(x1, y1, lenght):
    distance = 0
    for i in range(lenght):
        distance += abs(x1[i]-y1[i])
    return distance

#This is the Minkowski function to calculate distance
#Not understand this function, please see https://en.wikipedia.org/wiki/Minkowski_distance    
def Minkowski(x1, y1, lenght, p):
    distance = 0
    for i in range(lenght):
        distance += abs(x1[i]-y1[i])**p
    return distance**(1/p)