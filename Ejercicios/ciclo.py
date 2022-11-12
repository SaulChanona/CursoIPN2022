
j = float(input("Coloque un numero:"))

if (j < 0 and j >= -100):
    for j in range(-1, -100, -2): 
        print(f"{j}")
    
elif (j > 0 and j <= 100):
    for j in range(1, 100, 2): 
        print(f"{j}")

else: 
    print("Numero ivalido, coloquelo otra vez")




