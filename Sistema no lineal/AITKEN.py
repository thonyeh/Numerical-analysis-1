from math import *

def f(x):
	return e**x -sin(x)

def biseccion(a,b,TOL,NMAX):
	llave=True
	A=[]
	for i in range(NMAX):
		A.append(0.0)
		  
	if f(a)*f(b)<0.0:
		text='N\t c\t\t  f(c)\n'		
		N=0
		while N<NMAX:
			c=(b+a)/2
			A[N]=c
			if f(c)==0.0 or (b-a)/2<TOL:
				print text						
				return (A, llave)
			N=N+1
			text+="%d\t%.6f\t%.6f\n"%(N,c,f(c))
			if(copysign(1.0, f(c)) == copysign(1.0, f(a)) ):
				a=c
			else :
				b=c

		llave=False
		text+='FIN DEL NUMERO DE INTERVALOS\n'
		
	else:
		print 'ERROR DE INTERVALOS'
		llave=False
 
	return (A, llave)

	
def Aitken(A,tol,NMAX):
	i=0
	B=[]
	for j in range(NMAX):
		B.append(0.0)
	print 'AITKEN!!'
	text='k\t x \t\t f(x)\n'	

	
	while (A[i]!=0.0):
		if( abs( A[i+1]-2*A[i]+A[i-1] ) <tol ):
			print 'Denominador muy pequenho'
			break	
				
		B[i]= A[i] - ( (A[i+1] - A[i] )**2 )/(  A[i]-2*A[i+1]+A[i+2] )
		
		text+="%d\t%.6f\t%.6f\n"%( i+1, B[i], f(B[i]) )		
		if abs(f(B[i]))<tol:
			break 	
		i+=1
	print text
	return B

def main():
        a=-4.0
        b=-3.0
        tol= 0.000001
        NMAX=30
        A=[]
        llave=True
        text='N\t c\t\t  f(c)\n'
        A, llave = biseccion(a,b,tol,NMAX)
        if llave==True:
                print 'verdadero'
                B = Aitken(A,tol,NMAX)
        else:
                print 'error'
        print "fin\n"
    
if __name__=="__main__":
    main()


