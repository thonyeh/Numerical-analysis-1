from math import *
from Tkinter import *
n = int(raw_input("ingrese el orden de la matriz "))
M=[]
Q=[]
p=0
for i in range (n):
    M.append([0]*(n+1))
for i in range (n):
    Q.append([0]*(n))
for i in range (n):
    print ("Ingrese los elementos de la fila %d")%(i+1)
    for j in range(n+1):
        M[i][j] =input('')
for i in range (n):
    print M[i][0:n]

   
        
def doo(M,n):
    L = []
    U = []
    suma = 0
    p = 0
    for i in range (n):
        L.append([0]*(n))
    for i in range (n):
        U.append([0]*(n))
    for i in range (n):
        L[i][i]=float(1)

        
    for k in range (n):
        for i in range(k+1):
            suma = 0
            for p in range (i):
                suma = suma + L[i][p]*U[p][k]
            U[i][k] = M[i][k] - suma
        for i in range (k,n):
            suma = 0
            for p in range (k):
                suma = suma + L[i][p]*U[p][k]
            L[i][k] = (M[i][k] - suma)/U[k][k]

    print "la matriz L es:"
    for i in range (n):
        print L[i][0:n]
    print "La matriz U es:"
    for i in range (n):
        print U[i][0:n]

    
        
