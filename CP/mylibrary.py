import matplotlib.pyplot as plt

class mylib:
    def lcg(self,x,a,c,m):
        l=[x]
        for i in range(10000):
            x=(a*x+c)%m
            l.append(x)
        return l
    def Plot(self,list,k):
        x=list[k:]
        y=list[:-k]
        plt.scatter(x,y)
        plt.title(f"for k = {k}")
        plt.xlabel("$x_i$")
        plt.ylabel(f"$x_(i+{k})$")
        plt.show()
