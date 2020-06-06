import math, functools
from collections import Counter

sample_mean = lambda data: sum(data)/len(data)

sample_mean_squares =  lambda data: sum(map(lambda x: x*x,data))/len(data)

variance = lambda data: sample_mean_squares(data)-sample_mean(data)**2

corrected_variance = lambda data: len(data)*variance(data)/(len(data)-1)

median = lambda data: (data[len(data)//2]+data[len(data)//2+1])/2 if len(data)%2 else data[(len(data)+1)//2];

