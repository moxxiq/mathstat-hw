import math, functools
from collections import Counter

calc_sample_mean = lambda data: sum(data)/len(data)

calc_sample_mean_squares =  lambda data: sum(map(lambda x: x*x,data))/len(data)

calc_variance = lambda data: calc_sample_mean_squares(data)-calc_sample_mean(data)**2

correct_variance = lambda var, n: n*var/(n-1)

calc_median = lambda data: (data[len(data)//2]+data[len(data)//2+1])/2 if len(data)%2 else data[(len(data)+1)//2];

