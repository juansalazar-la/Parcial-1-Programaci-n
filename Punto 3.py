
palabra = input("Escribe una palabra (sin espacios): ")  # Solicita la palabra al usuario


cont_a = 0             #Inicia el contador de cada vocal en 0
cont_e = 0             
cont_i = 0
cont_o = 0
cont_u = 0

for letra in palabra:                                  #Se usa un for para recorrer la palabra ingresada  
    if letra == 'a' or letra == 'A':                   # Se usa el condicional if para reconocer cada vocal minúscula o mayúscula
        cont_a = cont_a + 1                    # Si es una vocal el contador va sumando de a 1 dependiendo cuantas vocales encuentre
    elif letra == 'e' or letra == 'E':
        cont_e = cont_e + 1
    elif letra == 'i' or letra == 'I':
        cont_i = cont_i + 1
    elif letra == 'o' or letra == 'O':
        cont_o = cont_o + 1
    elif letra == 'u' or letra == 'U':
        cont_u = cont_u + 1

print("'a' o 'A':", cont_a)                #Se muestran el número de cada vocal en la palabra ingresada
print("'e' o 'E':", cont_e)
print("'i' o 'I':", cont_i)
print("'o' o 'O':", cont_o)
print("'u' o 'U':", cont_u)


