num1 = int(input("Ingrese un número real: "))
num2 = int(input("Ingrese otro número real: "))

if num1 > num2:
    print(f"{num1} es el mayor")
elif num2 > num1:
    print(f"{num2} es el mayor")
else:
    print("los números ingresados son iguales")
