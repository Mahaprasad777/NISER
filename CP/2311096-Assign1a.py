#Name-Mahaprasad Manoranjan Sahoo, Roll No-2311096
#Question 1(Generating 10000 random numbers and plotting them)

import numpy as np
import matplotlib.pyplot as plt

def rng(c,x0,n):
    x=np.zeros(n)  
    x[0]=x0
    for i in range(1,n):
        x[i]=c*x[i-1]*(1-x[i-1]) 
    return x    

x0 = 0.1
n = 10000
cvalue = [1.7,2.3,3.7,4.1,4.5]
kvalue = [5,10,15,20]


for c in cvalue:
    x = rng(c,x0,n)
    print(x)
    for k in kvalue:
        plt.figure()
        plt.scatter(x[:-k],x[k:],s=1)
        plt.xlabel("$x_i$")
        plt.ylabel(f"$x_{{i+{k}}}$")
        plt.title(f"Graph for :c={c},k={k}")
        plt.grid(True)
        plt.show()

#Question 2(LCG)

def lcg(a,c,m,seed,n):
    N=[]
    x=seed
    for i in range(n):
        x= (a*x+c)%m
        N.append(x/m)
    return N
a = 1103515245
c = 12345
m = 32768
seed= 1
k=5

nums = np.array(lcg(a,c,m,seed,n))

plt.scatter(nums[:-k], nums[k:],s=1)
plt.xlabel("$x_i$")
plt.ylabel(f"$x_{{i+{k}}}$")
plt.title("LCG for k=5")
plt.show()

