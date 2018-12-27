from math import *
from numpy import *
from numpy import log as ln
import sympy as sy
import matplotlib.pyplot as plt
def datos(a,b,w):
    print 'Ingrese la cantidad de datos conocidos:'
    m=input ('')
    print ''
    print 'Iingrese los puntos conocidos y sus respectivos f(xk)'
    n=m-1
    M=[0]*(n+1)
    N=[0]*(n+1)
    for i in range (n+1):
        M[i]=input('x%d='%i)
        N[i]=input('f(x%d)='%i)
    if w==1:
        puntos(b,M,N,m,w)
        R=lagrange(M,N,m)
        print 'El polinomio de Lagrange es:'
        print 'O(x)=',R
        print ''
    if w==2:
        puntos(b,M,N,m,w)
        R=lagrange(M,N,m)
        print 'El polinomio de Lagrange es:'
        print 'D(x)=',R
        print ''
    grafica(a,b,R)
    return  R
def main():
    print 'Tengamos en cuenta'
    print 'Q: cantidad'
    print 'P:precio'
    print 'Ingrese el intervalo [a,b]'
    a=input('a=')
    b=input ('b=')
    print ''
    print 'RELACION Q-P (OFERTA)'
    print ''
    O=datos(a,b,1)
    print 'RELACION Q-P (DEMANDA)'
    print ''
    D=datos(a,b,2)
    doscurvas(a,b,O,D)
    print 'Para la determinacion aproximada del punto de equilibrio'
    print 'Tenemos que resolver O(x)=D(x)'
    F=O
    F+='-('
    F+=D
    F+=')'
    print 'es decir:'
    print F,'=0'
    menu(O,D)
def menu(O,D):
    print '1.Evalue un valor en O(x):'
    print '2.Evalue un valor en D(x):'
    print '3.REINICIAR'
    print '4.SALIR'
    r=input('')
    if r==1:
        x=input('x=')
        print fx(O,x)
        menu(O,D)
    elif r==2:
        x=input('x=')
        print fx(D,x)
        menu(O,D)
    elif r==3:
        main()
    else:
        pass
def fx(f,y):
    x=y
    m=float(eval(f))
    return m
def grafica(a1,b1,f):
    x=arange(float(a1),float(b1),0.00001)
    f_x=eval(f)
    plt.plot(x,f_x)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
def puntos(b,M,N,m,w):
    plt.plot(M,N,'ro')
    if w==1:
        plt.axis([1,b,-10,N[m-1]+0.5])
    if w==2:
        plt.axis([0,b,0,N[0]+0.5])
    plt.show()
def doscurvas(a,b,P,Q):
    x=arange(float(a),float(b),0.00001)
    f_x=eval(P)
    plt.plot(x,f_x)
    f_x2=eval(Q)
    plt.plot(x,f_x2)
    plt.xlabel('x')
    plt.show()
def lagrange(M,N,m):
    P=''
    s=0
    for i in range(m):
        s1=N[i]
        for j in range(m):
            if j!=i:
                s1=s1*(M[i]-M[j])**(-1)
        print s1
        print ''
        s+=s1
    P+=str(s)
    P+='*x**2'
    s=0
    for i in range(m):
        s2=(-1)*N[i]
        p=0
        for j in range(m):
            if j!=i:
                p+=M[j]
        s2*=p
        for j in range(m):
            if j!=i:
                s2=s2*(M[i]-M[j])**(-1)
        s+=s2
    if s!=0:
        if s>=0:
            P+='+'
        P+=str(s)
        P+='*x'
    s=0
    for i in range(m):
        s3=N[i]
        for j in range(m):
            if j!=i:
                s3=s3*(M[j])*(M[i]-M[j])**(-1)
        s+=s3
    if s!=0:
        if s>=0:
            P+='+'
        P+=str(s)
    return P
main()
