
from xml.etree.ElementTree import C14NWriterTarget


a = float(input("Ingrese valor para a= "))
b = float(input("Ingrese valor para b= "))
c = float(input("Ingrese valor para c= "))

op1 = b**2
op2 = 4*a*c
op3 = 2*a
op4 = -b
op5 = op1 - op2

f1= pow (op5,1/2)
f2= op4 + f1
x1 = f2/op3
f3 = op4 - f1
x2 = f3/op3

print("X1= ", x1)
print("X2= ", x2)