from math import *
#Metodo Doolitle:
M=[]
n=input('ingrese la dimension de la matriz:')


for i in range(n):
    M.append([0]*(n+1))
for i in range(n):
    print'ingrese los %d elementos de la fila %d:'%(n+1,i+1)
    for j in range(n+1):
        M[i][j]=input('')
print "matriz:"
L = []
D = []
LT = []
DLT = []
for i in range(n):
    L.append([0]*(n))
    D.append([0]*(n))
    LT.append([0]*(n))
    DLT.append([0]*(n))
for i in range(n):
    L[i][i]=1
for i in range (n):
	print M[i][0:n]

def LDLT(M,n):
               
    
    for k in range (n):
        suma = 0
        for p in range(k):
            suma = suma + (L[k][p]**2)*D[p][p]
        D[k][k] = M[k][k] - suma
        
        for i in range(k+1,n):
            suma = 0
            for p in range (k):
                suma = suma + M[i][p]*M[k][p]*(D[p][p]**(-1))
            L[i][k] = (M[i][k] - suma)*(D[k][k]**(-1))

    for i in range (n):
        for j in range (n):
            for k in range (n):
                DLT[i][j] = DLT[i][j] + D[i][k]*L[j][k]

    print L
    print D
    print DLT

def solLDLT (M,n):
    x=[]
    for s in range (n):
        x.append([0])
    y=[]
    for s in range (n):
        y.append([0])
        
    y[0]=M[0][n]/L[0][0]
    for j in range (1,n,1):       
        v=0
        for k in range (j):
            v+= L[j][k]*y[k]
        y[j]=(M[j][n]-v)/L[j][j]
    print y
    
    x[n-1]=y[n-1]/DLT[n-1][n-1]
    
    for j in range (n-2,-1,-1):
        v = 0
        for k in range (j+1,n):
            v = v + DLT[j][k] * x[k]
        x[j] = (y[j] - v)*(DLT[j][j]**(-1))
    print 'la solucion es:',(x)
    



    
