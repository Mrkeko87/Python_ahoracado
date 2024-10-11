from random import * #para poder sacar aleatorios de las listas

palabras = ['perro', 'luz', 'cielo', 'programar'] #guardamos las palabras que queremos usar 
aleatorio = choice(palabras) #para sacar una palabra aleatioria de palabras
numletras = len(aleatorio)  # Contamos el número de letras en aleatorio


print("La palabra secreta es: ",aleatorio, "\nNumero de letras: ",numletras,) #solo para saber que palabra es para las pruebas

print(" - " * numletras) # Pintamos una linea por cada letra

intentos = 5;

letras = list(aleatorio) #asi guardamos en letras todas las letras de la palabra aleatoria
print (letras) #aqui estan todas las letras separadas

letra = input ("mete una letra: ") #le pedimos que meta una letra para empezar a jugar
while intentos >= 1: #Si le quedan intentos entra y mira si esta la letra o no
    if letra == letras:
        letra = input ("CORRECTO!! mete otra letra: ") #le pedimos que meta otra cuando acierte y le queden oportunidades
    else:      
            print(f"{letra} No esta, te quedan {intentos} intentos mas")
            intentos -= 1
            letra = input ("mete una letra: ") #le pedimos que meta cuando falle y le queden oportunidades
else:
    print("PERDISTE......La palabra que se escondia es: ",aleatorio,)  # Cuando tienes 6 fallos dice que perdiste
