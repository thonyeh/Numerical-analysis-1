from math import *
from Tkinter import *
m = int(raw_input("ingrese el numero de filas de la matriz "))
n = int(raw_input("ingrese el numero de columnas de la matriz "))
M = []
for i in range (m):
    M.append([0]*(n+1))
for i in range(m):
    print'ingrese los %d elementos de la fila %d:'%(n,i+1)
    for j in range(n):
        M[i][j]=input('')
        
print'ingrese el vector b'
for i in range(m):
    M[i][n]=input('')
for i in range (m):
    print M[i][0:n+1]
        
b=[]
for i in range(m):
    b.append(0)
for i in range(m):
    b[i]=M[i][n]
sigma=0
beta=0
w=[]
d=[]
for i in range (m):
    w.append(0)
def Householder():
    for j in range (n):
        mayor = abs(M[j][j])
        for k in range (j+1,m):
            if mayor < abs(M[k][j]):
                mayor = abs(M[k][j])
        if mayor == 0:
            break
        sigma = 0
        suma=0
        for k in range(j,m):
            suma=suma+(M[k][j]**(2))
        sigma=sqrt(suma)
        if M[j][j]<0:
            sigma=sigma*(-1)
        for k in range(j,m):
            w[k]=M[k][j]
        w[j]=w[j]+sigma
        suma=0
        for k in range(j,m):
            suma=suma+w[k]**(2)
        beta=2*(suma)**(-1)
        M[j][j]=-sigma
        
        for l in range (j+1,n):
            s=0
            for k in range(j,m):
                s=s+w[k]*M[k][l]
            for k in range (j,m):
                M[k][l]=M[k][l]-w[k]*s*beta

        #transformacion del vector b
        s=0
        for k in range(j,m):
            s=s+w[k]*b[k]
        for k in range (j,m):
            b[k]=b[k]-w[k]*s*beta
    print M
    #resolucion del sistema Rx=b
