# -*- coding: cp1252 -*-
from math import *
#M�todo de Gram Schmidt#
A=[]
m=input('ingrese el numero de filas')
n=input('ingrese el numero de columnas') 
for i in range(m):
    A.append([0]*(n+1))
for i in range(m):
    print'ingrese los %d elementos de la fila %d:'%(n,i+1)
    for j in range(n):
        A[i][j]=input('')
print 'escriba el vector'
for i in range(m):
    A[i][n]=input('')
#GRAM SCHMIDT (vectores columna)"
def GaussSeidel(A,n):
    M=[]
    for s in range (n):
        M.append([0]*(n))
    for i in range(n):
        for j in range(n):
            M[i][j]=A[i][j]
    x=[]
    for s in range (n):
        x.append(0)
    y=[]
    for s in range (n):
        y.append(0)
    b=[]
    for s in range (n):
        b.append(0)
    for i in range(n):
        b[i]=A[i][n]
    sm=1.0
    tol = input('ingrese el TOL que desea usar:')
    print 'los cambios que van haciendo en la solucion del sistema:'
    while sm > tol:
        s1=sm=0
        for i in range(n):
            su=b[i]
            for j in range(0,n):
                su=su-M[i][j]*x[j]
            xi=x[i]+su*(M[i][i]**(-1))
            sm=max(abs(x[i]-xi),sm)
            x[i]=xi
            s1=max(s1,abs(x[i]))
        sm=sm*(s1**(-1))
        print x
    print 'la ultima linea es la soluci�n del sistema'
