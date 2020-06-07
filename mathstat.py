### mathstat.py
import math, functools
import numpy as np


#Функція Лапласа
from scipy.special import erf
norm_erf = lambda arg: erf(arg/math.sqrt(2))/2

calc_sample_mean = lambda data: sum(data)/len(data)

calc_sample_mean_squares =  lambda data: sum(map(lambda x: x*x,data))/len(data)

calc_variance = lambda data: calc_sample_mean_squares(data)-calc_sample_mean(data)**2

correct_variance = lambda var, n: n*var/(n-1)

calc_median = lambda data: (data[len(data)//2]+data[len(data)//2+1])/2 if len(data)%2 else data[(len(data)+1)//2];

# оптимальна кількість розбиттів в гістограмі (Формула Стеджерса)
m_func = lambda n: round(1+ 3.322*math.log10(n))

# ширина інтервалу
h_func = lambda lst: round((max(lst)-min(lst))/m_func(len(lst)))

def histogramData(data, polygon = False):
    data.sort()
    # this is needed for output
    min_el = data[0]
    max_el = data[-1]
    # histogram params
    m = m_func(len(data))
    h = h_func(data)
    # changing input array to just classify for integers
    data = np.array(data)
    data = data-min(data)
    data = data/h
    # make arr->list to simple use on count
    data = np.int64(np.ceil(data)).tolist()
    # create list with ranges frequencies
    sparse_arr = [0]*m
    # (;] arr + first [;] fix
    sparse_arr[0], sparse_arr[-1]=data.count(data[0]), -data.count(data[0])
    for i in data:
        sparse_arr[i-1]+=1
    if polygon == True:
        return dict(zip([i+h/2 for i in range(min_el,max_el+1,h)],sparse_arr))
    dict_keys = ['('+str(i)+';'+str(i+h)+']' for i in range(min_el,max_el+1,h)]
    dict_keys[0]='['+dict_keys[0][1:]
    dict_values = sparse_arr
    out_dict = dict(zip(dict_keys,dict_values))
    return out_dict
