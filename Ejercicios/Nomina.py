input("Bienvenido a El puerquito feliz S.A DE C.V")
input ("CALCULAR NOMINA")
nombre = string(input("Nombre del Empleado: "))
dias = int(input("Dias trabajados EN ESTE MES"))

pd = 250
paba = pd*dias
ivatra = paba*.16
sub = paba + ivatra
ivarete = ivatra/3
isr = paba*.10
pagoneto = sub - ivarete - isr


print ("Tu nomina " , nombre , "es: ")
print ("PAGO BASE: ", paba)
print ("IVA: ", ivatra)
print ("Subtotal: ", sub)
print ("Iva retenido: ", ivarete)
print ("ISR detenido : ", isr)
print("Pago neto : ", pagoneto)




