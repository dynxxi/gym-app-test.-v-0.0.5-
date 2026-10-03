ejercicios = [{"ejercicio": "sentadilla", "descripcion": "ejercicio de piernas"},
               {"ejercicio": "press de banca", "descripcion": "ejercicio para pechito"},
            {"ejercicio": "press militar", "descripcion": "ejercicio para hombrito"}]

def menu_principal():
    while True:
        elegir = input("\n Usuario, ¿A donde desea ir?.-"
    "\n - 1 : Quiero ver todos los ejercicios disponibles"
    "\n - 2 : Quiero agregar un ejercicio propio"
    "\n - 3 : Quiero buscar un ejercicio en especifico "
    "\n - 4 : Quiero salir del programa"
    "\n - Opción: ").strip().lower()

        if elegir == '1':
            check_ejercicios()
        elif elegir == '2':
            agregar_ejercicios_0_2()  
        elif elegir == '3':
            busqueda_ejercicio() 
        elif elegir == '4':
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
        ejercicio = input('\n ¿Cual es el nombre que desea ponerle a su ejercicio?: ').lower()
        if ejercicio == '':
            print('\n Respuesta invalida')
        else:
            descripcion = input('\n ¿Cual es la descripcion que desea agregarle a este objeto?: ').strip().lower()
            ejercicios.append({
            "ejercicio": ejercicio,
             "descripcion": descripcion
            })
            print(f'\n ¡Listo, tu ejercicio {ejercicio} se agrego correctamente en la ultima seccion de la lista!, ¡miralo!')
            for numero, ejercicio in enumerate (ejercicios, start=1):
                print (f'\n {numero}. {ejercicio["ejercicio"]} / Descripcion: {ejercicio["descripcion"]}')
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
menu_principal()

# ESP - este codigo esta actualmente en su version 0.0.6, resolvi errores que provocaban que fuera dificil de leer las indicaciones o las respuestas en el terminal, ademas de agregar otras funciones adicionales.
# la version 0.0.7 se van optimizar las funciones si es que se pueden, si no, se dejara asi y simplemente para la 0.1.0 agregara cosas nuevas, pero eso pasara en el futuro...

# ENG - this code is in 0.0.6 version actually, i resolved some errors who make dificult read the answers or the indicators in the terminal, and i added others additionals fuctions.
# the 0.0.7 will optmize the fuctions if they can, if not, i let them as they are and i'll just add more things in the 0.1.0 version, but that will happen in the future....
