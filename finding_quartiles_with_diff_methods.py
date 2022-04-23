# different method for finding quartiles are defined base on https://en.wikipedia.org/wiki/Quartile#Discrete_distributions
import numpy as np
import pandas as pd
arr = [73, 35, 76, 6, 72, 53, 45, 12, 33, 29, 60]
arr.sort()

print('Q1 quantile of arr: {0}\nMedian of arr: {1}\nQ3 quantile of arr: {2}'
.format(np.quantile(arr, .25), np.quantile(arr, .50), np.quantile(arr, .75)))

print('Q1 quantile of arr: {0}\nMedian of arr: {1}\nQ3 quantile of arr: {2}'
.format(np.percentile(arr, 25), np.percentile(arr, 50), np.percentile(arr, 75)))

def Median(arr):
    arr.sort()
    if len(arr)%2==0:
        pos = len(arr)//2
        med = (arr[pos-1]+arr[pos])/2
    else:
        pos = len(arr)//2
        med = arr[pos]
    return med

def method1(arr):
    MED = Median(arr)
    if len(arr)%2==0:
        pos = len(arr)/2
        arr1, arr2 = arr[:pos], arr[pos:]
        Q1, Q3 = Median(arr1), Median(arr2)
    else:
        pos = len(arr)//2
        arr1, arr2 = arr[:pos], arr[pos+1:]
        Q1, Q3 = Median(arr1), Median(arr2)
    return 'Q1: {0}, Median: {1}, Q3: {2}'.format(Q1, MED, Q3)

def method2(arr):
    MED = Median(arr)
    if len(arr)%2==0:
        pos = len(arr)/2
        arr1, arr2 = arr[:pos], arr[pos:]
        Q1, Q3 = Median(arr1), Median(arr2)
    else:
        pos = len(arr)//2
        arr1, arr2 = arr[:pos+1], arr[pos:]
        Q1, Q3 = Median(arr1), Median(arr2)
    return 'Q1: {0}, Median: {1}, Q3: {2}'.format(Q1, MED, Q3)

def method3(arr, include_median='N'):
    if len(arr)%2==0 and include_median=='N':
        MED = Median(arr)
        pos = len(arr)//2
        arr1, arr2 = arr[:pos], arr[pos:]
        Q1, Q3 = Median(arr1), Median(arr2)
    elif len(arr)%2==0 and include_median=='Y':
        MED1 = Median(arr)
        arr.append(MED1)
        arr.sort()
        Q1, MED, Q3 = method2(arr)
    elif len(arr)%2!=0:
        MED = Median(arr)
        n = (len(arr)-1)/4
        m = (len(arr)-3)/4
        if n.is_integer():
            pos = int(n - 1)
            pos3 = int(3*n -1)
            Q1 = arr[pos]/4 + arr[pos+1]*3/4
            Q3 = arr[pos3+1]*3/4 + arr[pos3+2]/4
        elif m.is_integer():
            pos = int(m - 1)
            pos3 = int(3*m - 1)
            Q1 = arr[pos+1]*3/4 + arr[pos+2]/4
            Q3 = arr[pos3+2]/4 + arr[pos3+3]*3/4
    return 'Q1: {0}, Median: {1}, Q3: {2}'.format(Q1, MED, Q3)

def method4(arr):
    n = (len(arr)+1) / 4
    MED = Median(arr)
    if n.is_integer():
        pos1, pos3 = int(n-1), int(3*n-1)
        Q1 = arr[pos1]
        Q3 = arr[pos3]
    else:
        m = (len(arr)+1) % 4
        n = (len(arr)+1) // 4
        pos = int(n)
        Q1 = ((arr[pos]*m)+(arr[pos+1]*(1-m)))/2
        Q3 = ((arr[3*pos]*m)+(arr[3*pos+1]*(1-m)))/2
    return 'Q1: {0}, Median: {1}, Q3: {2}'.format(Q1, MED, Q3)

print('Method1,\n   {0}\nMethod2,\n   {1}\nMethod3,\n   {2}\nMethod4,\n   {3}'
.format(method1(arr), method2(arr), method3(arr), method4(arr)))