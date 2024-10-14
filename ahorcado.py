from random import * #para poder sacar aleatorios de la lista de nombres

palabras = ['perro', 'luz', 'cielo', 'programar'] #guardamos las palabras que queremos usar 
aleatorio = choice(palabras) #para sacar una palabra aleatioria de palabras
numletras = len(aleatorio)  # Contamos el número de letras en aleatorio


#print("La palabra secreta es: ",aleatorio, "\nNumero de letras: ",numletras,) #solo para saber que palabra es para las pruebas

#print(" - " * numletras) # Pintamos una linea por cada letra
intentos = 6; #los intentos maximos menos 1 para que entre a comprobar en su ultimo intento
aciertos = 1; #contador de aciertos para poder decir que saco la palabra
letras = list(aleatorio) #asi guardamos en letras todas las letras de la palabra aleatoria
#print (letras) #aqui estan todas las letras separadas
letras_adivinadas = ['_' for _ in letras]  # esta variable pone _ donde no tenga una letra adivinada, al principio pone todas _


while intentos >= 1: #Si le quedan intentos entra y mira si esta la letra o no
    print("Palabra actual:", ''.join(letras_adivinadas))  #pintamos con el join todo el contenido seguido de letras_adivinadas
    letra = input ("mete una letra: ").lower() #le pedimos que meta una letra para empezar a jugar, el lower es para que entienda siempre minusculas y no cuente error

    if letra in letras: #Si la letra que mete esta en lista de letras pone correcto 
         for i, l in enumerate(letras): #recorremos todas  las letras y metemos en la posicion i la letra si aparece
            if l == letra: #ahora vemos si la letra es igual a l y si es asi entra
                letras_adivinadas[i] = letra  # en las lineas pintadas, cambiamos la posicion i por la letra
                aciertos += 1 #sumamos un acierto
                #veces = letras.count(letra)  #para contar las veces que sale esa letra
                #posicion = letras.index(letra) #miramos la posicion donde esta esa letra
                #print(f"La letra '{letra}' está en la posición {posicion}.")
         print (''.join(letras_adivinadas)) #aqui pintamos lo que tiene letras adivinadas que ya tiene cambiados _ por letras
         letra = input ("CORRECTO!! mete otra letra: ").lower() #le pedimos que meta otra cuando acierte y le queden oportunidades
    if aciertos == numletras: #si aciertos tiene todas los num letras
            print("¡Felicidades! Has adivinado la palabra:",aleatorio,)
            break
       
    else:      
         intentos -= 1
         print(f"{letra} No esta, te quedan {intentos} intentos mas")
         print (''.join(letras_adivinadas)) #aqui pintamos lo que tiene letras adivinadas que ya tiene cambiados _ por letras
         letra = input ("mete una letra: ").lower() #le pedimos que meta cuando falle y le queden oportunidades

else: #si no quedan intentos pues sale del juego ya
    print("PERDISTE......La palabra que se escondia es: ",aleatorio,)  # Cuando tienes 6 fallos dice que perdiste


