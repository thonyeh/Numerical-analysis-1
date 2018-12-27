import math
import time
mn = int(raw_input("ingrese la mantisa "))
b = int(raw_input("ingrese la base "))
U = int(raw_input("ingrese U "))
L = int(raw_input("ingrese L "))
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
        cad = str(num%b)+cad
        num = int(math.floor(num/b))
        a+=1
else:
    cad = cad + '0'
    
p = m
while m != 0:
    m = m*b
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
        cade = str(a%b)+cade
        a = int(math.floor(a/b))
else:
    cade = cade + '0'

while(len(cad)<mn+c+1):
    cad= cad + '0'
    
while(len(cade)<U):
    cade='0'+ cade
    
print ('longitud de palabra:',1+1+mn+len(cade))


nm=0
v=len(cade)
nm = 2*(b-1)*(b**(mn-1))*(U-L+1)+1

print ('numero de elementos del conjunto de maqui:',nm)

print('el numero se aguarda en la maquina asi:')
print (sn,se,cade,cad[c:c+mn])
