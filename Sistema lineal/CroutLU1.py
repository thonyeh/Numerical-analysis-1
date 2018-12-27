from math import *
from Tkinter import *
n = int(raw_input("ingrese el orden de la matriz "))
M=[]
L = []
U = []
for i in range (n):
    L.append([0]*(n))
    U.append([0]*(n))
for i in range (n):
    M.append([0]*(n+1))
for i in range (n):
    print ("Ingrese los elementos de la fila %d")%(i+1)
    for j in range(n+1):
        M[i][j] =input('')
for i in range (n):
    print M[i][0:n]
    
def croutLU1(M,n):
      
    suma = 0
    p = 0
    for i in range (n):
        for j in range (n):
            L[i][j]=0
            U[i][j]=0
    for i in range (n):
        U[i][i]=float(1)

    for i in range (n):
        for j in range(i,n):
            suma =0
            for p in range (0,i):
                suma = suma + L[j][p]*U[p][i]
            L[j][i] = M[j][i] - suma  
        for j in range(i+1,n):
            suma=0
            for p in range (0,i):
                suma = suma + L[i][p]*U[p][j]
            U[i][j]=(M[i][j] - suma)*(L[i][i])**(-1)
    print "la matriz L es:"
    for i in range (n):
        print L[i][0:n]
    print "La matriz U es:"
    for i in range (n):
        print U[i][0:n]
def solcroutLU1(M,n):
    x=[]
    for s in range (n):
        x.append([0])
    y=[]
    for s in range (n):
        y.append([0])
        
    y[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n,1):       
        v=0
        for k in range (j):
            v+= L[j][k]*y[k]
        y[j]=(M[j][n]-v)*(L[j][j]**(-1))
    print M
    print y
    
    x[n-1]=y[n-1]/U[n-1][n-1]
    
    for j in range (n-2,-1,-1):
        v=0
        for k in range (j+1,n):
            v+= U[j][k]*x[k]
        x[j]=(y[j]-v)*(U[j][j]**(-1))
    print 'la solucion es: %d', x
    


        
