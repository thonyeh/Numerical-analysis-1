from math import *
M=[]
n=input('ingrese la dimension de la matriz:')
for i in range(n):
    M.append([0]*(n+1))
for i in range(n):
    print'ingrese los %d elementos de la fila %d:'%(n+1,i+1)
    for j in range(n+1):
        M[i][j]=input('')
print "matriz:"
for i in range (n):
	print M[i][0:n]

def escalonada(M,n):
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append([0])
    print "matriz escalonada(ampliada):"
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=i+1
            mayor = M[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=M[i][l]
                M[i][l]=M[p][l]
                M[p][l]=Q[l]  
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
        print M[i]
def solucion(M,n):
    x=[]
    for s in range (n):
        x.append([0])
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        v=0
        for k in range (j+1,n):
            v+= M[j][k]*x[k]
        x[j]=(M[j][n]-v)/M[j][j]
    print x
