# -*- coding: cp1252 -*-
from math import *
#Método de Gram Schmidt#
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
def GS(A,n):
    E=[]
    U=[]
    suma=0
    for i in range(m):
        E.append([0]*(n))
        U.append([0]*(n))
    
    for j in range(n):
        for k in range(m):
            E[k][j]=A[k][j]
        for i in range(j):
            suma = 0
            for k in range(m):
                suma = suma + E[k][i]*E[k][j]
            U[i][j] = suma
            for k in range(m):
                E[k][j]=E[k][j] - U[i][j]*E[k][i]
                    
        suma = 0
        for k in range(m):
            suma = suma + (E[k][j])**2
        U[j][j] = (suma)**(0.5)
        
        for k in range(m):
            E[k][j]=E[k][j]*(U[j][j])**(-1)
    print 'La matriz tranformada es:'
    for i in range (m):
        print E[i][0:n]
    print U
#solucion del sistema Ux=ETb#
    for i in range (n):
        suma=0
        for j in range (m):
            suma=suma+E[j][i]*A[j][n]
        A[i][n]=suma
    x=[]
    for s in range (n):
        x.append(0)
    x[n-1]=A[n-1][n]/U[n-1][n-1]
    for j in range (n-2,-1,-1):
        v=0
        for k in range (j+1,n):
            v+= U[j][k]*x[k]
        x[j]=(A[j][n]-v)/U[j][j]
    print 'la solucion del sistema es:'
    print x
            
            
            
        
    
    
    
