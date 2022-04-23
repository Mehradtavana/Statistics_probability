import pandas as pd
import numpy as np
import psycopg2
import statsmodels.api as sm
import matplotlib.pyplot as plt

# definition of sampling distribution
def sampling(dataset, sample_number, popsamp):
    np.random.seed(1987)
    Mean_sample, propotion_sample, variance_sample = [], [], []
    for _ in range(sample_number):
        sample_data = np.random.choice(a=dataset, size= popsamp)
        sample_propotion = len(sample_data[sample_data >= sample_data.std()])
        propotion_sample.append(sample_propotion/popsamp)
        Mean_sample.append(sample_data.mean())
        variance_sample.append(sample_data.var())
    return Mean_sample, propotion_sample, variance_sample

# connect to data source that exist as docker hub in : https://hub.docker.com/repository/docker/mtavanamehr/postgres
postgresConnection = psycopg2.connect(host='***', port='5432', database="postgres", user="postgres", password="1qazXSW@")
cursor = postgresConnection.cursor()
data = pd.read_sql('select * from Course2_ToolTechniquesforDataScience',postgresConnection)
cursor.close()

# define probability and other needed basic statistical formula
def probability(n, s):
    return len(pd.merge(n, s, how='inner')) / len(s)

def complements(n, s):
    return pd.concat([n,s]).drop_duplicates(keep=False)

def intersect(a, b):
    return pd.merge(a, b, how='inner')

def union(a, b):
    return pd.merge(a, b, how='outer')

def prob_intersect(a, b, s):
    return len(pd.merge(a, b, how='inner')) / len(s)

# according to data, there is alot zero in payment side so we check the one probability that show
# all usages are zero when the payment is zero
n = data[data['payment'] == 0]['serial_number']
n_v = data[data['voice'] == 0]['serial_number']
n_s = data[data['sms'] == 0]['serial_number']
n_d = data[data['data'] == 0]['serial_number']
n_dp = data[data['data_package'] == 0]['serial_number']
s = data['serial_number']
n_vs = union(n_v, n_s)
n_dpd = union(n_dp, n_d)
n_usage_0 = union(n_vs, n_dpd)
n_inter_usage_pay = intersect(n_usage_0, n)
len(n_inter_usage_pay)/len(n) # probability of all usages equal to zero when the payment is zero
# because this probability is more than 95% so for first clearing step remove all zero payment rows
data_nzero_pay = data[data['payment'] != 0]
data_nzero_pay = data_nzero_pay[data_nzero_pay.province_name != 'NaN']

# clustering sampling per province
Province = sorted(data_nzero_pay['province_name'].unique())
first = Province.pop()
sample_size = 5000 

S_Data = data_nzero_pay[data_nzero_pay.province_name == first].sample(n=sample_size)
for i in Province:
    sample_data = data_nzero_pay[data_nzero_pay.province_name == i].sample(n=sample_size)
    S_Data = pd.concat([S_Data,sample_data],axis=0)

# normalization with dividing to mean of data
columns = ['sms','voice','data','data_package','age','payment']
for item in columns:
    S_Data[item] = S_Data[item] / S_Data[item].mean()

# now, we can use the definition for finding each sampling distribution for each column we want
Smean_v, Spropotion_v, Svaraince_v = sampling(S_Data['voice'], 25, 1000)

# check the normality distribution of sample with qqplot
sm.qqplot(Smean_v)
sm.qqplot(Spropotion_v)
sm.qqplot(Svaraince_v)
plt.show()
