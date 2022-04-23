from scipy import stats
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

dataset = pd.read_csv("input.csv")
dataset.describe()
arr = np.array(dataset)
c , n = arr.shape
print('counts of rows: {0}\ncounts of columns: {1}'.format(c,n))
# pure python calculation of covariance and
l1 , l2 = list(arr[:,0]), list(arr[:,1])
l1_mean, l2_mean = sum(l1)/c, sum(l2)/c

l1_var_s = sum((item-l1_mean)**2 for item in l1) / (c-1)
l2_var_s = sum((item-l2_mean)**2 for item in l2) / (c-1)

l1_std, l2_std = l1_var_s ** 0.5, l2_var_s ** 0.5

l1l2_cov_s = sum((l1[i]-l1_mean)*(l2[i]-l2_mean) for i in range(0,c))/c
l1l2_cor = l1l2_cov_s / (l1_std*l2_std)
print('''first column mean: {0}\nsecond column mean: {1}\nfirst column variance of sample: {2}
second column variance of sample: {3}\nstd of first column: {4}\nstd of second column: {5}\ncovariance_sample: {6}
correlative: {7}'''.format(l1_mean, l2_mean, l1_var_s, l2_var_s, l1_std, l2_std, l1l2_cov_s, l1l2_cor))
# Numpy
np_cov_s = np.cov(l1,l2)[0][1]
np_cor = np.corrcoef(l1,l2)[0][1]
# Pandas
pandas_corr = dataset.corr()['Height']['Weight']
# Scipy
scipy_cor = stats.pearsonr(l1,l2)[0]
print('Numpy library output,\ncovariance: {0}\ncorrelative: {1}'.format(np_cov_s, np_cor))
print('Pandas library output,\ncorrelative: {0}\nScipy library output, correlative: {1}'.format(pandas_corr, scipy_cor))


# heatmap of Numpy
sn.heatmap(np.cov(l1,l2), annot=True, fmt='g')
sn.heatmap(np.corrcoef(l1,l2), annot=True, fmt='g')

# heatmap of pandas
sn.heatmap(dataset.corr(), annot=True, fmt='g')