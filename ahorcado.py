from random import * #para poder sacar aleatorios de las listas

palabras = ['perro', 'luz', 'cielo', 'programar'] #guardamos las palabras que queremos usar 
aleatorio = choice(palabras) #para sacar un numero aleatioro de los que estan guardados



print(aleatorio)

intentos = 5;

while intentos >= 0:
    print(f"Tienes {intentos}  intentos mas")
    intentos -= 1
    
else:
    print("perdiste")  # esto lo ejecuta al salir y no es necesario

respuesta = 's'