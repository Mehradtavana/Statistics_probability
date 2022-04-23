# Pareto graph creation
import matplotlib.pyplot as plt
import numpy as np

def find_range(dataset, low, high):
    import bisect
    l = bisect.bisect_left(dataset, low)
    r = bisect.bisect_right(dataset, high)
    return dataset[l:r]

def Median(arr):
    arr.sort()
    if len(arr)%2==0:
        pos = len(arr)//2
        med = (arr[pos-1]+arr[pos])/2
    else:
        pos = len(arr)//2
        med = arr[pos]
    return med


dataset = [24, 35, 17, 21, 24, 37, 26, 46, 58, 30, 32, 13, 12, 38, 41, 43, 44, 27, 53, 27]
dataset.sort()

# default values
vbin = 5
co_ , medi, c1= [] , [], 0
dataset_range = dataset[-1]-dataset[0]
range_c = dataset_range / vbin
a = dataset[0]
b = range_c + dataset[0]

# create points and ogive values
for i in range(0,vbin):
    if i == vbin-1:
        ran = find_range(dataset, a, b)
        c = len(ran)
        med = Median(ran)
    else:
        ran = find_range(dataset, a, b)
        while ran[-1] == b:
            ran.pop()
        c = len(ran)
        med = Median(ran)
    c1 += c
    co_.append(c1)
    medi.append(med)
    a = b
    b += range_c

hist, bin_edge = np.histogram(dataset, bins=vbin)
fig, ax = plt.subplots()
ax.hist(dataset, bin_edge, cumulative=False)
ax.set_xlabel('Highest temperature')
ax.set_ylabel('Frequency')
ax.set_ylim(0,co_[-1]+1)
ax2 = ax.twinx()
ax2.plot(medi, co_, color='red', marker='D', ms=5)
ax2.set_ylabel('Ogive')
ax2.set_ylim(0,co_[-1]+1)
plt.show()