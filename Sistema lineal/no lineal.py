from math import *
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
def main():
    print 'Determinaremos la solucion de f(x)=0'
    print 'A continuacion ingrese los extremos del intervalo [a,b]:'
    a1=input('a:')
    b1=input('b:')
    print ''
    print 'A continuacion ingrese la funcion f(x):'
    print ''
    f=raw_input('f(x)=')
    print 'Desea ver la grafica de la funcion?'
    print '1.SI'
    print '2.NO'
    r=input('Ingrese 1 o 2:')
    print ''
    if r==1:
        grafica(a1,b1,f)
    else:
        menu(a1,b1,f)
def grafica(a1,b1,f):
    print 'Vuelva a ingresar la funcion f'
    print 'pero haciendo cambios de ser necesario:'
    print ''
    print 'sin(x) --hacer--> np.sin(x)'
    print 'ln(x) --hacer--> np.log(x)'
    print 'exp(x) --hacer--> np.exp(x)'
    print '(En general cual funcion matematica se le adiciona "np".)'
    print ''
    print 'NOTA: Se mostrara la grafica de f para que observe si existe'
    print 'o no una raiz en  [a,b], e intuya un punto inicial cercano a '
    print 'dicha raiz para cuando se le pida en algunos metodos.'
    print ''
    print 'Luego de mostrarse la ventana con la grafica'
    print 'CIERRELA PARA CONTINUAR'
    print ''
    g=raw_input('f(x)=')
    x=np.arange(float(a1),float(b1),0.00001)
    f_x=eval(g)
    plt.plot(x,f_x)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    menu(a1,b1,f)
def fx(f,y):
    x=y
    m=float(eval(f))
    return m
def der(f):
    x= symbols('x')
    init_printing(use_unicode=True)
    h=diff(f,x)
    df=''
    df+=str(h)
    return df
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
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def inicial():
    print 'Ingrese un punto inicial:'
    xi=input('xi=')
    return xi
def NewtonRaphson(a1,b1,f):
    a=float(a1)
    b=float(b1)
    df=der(f)
    fa=fx(f,a)
    fb=fx(f,b)
    A=[]
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
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
    print "f'(x)=",df
    print ''
    x0=a
    x1=b
    dx=fx(df,x1)
    x2=x1-fx(f,x1)*(dx**(-1))
    fa=fx(f,a)
    fb=fx(f,b)
    if fa*fb > 0:
        print 'El intervalo [a,b] no contiene una raiz'
    else:
        print 'El intervalo [a,b] contiene una raiz'
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
            else:
                Aitken(A,tol,i-1,f)
                menu(a1,b1,f)
        else:
            menu(a1,b1,f)
def menu(a1,b1,f):
    print 'Seleccione un metodo:'
    print ''
    print '1.Biseccion'
    print '2.RegulaFalsi'
    print '3.Punto Fijo'
    print '4.Newton-Raphson'
    print '5.Newton Modificado'
    print '6.Secante'
    print '7.Steffensen'
    print '8.Trabajar con otra funcion'
    print '9.SALIR'
    r=input('')
    if r==1:
        biseccion(a1,b1,f)
    elif r==2:
        RegulaFalsi(a1,b1,f)
    elif r==3:
        puntofijo(a1,b1,f)
    elif r==4:
        NewtonRaphson(a1,b1,f)
    elif r==5:
        newtonmod(a1,b1,f)
    elif r==6:
        Secante(a1,b1,f)
    elif r==7:
        Steffensen(a1,b1,f)
    elif r==8:
        main()
    elif r==9:
        pass
    else:
        'Ingrese un numero valido'
        menu(a1,b1,f)
main()
