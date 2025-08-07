# NAME- Mahaprasad Manoranjan Sahoo, Roll No - 2311096
# sum of first 20 odd numbers

N=20
sum=0
print("The first 20 odd numbers are - ")
for i in range(N):
  sum1=2*i+1
  print(sum1)
  sum+=2*i+1

print("Sum of first 20 odd numbers =", sum)

# factorial of N = 8

N=8
f=1
for i in range(1,N+1):
  f=f*i
print("The factorial of 8 is - ", f)

'''
RESULT - 

The first 20 odd numbers are - 
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
Sum of first 20 odd numbers = 400
The factorial of 8 is -  40320'''

# NAME- Mahaprasad Manoranjan Sahoo, Roll No - 2311096
# Calculate the sum of N = 15 terms of a GP and HP series for common difference 1.5 and common ratio 0.5 starting from t0 = 1.25.

N=15
d=1.5
r=0.5
t0=1.25 
sum=0

print('The 15 terms of GP are - ')
for i in range(N):
  gp=t0*(r**i)
  print(gp)
  sum += gp

print("The sum of first 15 terms of GP is - ",sum)

print("   ")

sum1=0
print("The 15 terms of HP are - ")
for i in range(N):
  ap=t0+i*d
  hp=1/ap
  print(hp)
  sum1 += hp

print("The sum of first 15 terms of HP is - ",sum1)

'''
RESULT - 

The 15 terms of GP are - 
1.25
0.625
0.3125
0.15625
0.078125
0.0390625
0.01953125
0.009765625
0.0048828125
0.00244140625
0.001220703125
0.0006103515625
0.00030517578125
0.000152587890625
7.62939453125e-05
The sum of first 15 terms of GP is -  2.4999237060546875
   
The 15 terms of HP are - 
0.8
0.36363636363636365
0.23529411764705882
0.17391304347826086
0.13793103448275862
0.11428571428571428
0.0975609756097561
0.0851063829787234
0.07547169811320754
0.06779661016949153
0.06153846153846154
0.056338028169014086
0.05194805194805195
0.04819277108433735
0.0449438202247191
The sum of first 15 terms of HP is -  2.4139570733659186'''

# NAME- Mahaprasad Manoranjan Sahoo, Roll No - 2311096
# Matrix product

def read_matrix(filename):
  with open(filename,'r') as f:
    matrix = []
    for line in f:
      row = [float(num) for num in line.strip().split()]
      matrix.append(row)
  return matrix

a = read_matrix('asgn0_matA')
print("MATRIX A = ",a)
b = read_matrix('asgn0_matB')
print("MATRIX B = ",b)
c = read_matrix('asgn0_vecC')
print("MATRIX C = ",c)
d = read_matrix('asgn0_vecD')
print("MATRIX D = ",d)

#AB

AB = []
for i in range(len(a)):
    row=[]
    for j in range(len(b[0])):
        s=0
        for k in range(len(b)):
            s+=a[i][k]*b[k][j]
        row.append(s)
    AB.append(row)
print("AB =",AB)

# DOT PRODUCT OF D.C
s=0
for i in range(len(d)):
    s += d[i][0] * c[i][0]
print("DOT product of D and C = ", s)

#BC

BC=[]
for i in range(len(b)):
    row=[]
    for j in range(len(c[0])):
        s=0
        for k in range(len(c)):
            s+=b[i][k]*c[k][j]
        row.append(s)
    BC.append(row)
print('BC = ', BC)


'''
RESULT - 

MATRIX A =  [[2.0, -3.0, 1.4], [2.5, 1.0, -2.0], [-0.8, 0.0, 3.1]]
MATRIX B =  [[0.0, -1.0, 1.0], [1.5, 0.5, -2.0], [3.0, 0.0, -2.0]]
MATRIX C =  [[-2.0], [0.5], [1.5]]
MATRIX D =  [[1.0], [0.0], [-1.0]]
AB = [[-0.3000000000000007, -3.5, 5.2], [-4.5, -2.0, 4.5], [9.3, 0.8, -7.0]]
DOT product of D and C =  -3.5
BC =  [[1.0], [-5.75], [-9.0]]
'''

