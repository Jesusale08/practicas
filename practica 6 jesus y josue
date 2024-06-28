def repetir():
    while True:
        rep = input("Desea repiter programa? (y/n):")
        if rep == "y":
            run()
        elif rep == "n":
            break
        else:
            print("Escribe una opcion valida")

def run():
    #Declaro la variable 
    abc = "abcdefghijklmnopqrstuvwxyz"

    while True:
        opcion = input("\nMenu\n\n1.cifrado Cesar\n2.Cifrado Primo\n3.stop\n\nOpcion:")
        if opcion.isnumeric()==True:
            opcion = int(opcion)
            if opcion==1:
                opcion_cesar()
            elif opcion==2:
                opcion_primo()
            elif opcion==3:
                break
            else:
                print("escribe una opcion valida")
        else:
            print("escribe un numero")

def cifrado_cesar(numero):
    list="abcdefghijklmnopqrstuvwxyz"
    #pedir la clave y saber que es un numero
    while True:
        clave = input("escribe la clave:")
        if clave.isnumeric()==True:
            clave = int(clave)
            break
        else:
            print("error, define la clave correctamente")

    cifrar = input("escriba la plabra a cifrar:")
    cifrar = cifrar.lower()
    cifrar_ini=[]
    cifrar_num=[]
    cifrar_fin=[]

    for i in range (len(cifrar)):
        cifrar_ini.append(cifrar[i])

    if numero == 1:
        for i in range (len(cifrar)):
            cifrar_num.append(list.index(cifrar_ini[i])+clave)
    else:
        for i in range(len(cifrar)):
            cifrar_num.append(list.index(cifrar_ini[i])-clave)

    for i in range(len(cifrar)):
        cifrar_fin.append(list[(cifrar_num[i])%len(list)])
    
    cifrado=""
    for i in range(len(cifrar)):
        cifrado= cifrado + cifrar_fin[i]
    if numero==1:
        print(f"\nLa palabra cifrada es {cifrado}")
    else:
        print(f"\nLa palabra descifrada es {cifrado}")
    
def cifrado_primo(numero):
    abc="abcdefghijklmnopqrstuvwxyz"
    list=[]
    while True:
        clave = input("escribe la clave:")
        if clave.isnumeric()==True:
            clave = int(clave)
            break
        else:
            print("error, define la clave correctamente")

def opcion_cesar():
    while True:
        opcion = input("\nMenu\n\n1.Cifrar\n2.Descifrar\n3.stop\n\nOpcion:")
        if opcion.isnumeric()==True:
            opcion = int(opcion)
        if opcion==1:
            cifrado_cesar(1)
        elif opcion==2:
            cifrado_cesar(2)
        elif opcion==3:
            break
        else:
            print("escribe una opcion valida")

def opcion_primo():
   while True:
        opcion = input("\nMenu\n\n1.Cifrar\n2.Descifrar\n3.stop\n\nOpcion:")
        if opcion.isnumeric()==True:
            opcion = int(opcion)
        if opcion==1:
            cifrado_primo(1)
        elif opcion==2:
            cifrado_primo(2)
        elif opcion==3:
            break
        else:
            print("escribe una opcion valida")

#Empieza el programa aqui
run()
repetir()
