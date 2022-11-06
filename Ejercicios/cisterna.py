nivel = float(input("Nivel de agua en metros :  "))

#mayor de 6
if(nivel > 6): 
    print("Desbordamiento de agua")
elif(nivel == 6):
    print("Apagar bomba")

#DE 4 Y 6
elif(nivel >=4 and nivel < 6):  
    print("desacelerar bomba")
#de 2 y 4
elif (nivel >= 2 and nivel <4 ):
    print("Bomba trbajando") 
#2 a 0 
elif(nivel > 0 and nivel <2): 
    print("Acelerar bomba de agua")
#0 y 2 
elif(nivel > 0): 
    print("Encender bomba")
#menor 0 
elif(nivel ==  0 ): 
    print("Fuga en cisterna")