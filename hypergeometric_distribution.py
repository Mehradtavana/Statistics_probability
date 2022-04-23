# hypergeometric distribution from complete python basic code to use the library
from math import factorial
#all computers 20, #defective 3, #purchase 2
nS , nD, nR = 20, 3, 2

def nCx(n,x):
    return factorial(n) / (factorial(n-x)*factorial(x))

def pmf(S, D, R):
    prob_l = []
    ND = S - D
    for i in range(R+1):
        up = nCx(D,i)*nCx(ND,R-i)
        prob = up / nCx(S,R)
        prob_l.append(prob)
    return prob_l

def Prob(x, S, D, R):
    return pmf(S, D, R)[x]

def E(x, S, D, R):
    moment = 0
    f = pmf(S, D, R)
    for i in range(len(f)):
        moment += i**x*f[i]
    return moment

def var(S, D, R):
    first_moment = E(1, S, D, R)
    second_moment = E(2, S, D, R)
    return second_moment - first_moment**2

print('''Probability of value none defectives: {0},
Probability of value one defective: {1},
Probability of value two defectives: {2},
expected value: {3},
variance: {4}'''.format(Prob(0, nS, nD, nR), Prob(1, nS, nD, nR), Prob(2, nS, nD, nR), 
E(1, nS, nD, nR), var(nS, nD, nR)))

# --------------------------------------------------

from sympy.stats import P, E, variance, FiniteRV

PMF = {}
for i in range(len(pmf(nS, nD, nR))):
    PMF[i] = Prob(i, nS, nD, nR)

X = FiniteRV('X',PMF)
print('''Probability of value none defectives: {0},
Probability of value one defective: {1},
Probability of value two defectives: {2},
expected value: {3},
variance: {4}'''.format(P(X<1), P(X<2)-P(X<1), P(X<=2)-P(X<2), E(X), variance(X)))
# --------------------------------------------------
from math import factorial
#all computers 20, #defective 3, #purchase 2
nS = 20
nD = 3
nR = 2
nND = nS - nD

def nCx(n,x):
    return factorial(n) / (factorial(n-x)*factorial(x))

def pmf_Hyper(S, D, R):
    prob_l = []
    ND = S - D
    for i in range(R+1):
        up = nCx(D,i)*nCx(ND,R-i)
        prob = up / nCx(S,R)
        prob_l.append(prob)
    return prob_l

def Prob_Hyper(x, S, D, R):
    return pmf(S, D, R)[x]

def E_Hyper(S, D, R):
    return R*D/S

def var_Hyper(S, D, R):
    st1 = (S-R)/(S-1)
    st2 = R*D/S
    st3 = 1 - D/S
    return st1*st2*st3

print('''Probability of value none defectives: {0},
Probability of value one defective: {1},
Probability of value two defectives: {2},
expected value: {3},
variance: {4}'''.format(Prob_Hyper(0, nS, nD, nR), Prob_Hyper(1, nS, nD, nR), Prob_Hyper(2, nS, nD, nR), 
E_Hyper(nS, nD, nR), var_Hyper(nS, nD, nR)))

# ----------------------------------------------------------------------------
from sympy.stats import Hypergeometric, P, E, variance
Y = Hypergeometric('Y', nS, nD, nR)
print('''Probability of value none defectives: {0},
Probability of value one defective: {1},
Probability of value two defectives: {2},
expected value: {3},
variance: {4}'''.format(P(Y<1), P(Y<2)-P(Y<1), P(Y<=2)-P(Y<2), E(Y), variance(Y)))