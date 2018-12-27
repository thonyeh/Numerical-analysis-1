import math
import time
from array import array
n = float(raw_input("Ingrese un numero  "))
a = 0; sn = 0; cad = ""; cade = ""; d = 0; se = 0
if n < 0:
    n = (-1)*n
    sn = 1
else:
    sn = 0
    
num = int(n)
m = n-int(n)
if(num != 0):  
    while(num != 0):  
        cad = str(num%2)+cad
        num = int(math.floor(num/2))
        a+=1
else:
    cad = cad + '0'
    
p = m
while m != 0:
    m = m*2
    cad = cad + str(int(m))
    m = m - int(m)

if p != 0 and a==0:
    i = 1
    while cad[i]=="0":
        a+=1
        i+=1
        
c = 0
while cad[c]=="0":
    c+=1
if c>1:
    se=1
    
if(a != 0):  
    while(a != 0):  
        cade = str(a%2)+cade
        a = int(math.floor(a/2))
else:
    cade = cade + '0'

while(len(cad)<52+c+1):
    cad= cad + '0'
    
while(len(cade)<10):
    cade='0'+ cade
    
print ('longitud de palabra:',1+1+(len(cad)-c-1)+len(cade))
nm=0
v=len(cade)
nm = 2*(2-1)*(2**(52-1))*(20+1)+1

eps=1
epsilon=0
while (eps +1)>1:
    epsilon=eps
    eps=0.5*eps
print ('epsilon de la maquina:', epsilon)

e=epsilon
a=[0]
i=0
while i < 20:
    a.append(e)
    e=e*2
    i+=1
print ("los primeros 20 números de maquina son:")    
for i in range (20):    
    print (a[i])

print ('numero de elementos del conjunto de maqui:',nm)

print ('asi se guarda el numero en la maquina')
print sn,se,cade,cad[c+1:c+53]
