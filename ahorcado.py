from random import * #para poder sacar aleatorios de las listas

palabras = ['perro', 'luz', 'cielo', 'programar'] #guardamos las palabras que queremos usar 
aleatorio = choice(palabras) #para sacar un numero aleatioro de los que estan guardados



print("La palabra secreta es " ,aleatorio, ) #solo para saber que palabra es para las pruebas

intentos = 5;
letra = input ("mete una letra: ") #le pedimos que meta una letra para empezar a jugar

while intentos >= 1:
    print(f"No esta, te quedan {intentos} intentos mas")
    intentos -= 1
    letra = input ("mete una letra") #le pedimos que meta cuando falle y le queden oportunidades

else:
    print("PERDISTE")  # Cuando tienes 6 fallos dice que perdiste
