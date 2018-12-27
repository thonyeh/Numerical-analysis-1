from math import *
A=[]
n=input('ingrese la dimension de la matriz:')
for i in range(n):
    A.append([0]*(n+1))
for i in range(n):
    print'ingrese los %d elementos de la fila %d:'%(n,i+1)
    for j in range(n):
        A[i][j]=input('')
print'ingrese el vector b'
for i in range(n):
    A[i][n]=input('')
def multip(M1,M2,n):
    M3=[]
    for l1 in range (n):
        M3.append([0]*(n))

    for x in range (n):
        for y in range (n):
            suma=0
            for z in range (n):
                suma=suma+M1[x][z]*M2[z][y]
            M3[x][y]=suma
    return M3

def aasensp():
    M = []
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    T = []
    h = []
    l = []
    v = []
    Lt = []
    TLt = []
    print 'METODO DE AASEN SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))
        Lt.append([0]*(n))
        TLt.append([0]*(n))
    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    for j in range (n):
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
        if j <(n-1):
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]*(v[j+1]**(-1))
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    z=[]
    for i in range (n):
        z.append(0)
    z[0]=M[0][n]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(M[j][n]-suma)*(L[j][j]**(-1))
    for i in range(n):
        T[i][n]=z[i]
    p=0
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            for l in range (i,n+1):
                Q[l]=T[i][l]
                T[i][l]=T[p][l]
                T[p][l]=Q[l]  
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=T[n-1][n]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(T[j][n]-suma)/T[j][j]
    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    x=[]
    for i in range (n):
        x.append(0)
    x[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*x[k]
        x[j]=(W[j]-suma)*(Lt[j][j]**(-1))
    print 'la solucion es:'
    print x
def aasenpp():
    M = []
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n+1):
            M[i][j]=A[i][j]
    L = []
    T = []
    h = []
    l = []
    v = []
    Lt = []
    TLt = []
    print 'METODO DE AASEN CON PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for i in range (n):
        L.append([0]*(n))
        T.append([0]*(n+1))
        Lt.append([0]*(n))
        TLt.append([0]*(n))
    for i in range (n):
        h.append(0)
        v.append(0)
        l.append(0)
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Q1=[]
    for s in range (n):
        Q.append(0)
    for i in range (n):
        L[i][i]=1
    I=[]
    for i in range (n):
        I.append([0]*(n))
    for i in range (n):
        I[i][i]=1
    for j in range (n):
        P=[]
        for k in range (n):
            P.append([0]*(n))
        for k in range (n):
            P[k][k]=1
        if j==0:
            h[0]=M[0][0]
        else:
            if j==1:
                h[0]=T[1][0]
                h[1]=M[1][1]
            else:
                l[0]=0
                for k in range (1,j):
                    l[k]=L[j][k]
                l[j]=1
                h[j]=M[j][j]
                h[0]=T[0][0]*l[0]+T[1][0]*l[1]
                h[j]=h[j]-l[0]*h[0]
                for k in range (1,j):
                    h[k]= T[k][k-1]*l[k-1]+T[k][k]*l[k]+T[k+1][k]*l[k+1]
                    h[j]=h[j]-l[k]*h[k]
        if j==0 or j==1:
            T[j][j]=h[j]
        else:
            T[j][j]=h[j]-T[j][j-1]*L[j][j-1]
            
        if j <(n-1):
            p=j+1
            for r in range (j+1,n):
                suma=0
                for k in range (0,j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            mayor =v[j+1]
            for k in range (j+2,n):
                if mayor < abs(v[k]):
                    p=k
            q=v[p]
            v[p]=v[j+1]
            v[j+1]=q
            Q1=P[p]
            P[p]=P[j+1]
            P[j+1]=Q1
            for k in range (2,j+1):
                q=L[j+1][k]
                L[j+1][k]=L[p][k]
                L[p][k]=q

            for k in range (j+1,n):
                q=M[j+1][k]
                M[j+1][k]=M[p][k]
                M[p][k]=q
            for k in range (j+1,n):
                q=M[k][j+1]
                M[k][j+1]=M[k][p]
                M[k][p]=q
            T[j+1][j]=T[j][j+1]=v[j+1]
        if j<(n-2):
            for k in range (j+2,n):
                L[k][j+1]=v[k]
            if v[j+1]!=0:
                for k in range (j+2,n):
                    L[k][j+1]=L[k][j+1]*(v[j+1]**(-1))
            print 'L:',L
        I=multip(P,I,n)
    print "la matriz L es:"
    for i in range (n):
        print L[i][0:n]
    print "La matriz T es:"
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print I[i]
    IT=[]
    for i in range (n):
        IT.append([0]*(n))
    for i in range (n):
        for j in range (n):
            IT[i][j]=I[j][i]
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Lt=[]
    for s in range (n):
        Lt.append([0]*n)    
    z=[]
    for i in range (n):
        z.append(0)
    B=[]
    for i in range(n):
        B.append(0)
    for i in range (n):
        suma=0
        for j in range (n):
            suma=suma+I[i][j]*M[j][n]
        B[i]=suma
    z[0]=B[0]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(B[j]-suma)*(L[j][j]**(-1))
    
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            
            Q=T[i]
            T[i]=T[p]
            T[p]=Q
            k=z[i]
            z[i]=z[p]
            z[p]=k
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])


    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=z[n-1]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(z[j]-suma)/T[j][j]

    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    y=[]
    for i in range (n):
        y.append(0)
    y[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*y[k]
        y[j]=(W[j]-suma)*(Lt[j][j]**(-1))

    x=[]
    for i in range (n):
        x.append(0)
    for j in range(n):
        suma = 0
        for l in range(n):
            suma=suma+IT[l][j]*y[l]
        x[j]=suma
    print 'la solucion del sistema es '
    print x
