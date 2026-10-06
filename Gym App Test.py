import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

ejercicios = [{"ejercicio": "sentadilla", "descripcion": "ejercicio de piernas"},
               {"ejercicio": "press de banca", "descripcion": "ejercicio para pechito"},
            {"ejercicio": "press militar", "descripcion": "ejercicio para hombrito"}]

ejercicios_set = {'sentadilla', 'press de banca', 'press militar'}

def seleccionado(event):
    if not lista.curselection():
       return
    
    descripcion = tk.Toplevel(app, f'Descripcion: {descripcion_ejercicio}')
    descripcion(event.x_root, event.y_root)
    lista.bind("<Button-1>", mostrar_menu)

    

def borrar_seleccionado():
    if not lista.curselection():
        return
    indice = lista.curselection()[0]
    nombre = lista.get(indice).lower()

    ejercicios_set.discard(nombre)
    for ejerx in ejercicios:
        if ejerx.get("ejercicio") == nombre:
          ejercicios.remove(ejerx)
          break
    lista.delete(0, tk.END)
    for item in ejercicios:
        lista.insert(tk.END, item["ejercicio"])

    messagebox.showinfo("¡Listo!,", f"El ejercicio '{nombre}' fue eliminado.")

def mostrar_menu(event):
    if not lista.curselection():
        return
    menu_contextual = tk.Menu(app, tearoff=0)
    menu_contextual.add_command(label="Borrar", command=borrar_seleccionado)
    
    menu_contextual.post(event.x_root, event.y_root)

    lista.bind("<Button-3>", mostrar_menu)

def agregar_ejercicios_0_2_gui():
    nombre = var_nombre.get().strip().lower()
    descripcion = var_descripcion.get().strip().lower()
    if nombre == '' or descripcion == '':
        messagebox.showwarning("Campos Vacios", "Porfavor, llene los campos")
        return
    if nombre in ejercicios_set:
        messagebox.showerror("Error", "Este nombre ya esta siendo ocupado por otro ejercicio")
        return
    else:
         ejercicios.append({
              "ejercicio": nombre,
              "descripcion": descripcion
         })
         ejercicios_set.add(nombre)

    lista.delete(0, tk.END)
    for item in ejercicios:
         lista.insert(tk.END, item["ejercicio"])
    var_nombre.set("")
    var_descripcion.set("")

    messagebox.showinfo("¡Listo!", f"El ejercicio {nombre} ha sido creado exitosamente.")


def seleccionado(event):
    if not lista.curselection():
        return
    indice = lista.curselection()
    nombre_seleccionado = lista.get(indice).lower()
    for item in ejercicios:
        if item["ejercicio"] == nombre_seleccionado:
            label_descripcion.config(text=f"DESCRIPCION: {item['descripcion']}")
            break


app = tk.Tk()
#Anchura x Altura
app.geometry("360x800")
app.config(background='black')
app.config(bg="#2b2b2b")

var_nombre = tk.StringVar(app)
var_descripcion = tk.StringVar(app)



tk.Wm.wm_title(app, "Gym App")

titulo = tk.Label(app, text="GYM APP 0.1.0", font=("Helvetica", 14, "bold"))
titulo.place(x=0, y=0, width=154, height=44)


lista = tk.Listbox(app, selectmode="browse", font=("Helvetica", 12, "bold"), borderwidth=1.5)
lista.place(x=12, y=81, width=324, height=143)


label_ejercicios = tk.Label(app, text="EJERCICIOS:", font=("Helvetica", 10, "bold"))
label_ejercicios.place(x=14, y=54, width=92, height=16)

label_descripcion = tk.Label(app, text="Seleccione un ejercicio para ver su descripcion", wraplength= 300, borderwidth=1.5)
label_descripcion.place(x=28,y=270, width=300, height=20 , relheight= 0.2)

caja_descripcion = tk.Entry(app, textvariable=var_descripcion ,borderwidth=1.5)
caja_descripcion.place(x=200, y=648, width=150, height=28)


caja_nombre = tk.Entry(app, textvariable=var_nombre)
caja_nombre.place(x=200, y=578, width=150, height=28)


nombre_ejercicio_label = tk.Label(app, text="Nombre", font=("Helvetica", 10, "bold"), borderwidth=1.5)
nombre_ejercicio_label.place(x=230, y=550, width=90, height=26)


descripcion_ejercicio_label = tk.Label(app, text="Descripcion", font=("Helvetica", 10, "bold"), borderwidth=1.5)
descripcion_ejercicio_label.place(x=230, y=620, width=90, height=26)


label_ejercicio_guardar2 = tk.Label(app, text="Agregar \nejercicio", fg="#f8230b", font=("Helvetica", 14, "bold"), borderwidth=1.5)
label_ejercicio_guardar2.place(x=225, y=480, width=100, height=60)


boton_guardar_ejercicio = tk.Button(app, text="Guardar", command=agregar_ejercicios_0_2_gui, borderwidth=1.5)
boton_guardar_ejercicio.place(x=215, y=694, width=120, height=30)




app.resizable(False,False)

for item in ejercicios:
    nombre_ejercicio = item['ejercicio']
    descripcion_ejercicio = item['descripcion']
    lista.insert(tk.END, item["ejercicio"]) 
    

lista.bind("<Button-3>", mostrar_menu)
lista.bind("<<ListboxSelect>>", seleccionado)

app.mainloop()




#lista.bind("<<ListboxSelect>>", seleccionado)
#tk.Button(app,text='Elegir',font=("Courier", 10),bg= "#FF0000",fg= "#FDFDFD",command= menu_principal)




# ESP - este codigo esta actualmente en su version 0.0.8.5, arregle algunos bugs con la implementacion de las sets en forma de listas y optimice el codigo con sets, para eliminar y crear ejercicios mas rapido.
# la version 0.0.9 se van optimizar las funciones si es que se pueden, si no, se dejara asi y simplemente para la 0.1.0 agregara cosas nuevas, pero eso pasara en el futuro...

# ENG - this code is in 0.0.8 version actually, i fixed some bugs with the new sets list add and optimized the code with sets, to make and delete the exercises faster.
# the 0.0.9 will optmize the fuctions if they can, if not, i let them as they are and i'll just add more things in the 0.1.0 version, but that will happen in the future....
