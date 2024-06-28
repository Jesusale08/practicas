def Repetir():
    while True:
        rep = input("\nDesea repetir programa? (y/n): ")
        if rep == "y":
            Run()
        elif rep == "n":
            print("\nGracias por usar el programa de Jesús Mundarain y Josue Barreno")
            break
        else:
            print("\nEscribe una opcion valida")

def Run():
    while True:
        opcion = input("\nMenu\n\n1.Cifrado Cesar\n2.Cifrado Primo\n3.Stop\n\nOpcion: ")
        if opcion.isnumeric()==True:
            opcion = int(opcion)
            if opcion==1 or opcion==2:
                Opcion(opcion)
            elif opcion==3:
                break
            else:
                print("\nEscribe una opcion valida")
        else:
            print("\nEscribe un numero")

def Cifrado_cesar(numero):
    #variables
    abc="abcdefghijklmnopqrstuvwxyz"
    cifrar_ini=[]
    cifrar_num=[]
    cifrar_fin=[]
    cifrado=""

    #pedir la clave y saber que es un numero
    while True:
        clave = input("\nEscribe la clave:")
        if clave.isnumeric()==True:
            clave = int(clave)
            break
        else:
            print("\nError, define la clave correctamente")

    #Pedir la palabra a cifrar
    cifrar = input("\nEscriba la palabra a cifrar: ")
    cifrar = cifrar.lower()

    #Poner en una lista los caracteres de una palabra o frase
    for i in range (len(cifrar)):
        cifrar_ini.append(cifrar[i])

    #Condicional por el "numero". Si es numero 1,  cifra al encontrar el indice en abc, de los caracteres cifrar_ini y sumando la clave
    #Condicional por el "numero". Si es numero 2,  cifra al encontrar el indice en abc, de los caracteres cifrar_ini y restando la clave
    for i in range (len(cifrar)):
        try:
            if numero == 1:
                cifrar_num.append(abc.index(cifrar_ini[i])+clave)
            elif numero == 2:
                cifrar_num.append(abc.index(cifrar_ini[i])-clave)
        except ValueError:
            cifrar_num.append(cifrar_ini[i])

    #cifrar_num es una lista de indices. Por lo tanto podemos encontrar la palabra cifrada/descifrada buscando la letra en abc[indice]
    #p.d.: Algunos indices estan fuera del rango. Se acomoda haciendo modulo de la longitud de abc
    for i in range(len(cifrar)):
        try:
            cifrar_fin.append(abc[(cifrar_num[i])%len(abc)])
        except ValueError:
            cifrar_fin.append(cifrar_num[i])
        except TypeError:
            cifrar_fin.append(cifrar_num[i])

    #Convertir una lista en un string
    for i in range(len(cifrar)):
        cifrado= cifrado + cifrar_fin[i]

    #Y bueno las impresiones para cada numero
    if numero==1:
        print(f"\nLa palabra cifrada es {cifrado}")
    else:
        print(f"\nLa palabra descifrada es {cifrado}")

def Cifrado_primo(numero):

    #Variables
    abc="abcdefghijklmnopqrstuvwxyz"
    primos=[]
    index = 0
    num=2

    #creacion de la lista primos
    while index < (len(abc)):
        cont=0
        for i in range (2,num):
            if num%i==0:
                cont=cont+1
            if cont>1:
                break
        if cont<1:
            primos.append(num)
            index+=1
        num+=1

    #Cifrando
    if numero == 1:
        while True:
            cont=0
            #Pidiendo los valores
            palabra = input("\nEscribe una palabra a cifrar: ")
            palabra = palabra.lower()
            #magic
            palabra=" "+palabra+" "
            cifrado=""
            for i in range (len(palabra)):
                cont+=1
                if palabra[i].isnumeric():
                    print("\nNo se permiten codificar numeros aqui")
                    break
                else:
                    try:
                        #palabra[i] me arrojara una letra que permitira que abc.index()  busque el indice de esa letra.
                        #Ese numero me ayudara a ubicar cual es el primo en la lista de primos en primos[].
                        # Por ultimo hay que convertirlo en string por que primos es una lista de numeros
                        cifrado=cifrado+str(primos[abc.index(palabra[i])])
                        #Agregando el guion
                        try:
                            #El contenido de palabra[] está modulado por que sale fuera del rango. Isinstance me
                            #determina si ese indice es un str. Si no es un str se agrega un guion
                            if not(isinstance((abc.index(palabra[(i+1)%(len(palabra))])),str)):
                                cifrado=cifrado+"-"
                        except ValueError:
                            pass
                    except ValueError:
                        cifrado=cifrado+palabra[i]
            if cont==len(palabra):
                break

        #Impresion Final
        print(f"\nLa palabra cifrada es {cifrado}")


    #Para Jesus y Josue la parte mas fastidiosa del codigo. Guiones y espacios
    else:
        #Variables
        descifrado_list=[]
        descifrado=""


        #Validar la palabra y Agarra la palabra y ponerlo en una lista
        while True:
            cont=0
            palabra_list=[]
            palabra = input("\nEscribe una palabra a descifrar: ")
            #magic
            palabra=" "+palabra+" "

            #Enlistamiento
            for i in range (len(palabra)):
                if (palabra[i].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric() and palabra[(i+2)%len(palabra)].isnumeric()):
                    palabra_list.append(palabra[i]+palabra[(i+1)%len(palabra)]+palabra[(i+2)%len(palabra)])
                elif (palabra[i-1].isnumeric() and palabra[(i)%len(palabra)].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric()):
                    pass
                elif (palabra[i-2].isnumeric() and palabra[(i-1)%len(palabra)].isnumeric() and palabra[(i)%len(palabra)].isnumeric()):
                    pass
                elif (palabra[i].isnumeric() and palabra[(i+1)%len(palabra)].isnumeric()):
                    palabra_list.append(palabra[i]+palabra[(i+1)%len(palabra)])
                elif (palabra[i].isnumeric() and palabra[(i-1)%len(palabra)].isnumeric()):
                    pass
                else:
                    palabra_list.append(palabra[i])

            #Verificacion
            for i in range (len(palabra_list)):
                cont+=1
                if palabra_list[i].isnumeric():
                    try:
                        if primos.index(int(palabra_list[i])):
                            pass
                    except ValueError:
                        print("\nInvalido. Repite de nuevo")
                        break
                else:
                    try:
                        if abc.index(palabra_list[i]):
                            print("\nInvalido. Repite de nuevo")
                            break
                    except ValueError:
                        pass
            
            #salida
            if cont == len(palabra_list):
                break

        #Buscando el indice y cambiarlo por letras
        for i in range (len(palabra_list)):
            try:
                if palabra_list[i].isnumeric():
                    descifrado_list.append(abc[primos.index(int(palabra_list[i]))])
                else:
                    descifrado_list.append(palabra_list[i])
            except ValueError:
                descifrado_list.append(palabra_list[i])

        #Convertir una lista en un string
        for i in range(len(palabra_list)):
            if palabra_list[i]!="-":
                descifrado= descifrado + descifrado_list[i]

        #Impresion final
        print(f"\nLa palabra descifrada es {descifrado}")

def Opcion(numero):
    opcion = input("\nMenu\n\n1.Cifrar\n2.Descifrar\n3.Stop\n\nOpcion: ")
    if opcion.isnumeric()==True:
        opcion = int(opcion)
        if numero==1 and (opcion==1 or opcion==2):
            Cifrado_cesar(opcion)
        elif numero==2 and (opcion==1 or opcion==2):
            Cifrado_primo(opcion)
        elif opcion==3:
            pass
        else:
            print("\nEscribe una opcion valida")
            Opcion(numero)

#Empieza el programa aqui
#Mostrando Bienvenida
print("\nBienvenidos a Practica 5 ó 6\nSeccion 2 Programacion\nGrupo 3\nJesús Noguera y Josue Barreno\n")
print("Este programa hace cifrados cesar y cifrado por primos")
Run()
Repetir()
