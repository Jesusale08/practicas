'PRACTICA 4 BRANDON GAITAN Y JESUS NOGUERA'
Menu=[]
while True:
    print("--- Lista de compras ---"+"\n"+"1. Agregar articulo"+"\n"+"2. Eliminar articulo"+"\n"+"3. Mostrar la lista completa"+"\n"+"4. Salir del programa")
    eleccion=int(input("Inserte el numero de su elección : "))
    if eleccion==1:
        eleccion=input("ingrese el nombre del articulo Deseado: ")
        Menu.append(eleccion)
    elif eleccion==2:
            articulo_a_eliminar=input("Ingrese el articulo que desea eliminar: ")
            if articulo_a_eliminar in Menu:
                Menu=[]
            else:
                print("el articulo no esta agregado si desea puede agregarlo")
    elif eleccion==3:
        if not Menu:
            print("la lista esta vacia")
        else:
            print("-- Lista de compras --")
            for eleccion in Menu:
                print(f"- {eleccion}")
    elif eleccion==4:
        print("usted a salido del programa para volver a usarlo por favor , dele inicio")
        break
    else:
        print(" Opción no Valida")