from math import *
from Tkinter import *
def main():
    m=input('ingrese el numero de filas:')
    n=input('ingrese el numero de columnas:') 
    A=dema(m,n+1)
    for i in range(m):
        print'ingrese los %d elementos de la fila %d:'%(n,i+1)
        for j in range(n):
            A[i][j]=input('')
    print'ingrese el vector b:'
    for i in range(m):
        A[i][n]=input('')
    menu(A,m,n)
    print ''
def pivo(v,r,p,h):
    if h ==1:
        k=v[p]
        v[p]=v[r]
        v[r]=k
    else:
        Q=[]
        Q=v[p]
        v[p]=v[r]
        v[r]=Q
def dema(m,n):
    M=[]
    if n!=1:
        for i in range(m):
            M.append([0]*(n))
    else:
        for i in range(m):
            M.append(0)
    return M
def adq(A,m,n):
    M=dema(m,n)
    for i in range(m):
        for j in range(n):
            M[i][j]=A[i][j]
    return M
def trans(M,n):
    N=dema(n,n)
    for i in range (n):
        for j in range (n):
            N[i][j]=M[j][i]
    return N
def iden(n):
    I=[]
    for i in range (n):
        I.append([0]*(n))
        I[i][i]=float(1)
    return I
def multip(M1,M2,n):
    M3=dema(n,n)
    for x in range (n):
        for y in range (n):
            suma=0
            for z in range (n):
                suma=suma+M1[x][z]*M2[z][y]
            M3[x][y]=suma
    return M3
def inversa(M,n):
    I=iden(n)
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=max1(M,i)
            pivo(M,p,i,2)
            pivo(I,p,i,2)
        for j in range (0,i):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
    for i in range (n):
        I[i][i]=I[i][i]*(M[i][i])**(-1)
    return I
def sol2(y,U,n,h):
    x=dema(n,1)
    if h==-1:
        for j in range (n-1,-1,-1):
            x[j]=y[j]
            for k in range (j+1,n):
                x[j]-= U[j][k]*x[k]
            x[j]=x[j]*((U[j][j])**(-1))
    else:
        for j in range (n):       
            z[j]=y[j]
            for k in range (j):
                z[j]-= L[j][k]*z[k]
            z[j]=z[j]*(L[j][j]**(-1))
    return x
def solu (M,N,n,h1):
    x=dema(n,1)
    if h1==-1:
        for j in range (n-1,-1,-1):
            x[j]=M[j][n]
            for k in range (j+1,n):
                x[j]-= N[j][k]*x[k]
            x[j]=x[j]*((N[j][j])**(-1))
    else:
        for j in range (n):
            x[j]=M[j][n]
            for k in range (j):
                x[j]-= N[j][k]*x[k]
            x[j]=x[j]*((N[j][j])**(-1))
    return x
def max1(M,i,n):
    mayor = M[i][i]
    p=i
    for j in range(i+1,n):
        if(abs(mayor) < abs(M[j][i])):
            mayor= M[j][i]
            p = j
    return p
def elim(M,i,n,h,k):
    for j in range (h,k):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
def gaussnormal(A,m,n):
    M=adq(A,n,n+1)
    Q=dema(n+1,1)
    mayor=0
    print 'GAUSS SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    print 'La matriz escalonada ampliada es:'
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=max1(M,i,n)
            pivo(M,i,p,2)
        elim(M,i,n,i+1,n)
        print M[i]
    x=solu(M,M,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def gausspp(A,m,n):
    M=adq(A,n,n+1)
    Q=dema(n+1,1)
    mayor=0
    print 'GAUSS CON PIVOTEO PARCIAL'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    print 'La matriz escalonada ampliada es:'
    for i in range (n):
        p=max1(M,i,n)
        pivo(M,i,p,2)
        elim(M,i,n,i+1,n)
        print M[i]
    x=solu(M,M,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def gaussjordan(A,m,n):
    M=adq(A,n,n+1)
    mayor=0
    Q=dema(n+1,1)
    print 'la matriz ampliada es:'
    for i in range(n):
        print M[i]
    print "matriz escalonada(ampliada):"
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=max1(M,i,n)
            pivo(M,i,p,2)
        elim(M,i,n,0,i)
        elim(M,i,n,i+1,n)
    for i in range (n):
        print M[i]
    x=solu(M,M,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def croutLU1normal(A,m,n): #1423
    M=adq(A,n,n+1)
    L=dema(n,n)
    U=iden(n)
    print 'CROUT LU1 SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    p = 0
    for i in range (n):
        for j in range(i,n):
            L[j][i] = M[j][i]
            for p in range (0,i):
                L[j][i]-=L[j][p]*U[p][i]  
        for j in range(i+1,n):
            U[i][j]=M[i][j]
            for p in range (0,i):
                U[i][j]-=L[i][p]*U[p][j]
            U[i][j]=U[i][j]*((L[i][i])**(-1))
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    y=solu(M,L,n,1)
    x=sol2(y,U,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def croutLU1pp(A,m,n):
    p=0
    M=adq(A,n,n+1)
    L=dema(n,n)
    U=iden(n)
    Q=dema(n+1,1)
    print 'CROUT LU1 CON PIVOTEO PARCIAL'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for k in range (n):
        p=max1(M,k,n)
        pivo(M,k,p,2)
        for i in range(k,n):
            L[i][k]=M[i][k]
            for p in range (k):
                L[i][k]-=L[i][p]*U[p][k]
        for i in range(k+1,n):
            U[k][i]=M[k][i]
            for p in range (0,i):
                U[k][i]-=L[k][p]*U[p][i]
            U[k][i]=U[k][i]*((L[k][k])**(-1))
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    y=solu(M,L,n,1)
    x=sol2(y,U,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def croutL1Unormal(A,m,n):
    M=adq(A,n,n+1)
    L=iden(n)
    U=dema(n,n)
    x=dema(n,1)
    y=dema(n,1)
    print 'CROUT L1U SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    suma = 0
    p = 0
    for i in range (n):
        for j in range(i,n):
            suma =0
            for p in range (0,i):
                suma=suma+L[i][p]*U[p][j]
            U[i][j]=M[i][j]-suma  
        for j in range(i+1,n):
            suma=0
            for p in range (0,i):
                suma=suma+L[j][p]*U[p][i]
            L[j][i]=(M[j][i]-suma)*(U[i][i])**(-1)
    print "la matriz L es:"
    for i in range (n):
        print L[i]
    print "La matriz U es:"
    for i in range (n):
        print U[i]
    y=solu(M,L,n,1)
    x=sol2(y,U,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def LDLTnormal(A,m,n):
    M=adq(A,n,n+1)
    L=iden(n)
    D=dema(n,n)
    LT=trans(L,n)
    x=dema(n,1)
    y=dema(n,1)
    print 'METODO LDLt SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
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
    DLT=multip(D,LT,n)
    print 'La matriz L es:'
    for i in range(n):
        print L[i]
    print 'La matriz D es:'
    for i in range(n):
        print D[i]
    y=solu(M,L,n,1)
    x=sol2(y,DLT,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def choleskynormal(A,m,n):
    M=adq(A,n,n+1)
    G=dema(n,n)
    x=dema(n,1)
    y=dema(n,1)
    print 'METODO DE CHOLESKY SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]    
    for k in range (n):
        suma = 0
        for p in range (k):
            suma = suma + (G[k][p])**2
        G[k][k] = sqrt(M[k][k] - suma)
        for i in range(k+1,n):
            suma = 0
            for p in range (k):
                suma = suma + (G[i][p] * G[k][p])
            G[i][k] = (M[i][k] - suma)/G[k][k]
    print 'la matriz G es:'
    for i in range(n):
        print G[i]
    GT=trans(G,n)
    y=solu(M,G,n,1)
    x=sol2(y,GT,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def aasennormal(A,m,n):
    M=adq(n,n+1)
    L=iden(n)
    TLt=dema(n,n)
    T=dema(n,n+1)
    h=dema(n,1)
    l=dema(n,1)
    v=dema(n,1)
    print 'METODO DE AASEN SIN PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    mayor=0
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
    z=solu(M,L,n,1)
    for i in range(n):
        T[i][n]=z[i]
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=max1(T,i,n)
            pivo(T,i,p,2)
        elim(T,i,n,i+1,n)
    W=solu(T,T,n,-1)
    Lt=trans(L,n)
    x=sol2(W,Lt,n,-1)
    print 'la solucion es:'
    print x
    menu(A,m,n)
def aasenpp(A,m,n):
    M=adq(A,n,n+1)
    L=iden(n)
    TLt=dema(n,n)
    T=dema(n,n+1)
    h=dema(n,1)
    l=dema(n,1)
    v=dema(n,1)
    y=dema(n,1)
    x=dema(n,1)
    I=iden(n)
    Q1=[]
    Q=[]
    print 'METODO DE AASEN CON PIVOTEO'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    mayor=0
    for j in range (n):
        P=iden(n)
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
                for k in range (j+1):
                    suma=suma+L[r][k]*h[k]
                v[r]=M[r][j]-suma
            mayor =v[j+1]
            for k in range (j+2,n):
                if mayor < abs(v[k]):
                    p=k
            pivo(v,p,j+1)
            pivo(P,p,j+1)
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
    IT=trans(I,n)
    z=dema(n,1)
    B=dema(n,1)
    for i in range (n):
        for j in range (n):
            B[i]+=I[i][j]*M[j][n]
    z=sol2(B,L,n,1)
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=max1(T,i,n)
            pivo(T,i,p,2)
            pivo(z,i,p,1)
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])
    W=sol2(z,T,n,-1)
    Lt=trans(L,n)
    y=sol2(M,Lt,n,-1)
    for j in range(n):
        for l in range(n):
            x[j]+=IT[l][j]*y[l]
    print 'la solucion del sistema es '
    print x
    menu(A,m,n)
def ParletReid(A,m,n):
    I=iden(n)
    P=iden(n)
    PP=iden(n)
    W=iden(n)
    M=dema(n,n)
    L=iden(n)
    U=dema(n,n+1)
    T=adq(A,n,n+1)
    S=dema(n,n+1)
    G=dema(n,1)
    F=dema(n,1)
    PPT=dema(n,n)
    b=dema(n,1)
    print 'METODO PARLET-REID'
    print " La matriz ampliada es:"
    for i in range(n):
        print T[i]
   #algoritmo#
    for i in range(n-2):
        P=iden(n)
        S=adq(I,n,n)
        #Pivoteo
        p = i+1       
        mayor = abs(T[i+1][i])
        for j in range (i+2,n):    
            if mayor < abs(T[j][i]):
                mayor = abs(T[j][i])
                p = j
        P[i+1] = S[p]
        P[p] = S[i+1]       
    #multiplicacion PAPT#
        pivo(T,p,i+1,2)
        U=adq(T,n,n+1)
        PT=trans(P,n)
        T=multip(U,PT)
    #Gauss#
        for j in range (n):
            G[j]=0
            U.append([0]*(n+1))
        for j in range (i+2,n):
            G[j] = U[j][i]*(U[i+1][i]**(-1))        
    #matriz de gaus#
        for j in range (n):
            for l in range (n):
                M[j][l] = S[j][l] - G[j]*I[i+1][l]       
    #multiplicacion MPAPTMT#
        U=adq(T,n,n+1)
        T=multip(M,U,n)
        U=adq(T,n,n+1)
        MT=trans(M,n)
        T=multip(U,MT,n)
    #EL P TOTAL#
        PP=multip(P,W,n)
        W=adq(PP,n,n)
    #M2P2M1P1#
        L= multip(multip(M,P,n),L,n)
    PPT=trans(PP,n)
    L=multip(L,PPT,n)
    L=inversa(L,n)
    print 'La matriz L es:'
    for i in range (n):
        print L[i]
    print 'La matriz tridiagonal T es:'
    for i in range (n):
        print T[i][0:n]
    print 'La matriz P es:'
    for i in range (n):
        print PP[i]
    z=solu(T,L,n,1)
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=max1(T[i])
            pivo(T,p,i,2)
            pivo(z,p,i,1)
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])
    W=sol2(z,T,n,-1)
    Lt=trans(L,n)
    y=sol2(W,Lt,n,-1)
    x=dema(n,1)
    for j in range(n):
        for l in range(n):
            x[j]+=PPT[j][l]*y[l]
    print 'la solucion del sistema es '
    print x
    menu(A,m,n)
def GS(A,m,n):
    E=dema(m,n)
    U=dema(m,n)
    suma=0
    M=adq(A,n,n+1)
    print 'METODO DE GRAM-SCHIMDT'
    print " La matriz ampliada es:"
    for i in range(n):
        print M[i]
    for j in range(n):
        for k in range(m):
            E[k][j]=M[k][j]
        for i in range(j):
            for k in range(m):
                U[i][j]+= E[k][i]*E[k][j]
            for k in range(m):
                E[k][j]=E[k][j] - U[i][j]*E[k][i]
        suma = 0
        for k in range(m):
            suma +=(E[k][j])**2
        U[j][j] = (suma)**(0.5)
        for k in range(m):
            E[k][j]=E[k][j]*(U[j][j])**(-1)
    print 'La matriz ortogonalizada E por columnas es:'
    for i in range (m):
        print E[i][0:n]
    print 'la matriz U es:'
    print U
    #solucion del sistema Ux=ETb#
    b=dema(n,1)
    for i in range (n):
        for j in range (m):
            b[i]+=E[j][i]*M[j][n]
    x=sol2(b,U,n,-1)
    print 'la solucion del sistema es:'
    print x
    menu(A,m,n)
def Householder(A,m,n):
    M=adq(A,m,n+1)
    print 'METODO DE HOUSEHOLDER'
    print " La matriz ampliada es:"
    for i in range(m):
        print M[i]
    b=dema(m,1)
    for i in range(m):
        b[i]=A[i][n]
    w = [0]*m
    for j in range (n):
        #sacamos maximo de columnas
        MaxCol = M[j][j]
        for k in range(j+1,m):
            MaxCol = max(MaxCol, M[k][j])
        if MaxCol==0:
            break
        psum = 0
        for k in range (j,m):
            psum = psum + M[k][j]*M[k][j]
        ssign = copysign(1,M[j][j])
        sigma = sqrt(psum)*ssign
        for k in range (j,m):
            w[k] = M[k][j]
        w[j] = w[j]+sigma
        betha = 0
        psum = 0
        for k in range(j,m):
            psum = psum+ w[k]*w[k]
        betha = float(2/psum)
        M[j][j] = -sigma
        for l in range(j+1,n):
            s = 0
            for k in range(j,m):
                s = s+w[k]*M[k][l]
            for k in range(j,m):
                M[k][l] = M[k][l]-w[k]*s*betha
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
                M[x][y]=0
    for x in range(n,m):
        for y in range(n):
            M[x][y]=0
    print 'la matriz reducida es:'
    for i in range(m):
        print M[i][0:n]
    #solucion RX=b
    x=sol2(b,M,n,-1)
    print 'la solucion del sistema es:'
    print x
    res = 0
    #suma de residuos al cuadrado
    for k in range(n,m):
        res = res + b[k]*b[k]
    print 'la suma de residuos al cuadrado es:'
    print res
    menu(A,m,n)
def Givens(A,m,n):
    M=adq(A,m,n+1)
    print 'METODO DE GIVENS'
    print " La matriz ampliada es:"
    for i in range(m):
        print M[i]
    b=dema(m,1)
    x=dema(n,1)
    for i in range(m):
        b[i]=A[i][n]
    t=0
    c=0
    s=0
    aux=0
    for i in range(n):
        for k in range(i+1,m):
            #hacer nulo el elemento (k,i)
            if M[k][i]!=0:
                if abs(M[k][i])>= abs(M[i][i]):
                    t=M[i][i]*(M[k][i])**(-1)
                    s=sqrt(1+(t)**2)**(-1)
                    c=s*t
                else:
                    t=M[k][i]*(M[i][i])**(-1)
                    c=sqrt(1+(t)**2)**(-1)
                    s=c*t
                M[i][i]=c*M[i][i]+s*M[k][i]
                for j in range(i+1,n):
                    aux=c*M[i][j]+s*M[k][j]
                    M[k][j]= (-s*M[i][j])+c*M[k][j]
                    M[i][j]=aux
                #transformacion del vector b#
                aux=c*b[i]+s*b[k]
                b[k]= (-s*b[i])+c*b[k]
                b[i]=aux
    #limpiar Matriz A
    print b
    for i in range(n):
        for j in range(n):
            if i>j:
                M[i][j]=0
    for i in range(n,m):
        for j in range(n):
            M[i][j]=0
    print 'la matriz reducida es:'
    for i in range (m):
        print M[i][0:n]
    #solucion#
    print 'el vector b transformado es:'
    print b
    x=sol2(b,M,n,-1)
    print 'la solucion es:' 
    print x
    #residuo al cuadrado#
    res=0
    for k in range(n+1,m):
        res=res+(b[k])**2
    print 'residuos al cuadrado'
    print res
    menu(A,m,n)
def jacobi(A,m,n):
    M=adq(A,n,n)
    x=dema(n,1)
    print 'ingrese el punto inicial'
    for l in range(n):
        x[l]=input('')
    y=dema(n,1)
    b=dema(n,1)
    for i in range(n):
        b[i]=A[i][n]
    sm=1.0
    tol = input('ingrese el TOL que desea usar:')
    print 'los cambios que van haciendo en la solucion del sistema:'
    while sm > tol:
        s1=0
        for i in range(n):
            su=b[i]
            for j in range(0,i):
                su=su-M[i][j]*x[j]
            for j in range (i+1,n):
                su=su-M[i][j]*x[j]
            y[i]=su*(M[i][i]**(-1))
            s1=max(s1,abs(y[i]))
        sm=0
        for i in range(n):
            sm=max(abs(x[i]-y[i])*(s1**(-1)),sm)
            x[i]=y[i]
        print x
    print 'la ultima linea es la solucion del sistema'
    menu(A,m,n)
def GaussSeidel(A,m,n):
    M=adq(A,n,n)
    x=dema(n,1)
    print 'ingrese el punto inicial'
    for l in range(n):
        x[l]=input('')
    y=dema(n,1)
    b=dema(n,1)
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
    print 'la ultima linea es la solucion del sistema'
    menu(A,m,n)
def Ssor(A,m,n):
    M=adq(A,n,n)
    x=dema(n,1)
    print 'ingrese el punto inicial'
    for l in range(n):
        x[l]=input('')
    y=dema(n,1)
    b=dema(n,1)
    w=input('ingrese el parametro w')
    for i in range(n):
        b[i]=A[i][n]
    sm=1.0
    tol = input('ingrese el TOL que desea usar:')
    print 'los cambios que van haciendo en la solucion del sistema:'
    while sm > tol:
        s1=sm=0
        for i in range(n):
            su=b[i]
            for j in range(0,i):
                su=su-M[i][j]*x[j]
            for j in range(i+1,n):
                su=su-M[i][j]*x[j]
            xi=(1-w)*x[i]+w*su*(M[i][i]**(-1))
            sm=max(abs(x[i]-xi),sm)
            x[i]=xi
            s1=max(s1,abs(x[i]))
        sm=sm*(s1**(-1))
        print x
    print 'la ultima linea es la solucion del sistema'
    menu(A,m,n)
def menu(A,m,n):
    print ''
    print 'Seleccione el numero correspondiente al metodo a utilizar:'
    print ''
    print '1. Metodo de Gauss'
    print '2. Metodo de Gauss-Jordan'
    print '3. Metodo de Crout LU1'
    print '4. Metodo de Crout L1U'
    print '5. Factorizacion LDLt'
    print '6. Factorizacion de Cholesky'
    print '7. Metodo de Parlet Reid'
    print '8. Metodo de Aasen'
    print '9. Metodo de Gram-Schmidt'
    print '10. Metodo de Householder'
    print '11. Metodo de Givens'
    print '12. Metodo de Jacobi'
    print '13. Metodo de Gauss-Seidel'
    print '14. Metodo de SSOR'
    print '15. TRABAJAR CON OTRO SISTEMA'
    print '16. SALIR'
    num1=0
    num=input('')
    if num==1:
        num1=sele(num1)
        if num1==1: gaussnormal(A,m,n)
        elif num1==2: gausspp(A,m,n)
    if num==2:
        gaussjordan(A,m,n)
    if num==3:
        num1=sele(num1)
        if num1==1: croutLU1normal(A,m,n)
        elif num1==2: croutLU1pp(A,m,n)
    if num==4:
        croutL1Unormal(A,m,n)
    elif num==5:
        LDLTnormal(A,m,n)
    elif num==6:
        choleskynormal(A,m,n)
    elif num==7:
        ParletReid(A,m,n)
    elif num==8:
        num1=sele(num1)
        if num1==1: aasennormal(A,m,n)
        elif num1==2: aasenpp(A,m,n)
    elif num==9:
        GS(A,m,n)
    elif num==10:
        Householder(A,m,n)
    elif num==11:
        Givens(A,m,n)
    elif num==12:
        jacobi(A,m,n)
    elif num==13:
        GaussSeidel(A,m,n)
    elif num==14:
        Ssor(A,m,n)
    elif num==15:
        main()    
    elif num==16:
        print 'TAREA FINALIZADA'
        pass
def sele(num1):
    print '---Seleccione:'
    print ''
    print '---1. Sin pivoteo'
    print '---2. Con pivoteo parcial'
    num1=input('')
    if num1!=1 and num1!=2:
        print 'ingrese un numero valido:'
        print ''
        sele(num1)
    return num1
main()
