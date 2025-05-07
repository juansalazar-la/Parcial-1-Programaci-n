num1= int(input("Ingrese el primer número entero: "))    #Pide al usuario ingresar 5 números enteros
num2= int(input("Ingrese el segundo número entero: "))
num3= int(input("Ingrese el tercer número entero: "))
num4= int(input("Ingrese el cuarto número entero: "))
num5= int(input("Ingrese el quinto número entero: "))


if num1 > 0:                           #Si el número 1 es mayor a 0 y par se imprime normal,
    if num1 % 2 == 0:                  #Si no cumple con esas condiciones el número es igual a 0
        valor1= num1                   #Mismo condicional para cada número
    else:
         valor3= 0
else:
    valor1= 0

if num2 > 0:
    if num2 % 2 == 0:
        valor2= num2
    else:
         valor2= 0
else:
    valor2= 0

if num3 > 0:
     if num3 % 2 == 0:
        valor3 = num3
     else:
         valor3= 0
else:
    valor3= 0

if num4 > 0:
    if num4 % 2 == 0:
        valor4 = num4
    else:
         valor4= 0
else:
    valor4= 0
    
if num5 > 0:
    if num5 % 2 == 0:
        valor5 = num5
    else:
         valor5= 0
else:
    valor5= 0

suma= valor1 + valor2 + valor3 + valor4 + valor5    #Se suman los 5 números

print(f"LA suma total de los números es: {suma}")   #Se imprime la suma de los números que son par y positivos