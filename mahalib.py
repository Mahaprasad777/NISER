#Name-Mahaprasad Manoranjan Sahoo, Roll No- 2311096
#Mahalib

import matplotlib.pyplot as plt

class mylib:

    def mat_mul(self, A,B):
        AB = []
        for i in range(len(A)):
            row=[]
            for j in range(len(B[0])):
                s=0
                for k in range(len(B)):
                    s+=A[i][k]*B[k][j]
                row.append(s)
            AB.append(row)
        print("LU =",AB)


    def read_matrix(self, filename):
        with open(filename,'r') as f:
            matrix=[]
            for line in f:
                row=[float(num) for num in line.strip().split()]
                matrix.append(row)
        return matrix

    def lcg(self, x, a, c, m):
        l=[x]
        for i in range(10000):
            x=(a*x+c)%m
            l.append(x)
        return l

    def lcg1(self, x, a, c, m):
        l=[x]
        for i in range(10000):
            x=(a*x+c)%m
            l.append(x/m)
        return l

    def Plot(self, list, k):
        x=list[k:]
        y=list[:-k]
        plt.scatter(x,y)
        plt.title(f"for k = {k}")
        plt.xlabel("$x_i$")
        plt.ylabel(f"$x_(i+{k})$")
        plt.show()


    def augmented_1(self,A, b):

        augmented = []
        for i in range(len(A)):
            row = A[i][:]      
            row.append(b[i])    
            augmented.append(row)
        return augmented


    def print_matrix(self, Mat):
        for row in Mat:
            print(row)
        print()


    def gj(self, A, b):

        n = len(A)
        aug = self.augmented_1(A, b)

        print("Augmented Matrix:")
        self.print_matrix(aug)

        for i in range(n):
            # Pivoting
            if aug[i][i] == 0:
                for k in range(i+1, n):
                    if aug[k][i] != 0:
                        aug[i], aug[k] = aug[k], aug[i]
                        break

            # Make pivot = 1
            p = aug[i][i]
            if p != 0:
                for j in range(len(aug[i])):
                    aug[i][j] = aug[i][j] / p

            # Eliminating all other entries in column i
            for k in range(n):
                if k != i:
                    ratio = aug[k][i]
                    if ratio != 0:
                        for j in range(len(aug[k])):
                            aug[k][j]=aug[k][j] - ratio*aug[i][j]


        print("Final RREF:")
        self.print_matrix(aug)

        # Extract solution
        sol = [aug[i][-1] for i in range(n)]
        print("Solution:")
        for idx, val in enumerate(sol):
            print(f"x{idx+1} = {val}")

        return sol

    def lu_decomposition(self, A):
        n = len(A)
        L = [[0.0]* n for i in range(n)] #creating empty matrix L of same Dimension of A
        U = [[0.0]* n for i in range(n)] #creating empty matrix U of same Dimension of A

        for i in range(n):
            for j in range(i, n):
                U[i][j] = A[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]

            for j in range(i, n):
                if i == j:
                    L[i][i] = 1
                else:
                    L[j][i] = A[j][i]
                    for k in range(i):
                        L[j][i] -= L[j][k] * U[k][i]
                    L[j][i] /= U[i][i]

        print("L matrix:")
        self.print_matrix(L)
        print("U matrix:")
        self.print_matrix(U)
        # Compute the product of L and U using mat_mul
        LU = self.mat_mul(L, U)
        return L, U

    def forward_sub(self, L, b):
        n = len(b)
        y = [0.0 for a in range(n)]
        for i in range(n):
            total = 0.0
            for j in range(i):
                total = total + L[i][j] * y[j]
            y[i] = b[i] - total
        return y
    def backward_sub(self, U, y):
        n = len(y)
        x = [0.0 for a in range(n)]
        for i in range(n-1, -1, -1):  # go backwards
            total = 0.0
            for j in range(i+1, n):
                total = total + U[i][j] * x[j]
            x[i] = (y[i] - total) / U[i][i]
        return x

    def solve_LU(self, A, b):
        L, U = self.lu_decomposition(A)
        y = self.forward_sub(L, b)
        x = self.backward_sub(U, y)
        return x

    def cholesky_decom(self,A):
        n = len(A)
        L = [[0.0 for _ in range(n)] for _ in range(n)] # Creating Empty Matrix
        for i in range(n):
            for j in range(i + 1):
                s = A[i][j]
                for k in range(j):
                    s -= L[i][k] * L[j][k]
                if i == j:
                    if s <= 0:
                        raise ValueError("Matrix error")
                    L[i][j] = (s ** 0.5)
                else:
                    L[i][j] = s / L[j][j]
        return L

    def cholesky_sol(self,L, b):
        n = len(L)
        y = [0.0 for _ in range(n)]
        for i in range(n):
            s = b[i]
            for j in range(i):
                s -= L[i][j] * y[j]
            y[i] = s / L[i][i]
        x = [0.0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s = y[i]
            for j in range(i + 1, n):
                s -= L[j][i] * x[j]
            x[i] = s / L[i][i]
        return x

    def jacobi_sol(self,A, b, tol=1e-6, max_iteration=9999):
        n = len(A)
        x_old = [0.0]*n
        x_new = [0.0]*n

        for it in range(max_iteration):
            for i in range(n):
                s = sum(A[i][j]*x_old[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - s) / A[i][i]
            
            # check convergence
            if max(abs(x_new[i]-x_old[i]) for i in range(n)) < tol:
                return x_new, it+1
            
            x_old = x_new[:]
        
        raise ValueError("Jacobi did not converge Within max iteration")

