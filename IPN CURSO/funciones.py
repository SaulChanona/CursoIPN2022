#Funciones 
#son acciones o tareas a ejecutar (verbos en ar, er ir)
#sintaxis:

'''def Nombre_de_la_Funcion (argumento o parrametros):
    contenido de la funcion de la funcion
    return valor (es)
   '''

def Sumar(num1, num2):
    return num1 + num2 #Regrsar, dovolver , retornar un valor

def Restar(a, b):
    resta = a - b
    print("La resta =", resta)

def Mult(a, b):
    multiplicar = a*b
    print("La multiplicacion es = ", multiplicar)

def Div(num1, num2):
    div1 = num1/num2
    div2= num2/num2
    print("La primer divicion es = ", div1 , "La segunda es = ", div2)



#MANDAR A LLLAMR LOS PARAMETROS

#iMPRIMIR EL RESULTADO
print ("La suma =", Sumar(10, 5))
Restar(20, 50)
Mult(20, 30)
Div(40, 2)
