
edad= int(input("Ingrese su edad: "))

if edad < 0:
    print("Este número no es válido")
elif edad < 13:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 59:
    print("Adulto")
else:
    print("Adulto mayor")

