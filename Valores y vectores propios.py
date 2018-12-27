from math import *
from Tkinter import *
from numpy import *
def main():
    print 'APROXIMACION NUMERICA DE VALORES Y VECTORES PROPIOS'
    print ''
    print 'Ingrese los datos de la matriz A:'
    print ''
    n=input('n-Dimension de la matriz:') 
    A=dema(n,n)
    con=0
    for i in range(n):
        print'ingrese los %d elementos de la fila %d:'%(n,i+1)
        for j in range(n):
            A[i][j]=input('')
    menu(A,n)
def menu(A,n):
    print 'Con que metodo desea trabajar?'
    print 'Seleccione una opcion:'
    print ''
    print '1. Metodo de la potencia'
    print '2. Metodo de la potencia inversa'
    print '3. Metodo de la potencia inversa con desplazamiento'
    print '4. Metodo de biseccion o de Givens'
    print '5. Metodo de Jacobi'
    print '6. Metodo de factorizacion Q R'
    print '7. REINICIAR'
    print '8. SALIR'
    r=input('')
    if r==1:
        Poten(A,n)
    elif r==2:
        PotenInv(A,n)
    elif r==3:
        PotenInvDesp(A,n)
    elif r==4:
        autovBisec(A,n)
    elif r==5:
        autovJac(A,n)
    elif r==6:
        autovQR(A,n)
    elif r==7:
        main()
    elif r==8:
        pass
    else:
        print 'Ingrese una opcion valida'
        menu(A,n)
def Poten(A,n):
    print 'Determine un vector inicial, x0.'
    print ''
    x0=dema(n,1)
    w=dema(n,1)
    print 'Ingrese los elementos del vector inicial:'
    for i in range(n):
        x0[i]=float(input(''))
    print ''
    #Normalizando x0
    p=0
    a=x0[0]
    for i in range(1,n):
        if abs(a)<abs(x0[i]):
            a=x0[i]
            p = i
    for i in range(n):
        w[i]=x0[i]/x0[p]
    #Iteraciones
    k=input('Indique con cuantas iteraciones desea que se realize el proceso:')
    print ''
    m=1
    while m<=k:
        print 'iteracion:',m
        m+=1
        for i in range(n):
            s=0
            for j in range(n):
                s+=A[i][j]*w[j]
            x0[i]=s
        sigma=x0[p]/w[p]
        a=x0[0]
        p=0
        for i in range(1,n):
            if abs(a)<abs(x0[i]):
                a=x0[i]
                p = i
        for i in range(n):
            w[i]=x0[i]/x0[p]
        print 'autovector:',w
        print 'autovalor:',sigma
        print ''
    print 'Aproximacion del valor propio dominante:'
    print sigma
    print 'Autovalor asociado a dicho valor propio:'
    print w
    print ''
    menu(A,n)
def PotenInv(A,n):
    det=linalg.det(A)
    if det==0:
        print 'La matriz es singular'
        print 'No se puede aplicar este metodo'
        print ''
        menu(A,n)
    else:
        M=linalg.inv(A)
        print 'Determine un vector inicial, x0.'
        print ''
        x0=dema(n,1)
        w=dema(n,1)
        print 'Ingrese los elementos del vector inicial:'
        for i in range(n):
            x0[i]=float(input(''))
        print ''
        #Normalizando x0
        p=0
        a=x0[0]
        for i in range(1,n):
            if abs(a)<abs(x0[i]):
                a=x0[i]
                p = i
        for i in range(n):
            w[i]=x0[i]/x0[p]
        #Iteraciones
        k=input('Indique con cuantas iteraciones desea que se realize el proceso:')
        print ''
        m=1
        while m<=k:
            print 'iteracion:',m
            m+=1
            for i in range(n):
                s=0
                for j in range(n):
                    s+=M[i][j]*w[j]
                x0[i]=s
            sigma=x0[p]/w[p]
            a=x0[0]
            p=0
            for i in range(1,n):
                if abs(a)<abs(x0[i]):
                    a=x0[i]
                    p = i
            for i in range(n):
                w[i]=x0[i]/x0[p]
            print 'autovector:',w
            print 'autovalor:',sigma**(-1)
            print ''
        print 'Aproximacion del menor valor propio:'
        print sigma**(-1)
        print 'Autovalor asociado a dicho valor propio:'
        print w
        print ''
        menu(A,n)
def PotenInvDesp(A,n):
    print 'Determine "q" una aproximacion de un autovalor de la matriz A'
    q=input('')
    print ''
    det=linalg.det(A)
    A2=adq(A,n,n)
    for i in range(n):
        A2[i][i]=A[i][i]-q
    det1=linalg.det(A2)
    if det==0:
        print 'La matriz A es singular'
        print 'No se puede aplicar este metodo'
        print ''
        menu(A,n)
    elif det1==0:
        print 'La matriz (A-qI) es singular'
        print 'No se puede aplicar este metodo'
        print ''
        menu(A,n)
    else:
        M=linalg.inv(A2)
        print 'Determine un vector inicial, x0.'
        print ''
        x0=dema(n,1)
        w=dema(n,1)
        print 'Ingrese los elementos del vector inicial:'
        for i in range(n):
            x0[i]=float(input(''))
        print ''
        #Normalizando x0
        p=0
        a=x0[0]
        for i in range(1,n):
            if abs(a)<abs(x0[i]):
                a=x0[i]
                p = i
        for i in range(n):
            w[i]=x0[i]/x0[p]
        #Iteraciones
        k=input('Indique con cuantas iteraciones desea que se realize el proceso:')
        print ''
        m=1
        while m<=k:
            print 'iteracion:',m
            m+=1
            for i in range(n):
                s=0
                for j in range(n):
                    s+=M[i][j]*w[j]
                x0[i]=s
            sigma=x0[p]/w[p]
            a=x0[0]
            p=0
            for i in range(1,n):
                if abs(a)<abs(x0[i]):
                    a=x0[i]
                    p = i
            for i in range(n):
                w[i]=x0[i]/x0[p]
            print 'autovector:',w
            sigma=q+sigma**(-1)
            print 'autovalor:',sigma
            print ''
        print 'Aproximacion del menor valor propio:'
        print sigma
        print 'Autovalor asociado a dicho valor propio:'
        print w
        print ''
        menu(A,n)
def autovBisec(A,n):
    print 'Aplicar Givens a la matriz para tridiagonalizar?'
    print '1. Aplicar GIVENS'
    print '2. Ya esta tridiagonalizada'
    g=input ('')
    print ''
    if g==1:
        E=Givens(A,n,n)
        print 'La matriz tridiagonalizada por GIVENS es:'
        for i in range(n):
            print E[i]
    else:
        E=dema(n,n)
        for i in range(n):
            for j in range(n):
                E[i][j]=A[i][j]
    print 'Ingrese un intervalo [a,b]'
    a=input('a=')
    b=input('b=')
    print ''
    M=dema(n+1,1)
    N=dema(n+1,1)
    for i in range(n+1):
        M[i]=polin(E,n,a,i)
        N[i]=polin(E,n,b,i)
    p1=0
    p2=0
    for i  in range(1,n+1):
        if sign(M[i-1])!=sign(M[i]):
            p1+=1
        if sign(N[i-1])!=sign(N[i]):
            p2+=1
    if p1==0 and p2==n:
        print 'Todos los valores propios estan en [a,b].'
        print ''
        tol=input('Ingrese el tol con el que desea aproximar un autovalor:')
        print ''
        while abs(a-b)>tol:
            c=(a+b)*2**(-1)
            M=dema(n+1,1)
            N=dema(n+1,1)
            R=dema(n+1,1)
            for i in range(n+1):
                M[i]=polin(E,n,a,i)
                N[i]=polin(E,n,c,i)
                R[i]=polin(E,n,b,i)
            p1=0
            p2=0
            p3=0
            for i  in range(1,n+1):
                if sign(M[i-1])!=sign(M[i]):
                    p1+=1
                if sign(N[i-1])!=sign(N[i]):
                    p2+=1
                if sign(R[i-1])!=sign(R[i]):
                    p3+=1
            p=0
            if min(p2-p1,p3-p2)==(p2-p1):
                if (p2-p1)!=0:
                    p=p2-p1
                    b=c
                else:
                    p=p3-p2
                    a=c
            else:
                if (p3-p2)!=0:
                    p=p3-p2
                    a=c
                else:
                    p=p2-p1
                    b=c
            print '[',a,b,']',' contiene ',p,' autovalores'
            print ''
        print 'El ultimo intervalo presenta valores aproximados a un autovalor.'
        print 'En particular un valor aproximado es: ',c
        print ''
        menu(A,n)
    else:
        print 'El intervalo [a,b] no contiene todos los autovalores'
        print ''
        menu(A,n)
def autovJac(A,n):
    menu(A,n)
def autovQR(A,n):
    menu(A,n)
def polin(A,n,v,k):
    D=dema(n,1)
    for i in range(n):
        D[i]=A[i][i]
    T=dema(n-1,1)
    for i in range(n-1):
        T[i]=A[i+1][i]
    P=dema(n+1,1)
    P[0]=1
    P[1]=D[0]-v
    for i in range(2,n+1):
        P[i]=(D[i-1]-v)*P[i-1]-(T[i-2]**2)*P[i-2]
    return P[k]
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
def inconsis(A,n):
    M=adq(A,n,n)
    Q=dema(n,1)
    con=0
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=max1(M,i,n)
            pivo(M,i,p,2)
        for j in range (i+1,n):
            if M[i][i]==0:
                con=1
                break
            else:
                w = M[j][i]*(M[i][i])**(-1)
                for k in range (i,n):
                    M[j][k] =M[j][k] - (w*M[i][k])
                    M[j][i]=0
    return con
def dema(m,n):
    M=[]
    if n!=1:
        for i in range(m):
            M.append([0]*(n))
    else:
        for i in range(m):
            M.append(0)
    return M
def Givens(A,m,n):
    M=[]
    for i in range (m):
        M.append([0]*(n))
    for i in range(m):
        for j in range(n):
            M[i][j]=A[i][j]
    x=[]
    for i in range(n):
        x.append(0)
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
    #limpiar Matriz A
    for i in range(n):
        for j in range(n):
            if i>j:
                M[i][j]=0
    for i in range(n,m):
        for j in range(n):
            M[i][j]=0
    return M
def inversa(M,n):
    I=iden(n)
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=max1(M,i,n)
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
def trans2(M,m,n):
    N=dema(n,m)
    for i in range (n):
        for j in range (m):
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
def multip2(M1,M2,m,n):
    M3=dema(n,n)
    for x in range (n):
        for y in range (n):
            suma=0
            for z in range (m):
                suma=suma+M1[x][z]*M2[z][y]
            M3[x][y]=suma
    return M3
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
main()
