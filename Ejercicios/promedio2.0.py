cal1 = float(input("Igrese la primera calificacion: "))
cal2 = float(input("Ingrese la segunda calificacion: "))
cal3 = float(input("Ingrese la tercera calificacion: "))


suma = cal1+cal2+cal3
promedio = suma / 3
print("El promedio es: ", promedio)

if (promedio > 6 and promedio <10):  # rango entre 18 hasta 120 años 
    print("Promedio")
elif(cal1 < 0 or cal1 >10):
    print("Errro en sistema,ingrese corectamente las calififcaciones  ")
elif(cal2 < 0 or cal2 >10):
    print("Errro en sistema,ingrese corectamente las calififcaciones ")
elif(cal3 < 0 or cal3 >10):
    print("Errro en sistema,ingrese corectamente las calififcaciones  ")
elif (promedio == 6 ):
    print("Aprobado de pansazo")
elif(promedio >= 0 and promedio < 6): 
    print("Reprobado ")
