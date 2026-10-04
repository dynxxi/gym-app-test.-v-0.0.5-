ejercicios = [{"ejercicio": "sentadilla", "descripcion": "ejercicio de piernas"},
               {"ejercicio": "press de banca", "descripcion": "ejercicio para pechito"},
            {"ejercicio": "press militar", "descripcion": "ejercicio para hombrito"}]

def menu_principal():
    while True:
        elegir = input("\n Usuario, ¿A donde desea ir?.-"
    "\n - 1 : Quiero ver todos los ejercicios disponibles"
    "\n - 2 : Quiero agregar un ejercicio propio"
    "\n - 3 : Quiero buscar un ejercicio especifico "
    "\n - 4 : Quiero borrar un ejercicio especifico"
    "\n - 5 : Quiero salir del programa"
    "\n - Opción: ").strip().lower()

        if elegir == '1':
            check_ejercicios()
        elif elegir == '2':
            agregar_ejercicios_0_2()  
        elif elegir == '3':
            busqueda_ejercicio() 
        elif elegir == '4':
            borrar_ejercicio()
        elif elegir == '5':
            return f'\n Hasta la proxima...'
        else: 
            print('\n Respuesta Invalida, Intente otra vez...')

def check_ejercicios():
    if not ejercicios:
        print(f'\n Actualmente no hay ejercicios dentro de la lista, cree un ejercicio en el menu principal si desea visualizar algun ejercicio.')
    else:
        for numero, ejercicio1 in enumerate(ejercicios, start=1):
            if ejercicio1.get("ejercicio"):
                    print (f' \n {numero} . {ejercicio1["ejercicio"]} - Descripcion: {ejercicio1["descripcion"]}')
        input('\n Presione cualquier tecla para volver al menu principal: ').strip().lower()
        return
    
            
            

def busqueda_ejercicio():
    while True:
        pregunta = input('\n ¿Qué ejercicio desea buscar? (Escriba "Salir" para salir): ').lower().strip()
        encontrado = False
        if pregunta == 'salir':
            print(f'Volviendo al menu principal...')
            return
        else:
            for numero, ejercicio1 in enumerate (ejercicios, start=1):
                if ejercicio1.get("ejercicio") == pregunta:
                    print (f' \n {numero} . Ejercicio : {ejercicio1["ejercicio"]} \n Descripción: {ejercicio1["descripcion"]}')
                    encontrado = True
                    break
            if not encontrado:
                    error_1 = input('\n El ejercicio que usted esta buscando no se encontró. \n (Escriba "Salir" si quiere ir al menu principal): ').lower().strip()
                    print(error_1)
                    if error_1 == 'salir':
                        print (f'\n Volviendo al menu principal . . .')
                        return
                    else:
                        print('\n ERROR 001, Reintentando . . .')
                        continue
                        

def agregar_ejercicios_0_2():
    while True:
        ejercicio1 = input('\n ¿Cual es el nombre que desea ponerle a su ejercicio?: ').lower()
        if ejercicio1 == '':
            print('\n Respuesta invalida')
        else:
            descripcion = input('\n ¿Cual es la descripcion que desea agregarle a este objeto?: ').strip().lower()
            ejercicios.append({
            "ejercicio": ejercicio1,
             "descripcion": descripcion
            })
            print(f'\n ¡Listo, tu ejercicio {ejercicio1} se agrego correctamente en la ultima seccion de la lista!, ¡miralo!')
            for numero, ejercicio1 in enumerate (ejercicios, start=1):
                print (f'\n {numero}. {ejercicio1["ejercicio"]} / Descripcion: {ejercicio1["descripcion"]}')
            pregunta = input('\n ¿Desea volver al menu (Salir) o desea termina la sesión (End)?: ').lower().strip()
            if pregunta == 'salir':
                print (f'\n Volviendo al menu principal...')
                return       
            elif pregunta == 'end':
                print (f'\n Hasta la proxima...')
                return 
            else:
                print ('\n Intentelo nuevamente')
                return

def borrar_ejercicio():
    while True:
        pregunta1 = input('\n¿Qué ejercicio desea eliminar?: ')
        encontrado = False
        if pregunta1 == '':
            print(f' \nTu respuesta {pregunta1} es invalida... \nReintentando')
        else:
            for ejercicio1 in (ejercicios):
                if ejercicio1.get("ejercicio") == pregunta1:
                    ejercicios.remove(ejercicio1)
                    print(f'\n¡El ejercicio {pregunta1} ha sido eliminado con exito!')
                    encontrado = True
                    pregunta3 = input(f'\n ¿Desea eliminar otro ejercicio o desea salir al menu principal? \nEscribe "salir" para salir o "buscar" para buscar otro: ').lower().strip()
                    if pregunta3 == 'salir':
                           return
                    elif pregunta3 == 'buscar':
                           print('Reintentando...')
                           continue
                    else:
                           print('Introduzca una respuesta valida...')
                           
            if not encontrado:
                pregunta2 = input(f'\nEste ejercicio no ha sido encontrado en la lista. \n¿Desea buscar otro o salir?. \nEscribe "salir" para salir o "buscar" para buscar otro: ').lower().strip()
                if pregunta2 == 'buscar':
                    print('Reintentando...')
                elif pregunta2 == 'salir':
                    return
                else:
                    print('\n Ingrese una respuesta correcta')
menu_principal()

# ESP - este codigo esta actualmente en su version 0.0.7, se resolvieron errores ocultos en el codigo y se agrego una nueva funcionalidad... BORRAR EJERCICIO, ahora puedes borrar un ejercicio que se encuentre dentro de la lista.
# la version 0.0.8 se van optimizar las funciones si es que se pueden, si no, se dejara asi y simplemente para la 0.1.0 agregara cosas nuevas, pero eso pasara en el futuro...

# ENG - this code is in 0.0.7 version actually, i resolved hidden errors in the code and... y added a new fuction... DELETE EXERCISES, now you can delete a exercise who was in the list.
# the 0.0.8 will optmize the fuctions if they can, if not, i let them as they are and i'll just add more things in the 0.1.0 version, but that will happen in the future....
