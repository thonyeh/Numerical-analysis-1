from math import *
from numpy import *
from numpy import log as ln
import sympy as sy
import matplotlib.pyplot as plt
def main():
    print 'Que desea resolver?'
    print ''
    print '1.Una ecuacion de la forma f(x)=0 (una sola variable. f:R --> R)'
    print '2.Un sistema de ecuaciones f(x1,x2,...,xn)=0 (2 o mas variables. f:R^n --> R^n)'
    r=input('')
    print ''
    if r==1:
        equ()
    elif r==2:
        syst()
    else:
        print 'Ingrese una opcion valida'
        print ''
        main()
def equ():
    print 'Determinaremos la solucion de f(x)=0'
    print ''
    print 'A continuacion ingrese los extremos del intervalo [a,b]:'
    a1=input('a:')
    b1=input('b:')
    print ''
    print 'A continuacion ingrese la funcion f(x):'
    print ''
    print 'NOTA: Se mostrara la grafica de f para que observe si existe'
    print 'o no una raiz en [a,b], e intuya un punto inicial cercano a '
    print 'dicha raiz para cuando se le pida en algunos metodos.'
    print ''
    print 'Luego de mostrarse la ventana con la grafica'
    print 'CIERRELA PARA CONTINUAR'
    print ''
    f=raw_input('f(x)=')
    grafica(a1,b1,f)
    menu(a1,b1,f)
def grafica(a1,b1,f):
    x=arange(float(a1),float(b1),0.00001)
    f_x=eval(f)
    plt.plot(x,f_x)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
def Epsilon():
    eps=1
    epsilon=0
    while (eps +1)>1:
        epsilon=eps
        eps=0.5*eps
    return epsilon
def fx(f,y):
    x=y
    m=float(eval(f))
    return m
def der(f):
    x= sy.symbols('x')
    sy.init_printing(use_unicode=True)
    h=sy.diff(f,x)
    df=''
    df+=str(h)
    return df
def inicial():
    print 'Ingrese un punto inicial:'
    xi=input('xi=')
    return xi
def Aitken(A,tol,i,f):
    k=0
    B=[]
    for j in range(i):
        B.append(0.0)
    print 'Usando el acelerador de Aitken'
    ite='It(k)'
    M1='xk'
    N1='f(xk)'
    print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
    print ''.ljust(35,'-')
    while (A[k]!=0.0):
        if k+2>i-1:
            break
        if( abs( A[k+1]-2*A[k]+A[k-1] ) <tol ):
            break
        B[k]=A[k]-((A[k+1]-A[k])**2)/(A[k]-2*A[k+1]+A[k+2])
        ite=''
        ite+=str(k+1)
        M1=''
        N1=''
        M1+=str(B[k])
        N1+=str(fx(f,B[k]))
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
        print ''.ljust(47,'-')
        if abs(fx(f,B[k]))<tol:
            break
        k+=1
    print 'xk de la ultima iteracion es la raiz'
def biseccion(a1,b1,f):
    A=[]
    a=float(a1)
    b=float(b1)
    i=1
    fa=fx(f,a)
    fb=fx(f,b)
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        tol=input('Ingrese el tol:')
        ite='It(k)'
        M1='a,f(a)'
        M2='b,f(b)'
        M3='xk,f(xk)'
        print ite.ljust(5),'|', M1.ljust(25),'|',M2.ljust(25),'|',M3.ljust(25)
        print''.ljust(85,'-')
        while (abs(a-b)>tol):
            ite=''
            ite+=str(i)
            M1='a='
            M2='b='
            M3='xk='
            N1='f(a)='
            N2='f(b)='
            N3='f(xk)='
            c=(a+b)*((2.0)**(-1))
            A.append(c)
            fa=fx(f,a)
            fb=fx(f,b)
            fc=fx(f,c)
            M1+=str(a)
            N1+=str(fa)
            M2+=str(b)
            N2+=str(fb)
            M3+=str(c)
            N3+=str(fc)
            print ite.ljust(5),'|', M1.ljust(25),'|',M2.ljust(25),'|',M3.ljust(25)
            ite=''
            print ite.ljust(5),'|', N1.ljust(25),'|',N2.ljust(25),'|',N3.ljust(25)
            print ''.ljust(89,'-')
            if fc ==0:
                a=c
                b=c
            elif fb*fc > 0:
                b=c
            else:
                a=c
            i+=1
        print 'la raiz es:',c
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def NewtonRaphson(a1,b1,f):
    a=float(a1)
    b=float(b1)
    df=der(f)
    fa=fx(f,a)
    fb=fx(f,b)
    A=[]
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        print "f'(x)=",df
        print ''
        print 'Ingrese un punto inicial, xi:'
        xi=input('xi=')
        if fx(f,xi)*(fx(df,xi)**(-1))>=0:
            print 'Debido al punto inicial escogido'
            print 'se obtendra una raiz menor o igual al valor de dicho punto'
            print ''
        else:
            print 'Debido al punto inicial escogido'
            print 'se obtendra una raiz mayor o igual al valor de dicho punto'
            print ''
        x0=xi+1
        i=1
        tol=input('Ingrese el tol:')
        print ''
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(xi-x0)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=xi
            xi=x0-fx(f,x0)*(fx(df,x0)**(-1))
            A.append(xi)
            M1+=str(xi)
            N1+=str(fx(f,xi))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            i+=1
        print 'la raiz es:',xi
        if xi<a or xi>b:
            print 'Esta raiz no se encuentra en el intervalo'
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def Newtondf(a1,b1,f):
    a=float(a1)
    b=float(b1)
    fa=fx(f,a)
    fb=fx(f,b)
    df=der(f)
    A=[]
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        print ''
        print 'Ingrese un punto inicial, xi:'
        xi=input('xi=')
        if fx(f,xi)*(fx(df,xi)**(-1))>=0:
            print 'Debido al punto inicial escogido'
            print 'se obtendra una raiz menor o igual al valor de dicho punto'
            print ''
        else:
            print 'Debido al punto inicial escogido'
            print 'se obtendra una raiz mayor o igual al valor de dicho punto'
            print ''
        x0=xi+1
        i=1
        tol=input('Ingrese el tol:')
        h=sqrt(Epsilon())
        print ''
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(xi-x0)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=xi
            xi=x0-fx(f,x0)*h*((fx(f,x0+h)-fx(f,x0))**(-1))
            A.append(xi)
            M1+=str(xi)
            N1+=str(fx(f,xi))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            i+=1
        print 'la raiz es:',xi
        if xi<a or xi>b:
            print 'Esta raiz no se encuentra en el intervalo'
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)    
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def newtonmod(a1,b1,f):
    a=float(a1)
    b=float(b1)
    A=[]
    df=der(f)
    fa=fx(f,a)
    fb=fx(f,b)
    print "f'(x)=",df
    print ''
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        print ''
        print 'Ingrese un punto inicial, xi:'
        x1=input('xi=')
        dx=fx(df,x1)
        x2=x1-fx(f,x1)*(dx**(-1))
        i=1
        tol=input('Ingrese el tol:')
        print ''
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(x2-x1)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x1=x2
            x2=x1-fx(f,x1)*(dx**(-1))
            A.append(x1)
            M1+=str(x1)
            N1+=str(fx(f,x1))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            print ''
            i+=1
        print 'la raiz es:',x1
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def Secante(a1,b1,f):
    a=float(a1)
    b=float(b1)
    A=[]
    print 'El metodo iniciara con x0=a y x1=b como puntos iniciales'
    print ''
    x0=a
    x1=b
    x2=x1-fx(f,x1)*(x1-x0)*((fx(f,x1)-fx(f,x0))**(-1))
    i=1
    tol=input('Ingrese el tol:')
    print ''
    fa=fx(f,a)
    fb=fx(f,b)
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(x2-x1)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=x1
            x1=x2
            x2=x1-fx(f,x1)*(x1-x0)*(fx(f,x1)-fx(f,x0))**(-1)
            A.append(x1)
            M1+=str(x1)
            N1+=str(fx(f,x1))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            i+=1
        print 'la raiz es:',x1
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def RegulaFalsi(a1,b1,f):
    a=float(a1)
    b=float(b1)
    A=[]
    i=1
    fa=fx(f,a)
    fb=fx(f,b)
    x1=1
    x0=0
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        tol=input('Ingrese el tol:')
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(x1-x0)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=x1
            x1=a-(fx(f,a))*(b-a)*(fx(f,b)-fx(f,a))**(-1)
            fa=fx(f,a)
            fb=fx(f,b)
            fx1=fx(f,x1)
            A.append(x1)
            M1+=str(x1)
            N1+=str(fx(f,x1))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            if fx1==0:
                a=x1
                b=x1
            elif fb*fx1 > 0:
                b=x1
            else:
                a=x1
            i+=1
        print 'la raiz es:',x1
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def Banach(a1,b1,f,xi):
    g=raw_input('g(x)=')
    dg=der(g)
    if abs(fx(dg,xi))>=1:
        print 'La funcion g ingresada no cumple dicho teorema'
        print ''
        sel(a1,b1,f,xi)
    return g
def sel(a1,b1,f,xi):
    print 'Seleccione una opcion:'
    print '1.Ingresar otro g'
    print '2.Ir a otro metodo de solucion'
    r=input('')
    if r==1:
        Banach(a1,b1,f,xi)
    elif r==2:
        menu(a1,b1,f)
    else:
        print 'Ingrese una opcion valida'
        print ''
        sel(a1,b1,f,xi)
def puntofijo(a1,b1,f):
    a=float(a1)
    b=float(b1)
    A=[]
    fa=fx(f,a)
    fb=fx(f,b)
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        xi=inicial()
        xi=float(xi)
        x0=xi+1
        print 'Ingrese una funcion g, despejando de f(x)=0'
        print 'tal que cumpla g(x)=x y el teorema de Banach'
        print ''
        g=Banach(a1,b1,f,xi)
        i=1
        tol=input('Ingrese el tol:')
        print ''
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(xi-x0)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=xi
            xi=fx(g,x0)
            A.append(xi)
            M1+=str(xi)
            N1+=str(fx(f,xi))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            print ''
            i+=1
        print 'la raiz es:',xi
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def Steffensen(a1,b1,f):
    a=float(a1)
    b=float(b1)
    A=[]
    x0=a
    xi=b
    fa=fx(f,a)
    fb=fx(f,b)
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
        menu(a1,b1,f)
    else:
        print 'El intervalo [a,b] contiene una raiz'
        print 'x(inicial)=',xi
        i=1
        tol=input('Ingrese el tol:')
        print ''
        ite='It(k)'
        M1='xk'
        N1='f(xk)'
        print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18)
        print ''.ljust(35,'-')
        while (abs(xi-x0)>tol):
            ite=''
            ite+=str(i)
            M1=''
            N1=''
            x0=xi
            g=(fx(f,x0+fx(f,x0))-fx(f,x0))*(fx(f,x0))**(-1)
            xi=x0-fx(f,x0)*g**(-1)
            A.append(xi)
            M1+=str(xi)
            N1+=str(fx(f,xi))
            print ite.ljust(5),'|',M1.ljust(18),'|',N1.ljust(18) 
            print ''.ljust(47,'-')
            i+=1
        print 'la raiz es:',xi
        print '---------'
        print 'Desea observar el proceso con el acelerador de AITKEN?'
        print '1.SI'
        print '2.NO'
        r=input('Ingrese 1 o 2:')
        print ''
        if r==1:
            if i-1<3:
                print 'No se puede aplicar Aitken'
                print 'debido a que ya posee menos de 3 iteraciones'
                menu(a1,b1,f)
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def menu(a1,b1,f):
    print 'Seleccione un metodo:'
    print ''
    print '1.Biseccion'
    print '2.Newton-Raphson'
    print '3.Newton por Diferencias finitas'
    print '4.Newton Modificado'
    print '5.Secante'
    print '6.Regula Falsi'
    print '7.Punto Fijo'
    print '8.Steffensen'
    print '9.SI DESEA REINICIAR'
    print '10.SI DESEA SALIR'
    r=input('')
    if r==1:
        biseccion(a1,b1,f)
    elif r==2:
        NewtonRaphson(a1,b1,f)
    elif r==3:
        Newtondf(a1,b1,f)
    elif r==4:
        newtonmod(a1,b1,f)
    elif r==5:
        Secante(a1,b1,f)
    elif r==6:
        RegulaFalsi(a1,b1,f)
    elif r==7:
        puntofijo(a1,b1,f)
    elif r==8:
        Steffensen(a1,b1,f)
    elif r==9:
        main()
    elif r==10:
        pass
    else:
        print 'Ingrese una opcion valida'
        menu(a1,b1,f)
def syst():
    print 'Determinaremos una solucion de:'
    print 'f(x)=(f1(x),f2(x),...,fn(x))=(0,0,...,0) con x=(x1,x2,...,xn)'
    print ''
    print 'NOTA: cada fj con j perteneciente a {1,..,n}'
    print 'corresponde a cada fila del sistema'
    print ''
    print 'Primero indique el valor de "n"(dimension del sistema) con el que trabajara'
    n=input ('n:')
    print ''
    print 'Ahora determine cada fj(x).con variables x1,...,xn'
    print 'EJEMPLO: f1(x)=x1*3+exp(x2-0.5)*x3'
    print ''
    F=[]
    for i in range (0,n):
        F.append(0)
    for j in range(0,n):
        F[j]=raw_input('f%d(x)='%(j+1))
    print ''
    print 'Se tiene el siguiente sistema:'
    for j in range(0,n):
        print F[j],'=0'
    print ''
    menu2(F,n)
def gausspp(A,n,b):
    M=[]
    for i in range(n):
        M.append([0]*(n+1))
    for i in range (n):
        for j in range (n):
            M[i][j]=A[i][j]
        M[i][n]=b[i]
    mayor=0
    Q=[]
    for s in range (n+1):
        Q.append([0])
    for i in range (n):
        j=i
        p=i
        mayor = M[j][i]
        for j in range (i+1,n):
            if(abs(mayor) < abs(M[j][i])):
                mayor= M[j][i]
                p = j
        for l in range (i,n+1):
            Q[l]=M[i][l]
            M[i][l]=M[p][l]
            M[p][l]=Q[l]  
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n+1):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
    x=[]
    for s in range (n):
        x.append(0)
    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= M[j][k]*x[k]
        x[j]=(M[j][n]-suma)/M[j][j]
    return x
def deriv(n,F,j,k):
    w='x1'
    for i in range (1,n):
        w+=str(' x')
        w+=str(i+1)
    x= sy.symbols(w)
    sy.init_printing(use_unicode=True)
    v='x'
    v+=str(k)
    h=sy.diff(F[j],v)
    dF=''
    dF+=str(h)
    return dF
def Jacobiano(F,n):
    dF=[]
    for i in range (0,n):
        dF.append([0]*n)
    for j in range(0,n):
        for k in range(0,n):
            dF[j][k]=deriv(n,F,j,k+1)
    return dF
def modulo(x,n):
    s=0
    for i in range(0,n):
        s+=x[i]**2
    s=sqrt(s)
    return s
def Fx(F,j,n,z):
    x1=z[0]
    x2=z[1]
    if 2<n:
        x3=z[2]
    if 3<n:
        x4=z[3]
    if 4<n:
        x5=z[4]
    if 5<n:
        x6=z[5]
    if 6<n:
        x7=z[6]
    if 7<n:
        x8=z[7]
    if 8<n:
        x9=z[8]
    if n==10:
        x10=z[9]
    if n >10:
        print 'error'
    else:
        m=float(eval(F[j]))
    return m
def dFx(dF,j,k,n,z):
    x1=z[0]
    x2=z[1]
    if 2<n:
        x3=z[2]
    if 3<n:
        x4=z[3]
    if 4<n:
        x5=z[4]
    if 5<n:
        x6=z[5]
    if 6<n:
        x7=z[6]
    if 7<n:
        x8=z[7]
    if 8<n:
        x9=z[8]
    if n==10:
        x10=z[9]
    if n >10:
        print 'error'
    else:
        m=float(eval(dF[j][k]))
    return m
def Newtonrph(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(0,n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    for i in range(0,n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for j in range(0,n):
            for k in range(0,n):
                eF[j][k]=dFx(dF,j,k,n,y0)
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtonrphmod(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(0,n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    for i in range(0,n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    for j in range(0,n):
        for k in range(0,n):
            eF[j][k]=dFx(dF,j,k,n,y0)
    while m>=0:
        m+=1
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtonjac(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(0,n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    for i in range(0,n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for j in range(0,n):
            eF[j][j]=dFx(dF,j,j,n,y0)
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtongauss(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(0,n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    for i in range(0,n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for j in range(0,n):
            for k in range(0,j+1):
                eF[j][k]=dFx(dF,j,k,n,y0)
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def NewtonSOR(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(0,n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    for i in range(0,n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    w=input('Ingrese el parametro w:')
    ro=(1-w)*w**(-1)
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for j in range(0,n):
            for k in range(0,j):
                eF[j][k]=dFx(dF,j,k,n,y0)
            eF[j][j]=dFx(dF,j,j,n,y0)*(1.0+ro)
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtonrphdf(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    h=sqrt(Epsilon())
    print 'La matriz Jacobiana es:'
    for i in range(n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    v=[]
    for i in range(n):
        f.append(0)
        fy.append(0)
        v.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for i in range(n):
            v[i]=y0[i]
        for j in range(n):
            for k in range(n):
                v[k]=y0[k]+h
                eF[j][k]=(Fx(F,j,n,v)-Fx(F,j,n,y0))/h
                v[k]=y0[k]
        for j in range(n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(n):
            y1[i]=y0[i]+x[i]
        for j in range(n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtonrphdfjac(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    h=sqrt(Epsilon())
    print 'La matriz Jacobiana es:'
    for i in range(n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    v=[]
    for i in range(n):
        f.append(0)
        fy.append(0)
        v.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for i in range(n):
            v[i]=y0[i]
        for j in range(0,n):
            v[j]=y0[j]+h
            eF[j][j]=(Fx(F,j,n,v)-Fx(F,j,n,y0))/h
            v[j]=y0[j]    
        for j in range(n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(n):
            y1[i]=y0[i]+x[i]
        for j in range(n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Newtonrphdfgauss(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    h=sqrt(Epsilon())
    print 'La matriz Jacobiana es:'
    for i in range(n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    v=[]
    for i in range(n):
        f.append(0)
        fy.append(0)
        v.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for i in range(n):
            v[i]=y0[i]
        for j in range(0,n):
            for k in range(0,j+1):
                v[k]=y0[k]+h
                eF[j][k]=(Fx(F,j,n,v)-Fx(F,j,n,y0))/h
                v[k]=y0[k]
        for j in range(n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(n):
            y1[i]=y0[i]+x[i]
        for j in range(n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def NewtonrphdfSOR(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    h=sqrt(Epsilon())
    print 'La matriz Jacobiana es:'
    for i in range(n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    v=[]
    for i in range(n):
        f.append(0)
        fy.append(0)
        v.append(0)
        y0.append(0)
        y1.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    w=input('Ingrese el parametro w:')
    ro=(1-w)*w**(-1)
    tol=input('Ingrese el tol:')
    print ''
    m=0
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    while m>=0:
        m+=1
        for i in range(n):
            v[i]=y0[i]
        for j in range(0,n):
            for k in range(0,j):
                eF[j][k]=dFx(dF,j,k,n,y0)
            eF[j][j]=dFx(dF,j,j,n,y0)*(1.0+ro)
        for j in range(n):
            for k in range(j):
                v[k]=y0[k]+h
                eF[j][k]=(Fx(F,j,n,v)-Fx(F,j,n,y0))/h
                v[k]=y0[k]
            v[j]=y0[j]+h
            eF[j][j]=((Fx(F,j,n,v)-Fx(F,j,n,y0))/h)*(1.0+ro)
            v[j]=y0[j]
        for j in range(n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(eF,n,f)
        for i in range(n):
            y1[i]=y0[i]+x[i]
        for j in range(n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        s=modulo(fy,n)
        ite=''
        for i in range(n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
        y0=y1
        if s<tol:
            break
    menu2(F,n)
def Broyden(F,n):
    dF=Jacobiano(F,n)
    eF=[]
    f=[]
    fy=[]
    print 'La matriz Jacobiana es:'
    for i in range(n):
        print dF[i]
        eF.append([0]*n)
    print ''
    print 'Defina un punto inicial x0 perteneciente a R^n:'
    y0=[]
    y1=[]
    z=[]
    for i in range(n):
        f.append(0)
        fy.append(0)
        y0.append(0)
        y1.append(0)
        z.append(0)
        y0[i]=input('x0[%d]='%(i+1))
    print ''
    print 'Inicialize con matriz:'
    A=[]
    for i in range(n):
        A.append([0]*n)
    for i in range(n):
        print 'Ingrese los %d elementos de la fila %d'%(n,i+1)
        for j in range(n):
            A[i][j]=input('')
    tol=input('Ingrese el tol:')
    print ''
    m=1
    ite='It(k)'
    M1='xk'
    N1='||f(xk)||'
    print ite.center(5),'|',M1.center(25),'|',N1.center(18)
    print ''.ljust(50,'-')
    for j in range(0,n):
        fy[j]=Fx(F,j,n,y1)
    s=modulo(fy,n)
    for i in range(n):
        y1[i]=y0[i]
    while s>tol:
        m+=1
        for j in range(0,n):
            f[j]=(-1)*Fx(F,j,n,y0)
        x=gausspp(A,n,f)
        for i in range(0,n):
            y1[i]=y0[i]+x[i]
        for j in range(0,n):
            z[j]=Fx(F,j,n,y1)-Fx(F,j,n,y0)
        p=0
        for i in range(n):
            p+=x[i]**2
        B=[]
        C=[]
        for i in range(n):
            B.append(0)
            C.append([0]*n)
        for i in range(n):
            B[i]=z[i]
            for j in range(n):
                B[i]-=A[i][j]*x[j]
        for i in range(n):
            for j in range(n):
                C[i][j]=B[i]*x[j]*p**(-1)
        for i in range(n):
            for j in range(n):
                A[i][j]=A[i][j]+C[i][j]
        for j in range(0,n):
            fy[j]=(-1)*Fx(F,j,n,y1)
        for i in range(n):
            y0[i]=y1[i]
        s=modulo(fy,n)
        ite=''
        for i in range(0,n):
            if i==0:
                ite+=str(m)
                M1='x1='
                N1=''
                M1+=str(y1[0])
                N1+=str(s)
                print ite.ljust(5),'|',M1.ljust(25),'|',N1.ljust(20) 
            else:
                ite=''
                M1='x'
                M1+=str(i+1)
                M1+='='
                N1=''
                M1+=str(y1[i])
                print ite.ljust(6),'|',M1.ljust(25),'|',N1.ljust(20)
        print ''.ljust(50,'-')
    menu2(F,n)
def menu2(F,n):
    print 'Seleccione un metodo:'
    print ''
    print '1.Newton-Raphson(llamado tambien Newton)'
    print '2.Newton Modificado'
    print '3.Newton variante Jacobi'
    print '4.Newton variante Gauss-Seidel'
    print '5.Newton variante Relajacion SOR'
    print '6.Newton por Diferencias finitas'
    print '7.Newton por Diferencias finitas variante Jacobi'
    print '8.Newton por Diferencias finitas variante Gauss-Seidel'
    print '9.Newton por Diferencias finitas variante Relajacion SOR'
    print '10.Broyden'
    print '11.SI DESEA REINICIAR'
    print '12.SI DESEA SALIR'
    r=input('')
    if r==1:
        Newtonrph(F,n)
    elif r==2:
        Newtonrphmod(F,n)
    elif r==3:
        Newtonjac(F,n)
    elif r==4:
        Newtongauss(F,n)
    elif r==5:
        NewtonSOR(F,n)
    elif r==6:
        Newtonrphdf(F,n)
    elif r==7:
        Newtonrphdfjac(F,n)
    elif r==8:
        Newtonrphdfgauss(F,n)
    elif r==9:
        NewtonrphdfSOR(F,n)
    elif r==10:
        Broyden(F,n)
    elif r==11:
        main()
    elif r==12:
        pass
    else:
        print 'Ingrese una opcion valida'
        menu2(F,n)
main()
