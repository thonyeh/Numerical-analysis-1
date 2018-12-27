from  math import *
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
#Transformacion de Matriz A, columnas 1 a n
def houseHolder():
        b=[]
        for i in range(m):
            b.append(0)
        for i in range(m):
            b[i]=A[i][n]
        X=[]
        for i in range(n):
            X.append(0)
            
        w = [0]*m
        for j in range (n):
                #sacamos maximo de columnas
                MaxCol = A[j][j]
                for k in range(j+1,m):
                        MaxCol = max(MaxCol, A[k][j])
                if MaxCol==0:
                        return -1
                psum = 0
                for k in range (j,m):
                        psum = psum + A[k][j]*A[k][j]
                ssign = copysign(1,A[j][j])
                sigma = sqrt(psum)*ssign
                for k in range (j,m):
                        w[k] = A[k][j]
                w[j] = w[j]+sigma
                betha = 0
                psum = 0
                for k in range(j,m):
                        psum = psum+ w[k]*w[k]
                betha = float(2/psum)
                A[j][j] = -sigma
                for l in range(j+1,n):
                        s = 0
                        for k in range(j,m):
                                s = s+w[k]*A[k][l]
                        for k in range(j,m):
                                A[k][l] = A[k][l]-w[k]*s*betha
                #Transformar vector B
                s = 0
                for k in range(j,m):
                        s = s+w[k]*b[k]
                for k in range(j,m):
                        b[k] = b[k] - w[k]*s*betha
     
        #limpiar Matriz A
        for x in range(n):
                for y in range(n):
                        if x>y:
                                A[x][y]=0
        for x in range(n,m):
                b[x]=0
                for y in range(n):
                        A[x][y]=0
        print 'la matriz reducida es:'
        for i in range(m):
            print M[0:n]
        #solucion RX=b
        for j in range(n,-1,-1):
            suma=0
            for k in range (j+1,n):
                suma=suma+M[j][k]*x[k]
            x[i]=(b[j]-suma)*(M[j][j]**(-1))
        print 'la solucion del sistema es:'
        print X     
        res = 0
        #suma de residuos al cuadrado
        for k in range(n,m):
                res = res + b[k]*b[k]
        print 'la suma de residuos al cuadrado es:'
        print res
     


