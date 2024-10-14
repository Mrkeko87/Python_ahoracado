from random import * #para poder sacar aleatorios de la lista de nombres

#definimos las variables que vamos a usar:
palabras = ['perro', 'luz', 'cielo', 'programar'] #guardamos las palabras que queremos usar 
aleatorio = choice(palabras) #para sacar una palabra aleatioria de palabras
numletras = len(aleatorio)  # Contamos el número de letras en aleatorio
intentos = 6; #los intentos maximos menos 1 para que entre a comprobar en su ultimo intento
aciertos = 0; #contador de aciertos para poder decir que saco la palabra
letras = list(aleatorio) #asi guardamos en letras todas las letras de la palabra aleatoria
letras_adivinadas = ['_' for _ in letras]  # esta variable pone _ donde no tenga una letra adivinada, al principio pone todas _
letras_erroneas = [] #aqui vamos a meter la letras que no estan
letra_repetida = [] #aqui ponemos las letras que ya hemos metido para no repetir y que no cuenten como fallo ni como hacierto

#definimos los colores para hacer la salida mas visual
ROJO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"


#ahora pintamos el numero de letras que tiene la palabra, solo al iniciar el juego
print("La palabra tiene ",numletras, "letras")

#comenzamos el juego y no saldremos hasta encontrar un break
while intentos > 0: #Si le quedan intentos entra y mira si esta la letra o no
    print ( "Palabra actual:  "+ VERDE + "  ".join(letras_adivinadas) + RESET )  #pintamos con el join todo el contenido seguido de letras_adivinadas
    letra = input ("mete una letra: ").lower() #le pedimos que meta una letra para empezar a jugar, el lower es para que entienda siempre minusculas y no cuente error
   
   #con este if miramos si la letra ya se metio antes para que no le cuente el fallo ni el acierto
    if letra in letra_repetida:
        print ( ROJO + "" ,letra, "ya estaba, prueba con otra distinta\n" + RESET )
        continue #salta de nuevo al inicio del while
    #vamos a comprobar que solo nos mete letras
    if len(letra) != 1 or not letra.isalpha():
        print( ROJO + "ERROR!!!!Ni simbolos, ni numeros, ni varias letras \n" + RESET)
        continue #salta de nuevo al inicio del while
    
    if letra in letras: #Si la letra que mete esta en lista de letras pone correcto 
         for i, l in enumerate(letras): #recorremos todas  las letras y metemos en la posicion i la letra si aparece
            if l == letra: #ahora vemos si la letra es igual a l y si es asi entra
                letras_adivinadas[i] = letra  # en las lineas pintadas, cambiamos la posicion i por la letra
                letra_repetida.append(letra) #añadimos a lista letra repetida
                aciertos += 1 #sumamos un acierto
         print (VERDE +"¡¡CORRECTO!!\n" + RESET) #le pedimos que meta otra cuando acierte y le queden oportunidades

  
    else:      
         
         intentos -= 1
         if intentos == 0: #si intentos es 0 ya le dice que ha perdido
             print(ROJO + "PERDISTE......La palabra que se escondia es:",aleatorio,"" + RESET) 
             break   #para salir del bucle y terminar el juego
         
         letras_erroneas.append(letra) #añadimos la letra erronea en la lista
         letra_repetida.append(letra) #añadimos a lista letra repetida

         print(ROJO + f"{letra} No esta, te quedan {intentos} intentos mas\n" + RESET) #con la f ponemos los dos campos entre {}
         print ("LETRAS ERRONEAS: " + ROJO +" - ".join(letras_erroneas) + RESET) #con el mas te pinta todas las letras junto al join

   
    if aciertos == numletras: #si aciertos tiene todas los num letras gana y termina el juego
         print(VERDE + "¡Felicidades! Has adivinado la palabra:",aleatorio,"" + RESET)
         break   #para salir del bucle y terminar el juego
         