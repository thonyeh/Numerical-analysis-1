#transformaciones de givens #
from math import *
from Tkinter import *
m = int(raw_input("ingrese el numero de filas de la matriz "))
n = int(raw_input("ingrese el numero de columnas de la matriz "))
A = []
for i in range (m):
    A.append([0]*(n+1))
for i in range(m):
    print'ingrese los %d elementos de la fila %d:'%(n,i+1)
    for j in range(n):
        A[i][j]=input('')
        
print'ingrese el vector b'
for i in range(m):
    A[i][n]=input('')
for i in range (m):
    print A[i][0:n+1]
        
#transformacion de la matriz#
def Givens(A,n):
    b=[]
    x=[]
    for i in range(m):
        b.append(0)
    for i in range(n):
        x.append(0)
    for i in range(m):
        b[i]=A[i][n]
    t=0
    c=0
    s=0
    aux=0
    for i in range(n):
        for k in range(i+1,m):
            #hacer nulo el elemento (k,i)
            if A[k][i]!=0:
                if abs(A[k][i])>= abs(A[i][i]):
                    t=A[i][i]*(A[k][i])**(-1)
                    s=(1+(t)**2)**(-0.5)
                    c=s*t
                else:
                    t=A[k][i]*(A[i][i])**(-1)
                    c=(1+(t)**2)**(-0.5)
                    s=c*t
                A[i][i]=c*A[i][i]+s*A[k][i]
                for j in range(i+1,n):
                    aux=c*A[i][j]+s*A[k][j]
                    A[k][j]= -s*A[i][j]+c*A[k][j]
                    A[i][j]=aux
                #transformacion del vector b#
                aux=c*b[i]+s*b[k]
                b[k]= -s*b[i]+c*b[k]
                b[i]=aux
    print A
    #solucion#
    for j in (n-1,-1,-1):
        suma=0
        for k in range(j+1,n):
            suma = suma + A[j][k]*x[k]
        x[j]=(b[j]-suma)*(A[j][j])**(-1)
    print 'la solucion es:' 
    print x
    #residuo al cuadrado#
    suma=0
    for k in range(n+1,m):
        suma=suma+(b[k])**2
    print 'residuos al cuadrado'
    print suma

    

                    
                    
                    
