# Ejemplo 2. Operaciones matematicas

# ENTRADA DE DATOS
# Declarara  o craer varibles
 
from ssl import PROTOCOL_TLSv1_2


numero_1 = 10 
numero_2 = 2
# declarar o crear constatnte: Elemento que su valor permanece fijo
PI = 3.1416


# PROCESOS (CALCULOS U OPERACIONES MATEMATICAS Y/O LOGICASS: IF, ELIF Y ELSE)
suma = numero_1 + numero_2
resta = numero_1-numero_2
multiplicar = numero_1*numero_2
dividir = numero_1/numero_2
pot1 = numero_1**numero_2
pot2  = numero_2**numero_1
raiz1 =  pow(numero_1, numero_2)
raiz2 = pow(numero_2, numero_1)
# SALIDAS DE DATOS(Mostarar resultados)          
print("La suma es igual= " , suma )
print("la resta es=  "  + str(resta) )#concatetacion union de uno mas textoa
print (f"La divivcion es = {dividir}")
print(f"primera potencia es {pot1}")
print("la 2da potencia es ", pot2)
print("la raiz es " +  str(raiz1))
print("La segunda raiz es ", raiz2)
#CONVERSION CONVERSION DE UN TIPO DE DATO A OTRO 
print(f"la multiplicacion es ={multiplicar} ")#Interpolacion de texto f : formato