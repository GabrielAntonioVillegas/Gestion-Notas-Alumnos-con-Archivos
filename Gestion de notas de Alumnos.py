from   tkinter   import *
from   tkinter   import ttk
from   tkinter   import messagebox
from   functools import partial
from   tkinter   import PhotoImage
from   tkinter   import font
import random
import time

def volver_ventana_menu(menu1):
    menu1.destroy()
#Ventana Menu Alumnos=========================================================================================================================
def ventana_menu_alumnos(app0):
    menu1 = Toplevel(app0)
    menu1.title('Menu de Alumnos')
    menu1.geometry('600x300+0+350')
    menu1.configure(background='gainsboro')

    alta = Button(menu1, text='ALTA DATOS',borderwidth=4, command=partial(ventana_alumnos, menu1))
    alta.place(x= 60,  y= 100, height= 50, width= 110)

    baja = Button(menu1, text='BAJA DATOS', borderwidth=4,command=partial(ventana_baja_alumnos, menu1))
    baja.place(x=190, y=100, height=50, width=110)

    modificacion= Button(menu1, text='MODIFICACION', command=partial(ventana_modificar_alumnos, menu1), borderwidth=4)
    modificacion.place(x=320, y=100, height=50, width= 110)

    listado = Button(menu1, text='LISTADO', borderwidth=4, command=partial(ventana_listar_alumnos, menu1))
    listado.place(x=450, y= 100, height=50, width=110)

    
    volver= Button(menu1, text='VOLVER', borderwidth=4, command=partial(volver_ventana_menu, menu1))
    volver.place(x=255, y= 200, height= 50, width= 110)
#=======================================
def alta_datos(datos_alum, dni_entry, ape_entry, nom_entry, email_entry, cur_entry, div_entry, cont):

    llenar_vector_alumnos(datos_alum, dni_entry, ape_entry, nom_entry, email_entry, cur_entry, div_entry, cont)
    
    archi_alum= open('alumnos.dat', 'a', encoding='utf-8')
    for n in range(7):
        if(n < 6):
            archi_alum.write(str(datos_alum[n]) + ', ')
        else:
            archi_alum.write(str(datos_alum[n]) + '\n')

    datos_alum.clear()
    archi_alum.close()
#Funcion Validar Gmail==================
def validar_gmail(email_entry):
    aux =''
    aux = email_entry.get()
    cont=0
    for n in range(len(aux)):
        if(aux[n] == '@'):
            cont+=1
    for z in range(len(aux)):
        if(aux[z] == '.'):
            cont+=1
                        
    if(cont == 2):
        return(True)
    else:
        return(False)
#Funcion LLenar Vector de Alumnos=======       
def llenar_vector_alumnos(datos_alum, dni_entry, ape_entry, nom_entry, email_entry,curso_combo, divi_combo, cont):

    contador = open('contador.dat', 'r', encoding='utf-8')
    launux = contador.readline()
    contador.close()
    if(launux == ''):
        contador = open('contador.dat', 'a', encoding='utf-8')
        contador.write(str(0))

    contador.close()
    

    if(len(dni_entry.get()) > 0 and len(dni_entry.get()) < 9 and len(ape_entry.get()) > 0 and len(nom_entry.get()) > 0 and
       len(email_entry.get()) > 0 and curso_combo.get() != '' and divi_combo.get() != '' and validar_gmail(email_entry)):
        
        contador = open('contador.dat', 'r', encoding='utf-8')
        linea = contador.read()
        cont = int(linea)+1
        contador.close()

        datos_alum.append(cont)

        datos_alum.append(dni_entry.get())
        dni_entry.delete(0, END)
        dni_entry.focus_set()

        datos_alum.append(ape_entry.get())
        ape_entry.delete(0, END)

        datos_alum.append(nom_entry.get())
        nom_entry.delete(0, END)

        datos_alum.append(email_entry.get())
        email_entry.delete(0, END)

        datos_alum.append(curso_combo.get())
        curso_combo.delete(0,END)

        datos_alum.append(divi_combo.get())
        divi_combo.delete(0,END)

        
    elif(len(dni_entry.get()) > 8 ):
        messagebox.showerror(title='Dni no valido', message= 'Usted ingresó un numero de Dni no valido')

    elif(not validar_gmail(email_entry)):
        messagebox.showerror(title='Mail no valido',
                             message='Por favor, ingrese un mail con los caracteres validos')
    else:
        messagebox.showerror(title='Datos no completados',
                             message='Por favor llene todas las casillas con datos correspondientes')

    archi_cont= open('contador.dat', 'w', encoding='utf-8')
    archi_cont.write(str(cont))
    archi_cont.close()     
#Funcion Volver Ventana Alta Alumnos====
def volver_ventana_alta(app1):
    app1.destroy()
#Funcion Creacion de la ventana alumnos=
def ventana_alumnos(menu1):
    app1 = Toplevel(menu1)
    app1.title('Alumnos')
    app1.geometry('500x500+650+0')
    app1.configure(background='gainsboro')

    #Labels=================================
    dni_lbl= Label(app1, text='Dni: ',     background='gainsboro')
    dni_lbl.place(x = 100, y = 50)
    
    ape_lbl= Label(app1, text='Apellido: ',background='gainsboro')
    ape_lbl.place(x = 100, y = 100)

    nom_lbl= Label(app1, text='Nombre: ',  background='gainsboro')
    nom_lbl.place(x = 100, y = 150)

    email_lbl= Label(app1, text='Email: ', background='gainsboro')
    email_lbl.place(x = 100, y = 200)

    cur_lbl= Label(app1, text='Curso: ',   background='gainsboro')
    cur_lbl.place(x = 100, y = 250)

    div_lbl= Label(app1, text='Division: ',background='gainsboro')
    div_lbl.place(x = 100, y = 300)

    #Entrys=================================
    
    dni_entry= Entry(app1, width = 15)
    dni_entry.place(x = 200, y = 50)
    
    ape_entry= Entry(app1, width = 30)
    ape_entry.place(x = 200, y = 100)

    nom_entry= Entry(app1, width = 30)
    nom_entry.place(x = 200, y = 150)

    email_entry= Entry(app1, width = 30)
    email_entry.place(x = 200, y = 200)
    
    #ComboBox===============================
    vec_curso = ['', '1', '2', '3','4','5','6']

    vec_div   = ['', '1', '2', '3','4','5']

    curso_combo= ttk.Combobox(app1, exportselect = True)
    curso_combo.place(x = 200, y=250)

    divi_combo = ttk.Combobox(app1, exportselect = True )
    divi_combo.place(x = 200, y = 300)
    
    curso_combo['values'] = vec_curso

    divi_combo['values'] = vec_div
    
    #Alta===================================
    datos_alum=[]
    cont= int(0)

    agregar_dat = Button(app1, text= 'Agregar Datos',borderwidth=4,
                      command=partial(alta_datos,datos_alum,  dni_entry, ape_entry, nom_entry, email_entry,curso_combo, divi_combo, cont))
    
    agregar_dat.place(x = 185, y = 350, height= 50, width= 125)

    volver = Button(app1, text='VOLVER', borderwidth=4, command=partial(volver_ventana_alta, app1))
    volver.place(x= 185, y= 430, height=50, width=125)
#Funcion Baja Datos Alumnos=============
def baja_datos_alumnos(bajon_ent):
    bajon = bajon_ent.get()
    bajon_ent.delete(0, END)
    bajon_ent.focus_set()
    
    datos_real = open('alumnos.dat', 'r', encoding='utf-8')
    datos_temp = open('alumnos_temp.dat', 'w', encoding='utf-8')
    
    linita = datos_real.readline()
    c = int(0)
    
    while(linita != ''):
        aux = linita.split(', ',7) 
        if(bajon != aux[0]):
            datos_temp.write(linita)
        else:
            messagebox.showinfo(title='Baja de Datos', message= 'Se eliminó el dato con exito')
        linita = datos_real.readline()

    datos_real.close()
    datos_temp.close()
    
    datos_real = open('alumnos.dat', 'w', encoding='utf-8')
    datos_temp = open('alumnos_temp.dat', 'r', encoding='utf-8')
    
    linita = datos_temp.readline()
    while(linita != ''):
        datos_real.write(linita)
        linita = datos_temp.readline()
    datos_real.close()
    datos_temp.close()

    datos_temp= open('alumnos_temp.dat', 'w', encoding='utf-8')
    datos_temp.close()
#Funcion Cerrrar Ventana Baja Alumnos===
def volver_ventana_baja(app1_1):
    app1_1.destroy()
#Funcion Creacion Ventana Baja Alumnos==
def ventana_baja_alumnos(menu1):
    app1_1= Toplevel(menu1)
    app1_1.geometry('500x400+650+0')
    app1_1.title('Baja de Datos')
    app1_1.configure(background='gainsboro')

    ingrese= Label(app1_1,text='Ingrese la ID del dato que quiere borrar', background='gainsboro')
    ingrese.place(x=150,y=100)

    bajon_ent = Entry(app1_1,width=30)
    bajon_ent.place(x= 160, y= 150)
    
    volver= Button(app1_1, text='VOLVER', command=partial(volver_ventana_baja, app1_1), borderwidth=4)
    volver.place(x=200, y=300, height=50, width=100)
    
    bajar= Button(app1_1, text='BORRAR', borderwidth=4, command=partial(baja_datos_alumnos, bajon_ent))
    bajar.place(x=200, y=200, height=50, width=100)
#Creacion Ventana Modificacion Alumnos==
def modificacion_alumnos(buscador_ent, dni_modi_ent, ape_modi_ent, nom_modi_ent, email_modi_ent,curso_combo_modi, divi_combo_modi, aviso_lbl):
    if(len(dni_modi_ent.get()) > 0 and len(ape_modi_ent.get()) > 0 and len(nom_modi_ent.get()) > 0 and len(email_modi_ent.get()) and len(curso_combo_modi.get()) != '' and len(divi_combo_modi.get()) != '' and validar_gmail(email_modi_ent)):

        dato = buscador_ent.get()
        alumnos = open('alumnos.dat', 'r', encoding='utf-8')
        temporal= open('alumnos_temp.dat', 'w',encoding='utf-8')

        linita=alumnos.readline()
        while(linita != ''):
            aux = linita.split(', ', 7)
            if(dato != aux[0]):
                temporal.write(linita)
            else:
                m_dni = dni_modi_ent.get()
                dni_modi_ent.delete(0, END)

                m_ape = ape_modi_ent.get()
                ape_modi_ent.delete(0, END)

                m_nom = nom_modi_ent.get()
                nom_modi_ent.delete(0, END)

                m_gml = email_modi_ent.get()
                email_modi_ent.delete(0, END)

                m_cur = curso_combo_modi.get()
                curso_combo_modi.delete(0, END)

                m_div = divi_combo_modi.get()
                divi_combo_modi.delete(0, END)

                buscador_ent.delete(0, END)


                lineaux=  ''
                lineaux = dato + ', ' + str(m_dni) + ', ' + str(m_ape) + ', ' + str(m_nom) + ', ' + str(m_gml) + ', ' + str(m_cur) + ', ' + str(m_div) + '\n'
                temporal.write(lineaux)
                messagebox.showinfo(title='Modificacion Exitosa', message='Se ha modificado el dato con exito')

            linita=alumnos.readline()

        alumnos.close()
        temporal.close()
    
        #========================================================
        alumnos = open('alumnos.dat', 'w', encoding='utf-8')
        temporal= open('alumnos_temp.dat','r', encoding='utf-8')

        nuevalinita= temporal.readline()
        while(nuevalinita != ''):
            alumnos.write(nuevalinita)
            nuevalinita=temporal.readline()
        
        alumnos.close()
        temporal.close()
    
        #========================================================
        temporal = open('alumnos_temp.dat','w', encoding='utf-8')
        temporal.close()
    else:
        messagebox.showerror(title='Incorrecto', message='Llene todos los datos')
#=======================================
def buscar_alumno(buscador_ent, dni_modi_ent, ape_modi_ent, nom_modi_ent, email_modi_ent,curso_combo_modi, divi_combo_modi, aviso_lbl):

    if(len(buscador_ent.get()) > 0):
        dato = buscador_ent.get()
        alumnos = open('alumnos.dat' , 'r', encoding='utf-8')
        linita = alumnos.readline()

        while(linita != ''):
            aux = linita.split(', ', 7)
            if(aux[0] == dato):
                aviso_lbl.configure(text='Se mostraran los datos del alumno que usted quiere buscar' + '\n' +
                                         'Modifique el dato que desee')
                dni_modi_ent.insert(0, aux[1])
                ape_modi_ent.insert(0, aux[2])
                nom_modi_ent.insert(0, aux[3])
                email_modi_ent.insert(0, aux[4])
                curso_combo_modi.insert(0, aux[5])
                divi_combo_modi.insert(0, aux[6][:-1])
            
            linita = alumnos.readline()
        alumnos.close()
    
    else:
        messagebox.showerror(title='Incorrecto', message='Ingrese una ID de alumno valida')
#=======================================
def volver_ventana_modificar_alumnos(app1_2):
    app1_2.destroy()
#=======================================
def ventana_modificar_alumnos(menu1):
    app1_2= Toplevel(menu1)
    app1_2.geometry('800x400+550+0')
    app1_2.title('Modificacion de Datos')
    app1_2.configure(background='gainsboro')
        #cont = int()
    #contador = open('contador.dat', 'r', encoding='utf-8')
    #numero = contador.read()
    #cont = int(numero)
    #contador.close()
    ingrese= Label(app1_2,text='Ingrese la ID del dato que quiere modificar', background='gainsboro')
    ingrese.place(x=90,y=100)

    buscador_ent = Entry(app1_2,width=30)
    buscador_ent.place(x= 110, y= 150)

    #Labels=================================
    dni_lbl= Label(app1_2, text='Dni: ',     background='gainsboro')
    dni_lbl.place(x = 450, y = 50)
    
    ape_lbl= Label(app1_2, text='Apellido: ',background='gainsboro')
    ape_lbl.place(x = 450, y = 100)

    nom_lbl= Label(app1_2, text='Nombre: ',  background='gainsboro')
    nom_lbl.place(x = 450, y = 150)

    email_lbl= Label(app1_2, text='Email: ', background='gainsboro')
    email_lbl.place(x = 450, y = 200)

    cur_lbl= Label(app1_2, text='Curso: ',   background='gainsboro')
    cur_lbl.place(x = 450, y = 250)

    div_lbl= Label(app1_2, text='Division: ',background='gainsboro')
    div_lbl.place(x = 450, y = 300)

    aviso_lbl = Label(app1_2, background='gainsboro')
    aviso_lbl.place(x=20, y=180, height='50', width='350')

    #Entrys=================================
    
    dni_modi_ent= Entry(app1_2, width = 15)
    dni_modi_ent.place(x = 520, y = 50)
    
    ape_modi_ent= Entry(app1_2, width = 30)
    ape_modi_ent.place(x = 520, y = 100)

    nom_modi_ent= Entry(app1_2, width = 30)
    nom_modi_ent.place(x = 520, y = 150)

    email_modi_ent= Entry(app1_2, width = 30)
    email_modi_ent.place(x = 520, y = 200)
    
    #ComboBox===============================
    vec_curso = ['', '1', '2', '3','4','5','6']

    vec_div   = ['', '1', '2', '3','4','5']

    separacion = Label(app1_2, background= 'gainsboro', relief= 'raised', borderwidth=5)
    separacion.place(x= 380, y= 0, width=30, height= 400)

    curso_combo_modi= ttk.Combobox(app1_2, exportselect = True)
    curso_combo_modi.place(x = 520, y=250)

    divi_combo_modi = ttk.Combobox(app1_2, exportselect = True )
    divi_combo_modi.place(x = 520, y = 300)
    
    curso_combo_modi['values'] = vec_curso

    divi_combo_modi['values'] = vec_div

    #Botones================================
    
    buscar= Button(app1_2, text='BUSCAR', 
                   command=partial(buscar_alumno,buscador_ent, dni_modi_ent, ape_modi_ent, nom_modi_ent, email_modi_ent,
                                                 curso_combo_modi, divi_combo_modi, aviso_lbl), borderwidth=4)

    buscar.place(x=150, y=250, height=50, width=100)

    modificar= Button(app1_2, text='MODIFICAR', 
                      command=partial(modificacion_alumnos,buscador_ent, dni_modi_ent, ape_modi_ent, 
                                                           nom_modi_ent, email_modi_ent,curso_combo_modi, divi_combo_modi, aviso_lbl),borderwidth=4)
    
    modificar.place(x=520, y=330, height=50, width=100)

    volver= Button(app1_2, text='VOLVER', command=partial(volver_ventana_modificar_alumnos, app1_2), borderwidth=4)
    volver.place(x=150, y=330, height=50, width=100)
#Funcion Cerrar ventana Listado Alumnos=
def volver_ventana_listado(app1_3):
    app1_3.destroy()
#Creacion Ventana Listado Alumnos=======
def ventana_listar_alumnos(menu1):
    app1_3= Toplevel(menu1)
    app1_3.geometry('920x500+430+0')
    app1_3.title('Listado de Alumnos')
    app1_3.configure(background='gainsboro')

    arbol_alum = ttk.Treeview(app1_3, columns=(1,2,3,4,5,6,7), show='headings',height='10')
    arbol_alum.heading(1, text='Id')
    arbol_alum.column(1, width=30)

    arbol_alum.heading(2, text='Dni')
    arbol_alum.column(2, width=100)

    arbol_alum.heading(3, text='Apellido')
    arbol_alum.column(3, width=150)

    arbol_alum.heading(4, text='Nombre')
    arbol_alum.column(4, width=150)

    arbol_alum.heading(5, text='Email')
    arbol_alum.column(5, width=250)

    arbol_alum.heading(6, text='Curso')
    arbol_alum.column(6, width=50)

    arbol_alum.heading(7, text='Division')
    arbol_alum.column(7, width=70)
    arbol_alum.place(x=65, y=100)
    
    alum = open('alumnos.dat', 'a', encoding='utf-8')
    alum.close()

    alum = open('alumnos.dat', 'r', encoding='utf-8')
    cad=''
    linea= alum.readline()
    while(linea != ''):
        aux=linea.split(', ', 7)
        cad= linea
        arbol_alum.insert('','end',values=aux)
        linea=alum.readline()
    alum.close()
    

    volver= Button(app1_3, text='VOLVER', command=partial(volver_ventana_listado, app1_3), borderwidth=4)
    volver.place(x=390, y=400, height=50, width=100)






#Ventana Notas===============================================================================================================================
def modificar_nota(buscadora_enti, id_alum_enti,id_mate_enti,nota1_enti,nota2_enti, nota3_enti, nota4_enti):
    datico = buscadora_enti.get()
    
    notas= open('notas.dat', 'r', encoding='utf-8')
    temporal=open('notas_temp.dat', 'w', encoding='utf-8')

    linosa = notas.readline()
    while(linosa != ''):
        aux = linosa.split(', ', 7)
        if(datico != aux[0]):
            temporal.write(linosa)
        else:
            i_alu = id_alum_enti.get()
            id_alum_enti.delete(0, END)

            i_mat = id_mate_enti.get()
            id_mate_enti.delete(0, END)

            m_not1= nota1_enti.get()
            nota1_enti.delete(0, END)

            m_not2 = nota2_enti.get()
            nota2_enti.delete(0, END)

            m_not3 = nota3_enti.get()
            nota3_enti.delete(0, END)

            m_not4 = nota4_enti.get()
            nota4_enti.delete(0, END)

            buscadora_enti.delete(0, END)

            lisaux = ''
            lisaux = datico + ', ' + str(i_alu) + ', ' + str(i_mat) + ', ' + str(m_not1) + ', ' + str(m_not2) + ', ' + str(m_not3) + ', ' + str(m_not4) + '\n'
            temporal.write(lisaux)
            messagebox.showinfo(title='Modificacion Exitosa', message='El dato se modifico con exito')

        linosa = notas.readline()

    notas.close()
    temporal.close()

    #============================
    notas = open('notas.dat', 'w', encoding='utf-8')
    temporal=open('notas_temp.dat', 'r', encoding='utf-8')

    nuevalinosa = temporal.readline()
    while(nuevalinosa != ''):
        notas.write(nuevalinosa)
        nuevalinosa = temporal.readline()
    
    notas.close()
    temporal.close()

    temporal=open('notas_temp.dat','w', encoding='utf-8')
    temporal.close()
#=======================================
def buscador_nota(buscadora_enti, id_alum_enti,id_mate_enti,nota1_enti,nota2_enti, nota3_enti, nota4_enti):
    if(len(buscadora_enti.get()) > 0):
        dat = buscadora_enti.get()

        nota = open('notas.dat', 'r', encoding='utf-8')
        liniardi = nota.readline()

        while(liniardi != ''):
            aux = liniardi.split(',', 7)
            if(aux[0] == dat):
                id_alum_enti.insert(0, aux[1])
                id_mate_enti.insert(0, aux[2])
                nota1_enti.insert(0,   aux[3])
                nota2_enti.insert(0,   aux[4])
                nota3_enti.insert(0,   aux[5])
                nota4_enti.insert(0,   aux[6])

            liniardi = nota.readline()
        nota.close()
    else:
        messagebox.showerror(title='Incorrecto', message='Ingrese una id de materia valida')
#=======================================
def volver_modificar_notas(app2_3):
    app2_3.destroy()
#=======================================
def ventana_modificar_notas(menu2):
    app2_3 = Toplevel(menu2)
    app2_3.geometry('800x400+550+0')
    app2_3.configure(background='gainsboro')

    #Labels===============================
    ingrese= Label(app2_3,text='Ingrese la ID del dato que quiere modificar', background='gainsboro')
    ingrese.place(x=90,y=100)

    separacion = Label(app2_3, background= 'gainsboro', relief= 'raised', borderwidth=5)
    separacion.place(x= 380, y= 0, width=30, height= 400)

    alumno = Label(app2_3, text='Id del Alumno: ', background='gainsboro')
    alumno.place(x= 450, y= 50)

    materia = Label(app2_3, text='Id de la Materia: ', background='gainsboro')
    materia.place(x= 450, y= 100)

    nota1 = Label(app2_3, text='Nota 1: ', background='gainsboro')
    nota1.place(x= 450, y= 150)

    nota2 = Label(app2_3, text='Nota 2: ', background='gainsboro')
    nota2.place(x=450, y=200)

    nota3 = Label(app2_3, text='Nota 3: ', background='gainsboro')
    nota3.place(x= 450, y=250)

    nota4 = Label(app2_3, text='Nota 4: ', background='gainsboro')
    nota4.place(x=450, y= 300)

    #Entrys==============================
    id_alum_enti = Entry(app2_3, width=15)
    id_alum_enti.place(x=550, y= 50)

    id_mate_enti = Entry(app2_3, width=15)
    id_mate_enti.place(x= 550, y= 100)

    nota1_enti = Entry(app2_3, width=15)
    nota1_enti.place(x= 550, y=150)

    nota2_enti = Entry(app2_3, width=15)
    nota2_enti.place(x= 550, y=200)

    nota3_enti = Entry(app2_3, width=15)
    nota3_enti.place(x= 550, y=250)

    nota4_enti = Entry(app2_3, width=15)
    nota4_enti.place(x= 550, y=300)

    buscadora_enti = Entry(app2_3,width=30)
    buscadora_enti.place(x= 110, y=150)

    #Buttons============================
    buscar= Button(app2_3, text='BUSCAR', 
    command=partial(buscador_nota,buscadora_enti, id_alum_enti,id_mate_enti,nota1_enti,nota2_enti, nota3_enti, nota4_enti), borderwidth=4)

    buscar.place(x=150, y=250, height=50, width=100)

    modificar= Button(app2_3, text='MODIFICAR', 
    command=partial(modificar_nota, buscadora_enti, id_alum_enti,id_mate_enti,nota1_enti,nota2_enti, nota3_enti, nota4_enti), borderwidth=4)
    modificar.place(x=548, y=330, height=50, width=100)

    volver= Button(app2_3, text='VOLVER', command=partial(volver_modificar_notas, app2_3), borderwidth=4)
    volver.place(x=150, y=330, height=50, width=100)
#=======================================
def baja_notas(bajon_enti):
    baja = bajon_enti.get()
    bajon_enti.delete(0, END)
    bajon_enti.focus_set()
    
    notas = open('notas.dat', 'r', encoding='utf-8')
    temporal= open('notas_temp.dat', 'w', encoding='utf-8')

    linita = notas.readline()

    while(linita != ''):
        aux= linita.split(', ', 7)
        if(baja != aux[0]):
            temporal.write(linita)
        else:
            messagebox.showinfo(title='Baja de Datos', message='Dato eliminado con exito')
        linita = notas.readline()

    notas.close()
    temporal.close()

    notas = open('notas.dat', 'w', encoding='utf-8')
    temporal=open('notas_temp.dat', 'r', encoding='utf-8')

    linear = temporal.readline()
    while(linear != ''):
        notas.write(linear)
        linear = temporal.readline()

    notas.close()
    temporal.close()

    temporal= open('notas_temp.dat', 'w', encoding='utf-8')
    temporal.close()
#=======================================
def volver_baja_notas(app2_2):
    app2_2.destroy()
#=======================================
def ventana_baja_notas(menu2):
    app2_2 = Toplevel(menu2)
    app2_2.geometry('500x400+650+0')
    app2_2.title('Baja Notas')
    app2_2.configure(background='gainsboro')

    ingrese= Label(app2_2,text='Ingrese la ID del dato que quiere borrar', background='gainsboro')
    ingrese.place(x=150,y=100)

    bajon_enti = Entry(app2_2,width=30)
    bajon_enti.place(x= 160, y= 150)
    
    volver= Button(app2_2, text='VOLVER', command=partial(volver_baja_notas, app2_2), borderwidth=4)
    volver.place(x=200, y=300, height=50, width=100)
    
    bajar= Button(app2_2, text='BORRAR',command=partial(baja_notas, bajon_enti), borderwidth=4)
    bajar.place(x=200, y=200, height=50, width=100)
#=======================================
def volver_ventana_listado_notas(app2_1):
    app2_1.destroy()
#=======================================
def listado_notas(menu2):
    app2_1 = Toplevel(menu2)
    app2_1.geometry('630x400+650+0')
    app2_1.title('Listado Notas')
    app2_1.configure(background='gainsboro')

    arbol_notas = ttk.Treeview(app2_1, columns=(1,2,3,4,5,6,7), show='headings', height='10')
    arbol_notas.heading(1, text='Id Nota')
    arbol_notas.column(1, width=70)

    arbol_notas.heading(2, text='Id Alumno')
    arbol_notas.column(2, width=70)

    arbol_notas.heading(3, text='Id Materia')
    arbol_notas.column(3, width=70)

    arbol_notas.heading(4, text='Nota 1')
    arbol_notas.column(4, width=70)

    arbol_notas.heading(5, text='Nota 2')
    arbol_notas.column(5, width=70)

    arbol_notas.heading(6, text='Nota 3')
    arbol_notas.column(6, width=70)

    arbol_notas.heading(7, text='Nota 4')
    arbol_notas.column(7, width=70)

    arbol_notas.place(x=70, y=100)

    #====================================
    
    notas = open('notas.dat', 'r', encoding='utf-8')
    cad=''
    linea= notas.readline()
    while(linea != ''):
        aux=linea.split(', ', 7)
        cad= linea
        arbol_notas.insert('','end',values=aux)
        linea=notas.readline()
    notas.close()
    

    volver= Button(app2_1, text='VOLVER', command=partial(volver_ventana_listado_notas, app2_1), borderwidth=4)
    volver.place(x=270, y=340, height=50, width=100)
#=======================================
def alta_datos_notas(id_mate_ent, id_alum_ent, nota1_ent, nota2_ent, nota3_ent, nota4_ent, datos_notas, cont):
       
    llenar_vector_notas(id_mate_ent, id_alum_ent, nota1_ent, nota2_ent, nota3_ent, nota4_ent, datos_notas, cont)

    archi_notas = open('notas.dat', 'a', encoding='utf-8')
    for n in range(7):
        if(n < 6):
            archi_notas.write(str(datos_notas[n]) + ', ')
        else:
            archi_notas.write(str(datos_notas[n]) + '\n')

    datos_notas.clear()
    archi_notas.close()
#=======================================   
def llenar_vector_notas(id_mate_ent, id_alum_ent, nota1_ent, nota2_ent, nota3_ent, nota4_ent, datos_notas, cont):
  

    if(len(id_mate_ent.get()) > 0 and len(id_alum_ent.get()) > 0 and len(nota1_ent.get()) > 0 and 
       len(nota2_ent.get()) > 0 and len(nota3_ent.get()) > 0 and len(nota4_ent.get()) > 0):

        contador= open('contador_notas.dat', 'r', encoding='utf-8')
        linea =contador.read()
        cont = int(linea)+1
        contador.close()

        datos_notas.append(cont)
        
        datos_notas.append(id_alum_ent.get())
        id_alum_ent.delete(0, END)

        datos_notas.append(id_mate_ent.get())
        id_mate_ent.delete(0, END)

        datos_notas.append(nota1_ent.get())
        nota1_ent.delete(0, END)
        nota1_ent.focus_set()

        datos_notas.append(nota2_ent.get())
        nota2_ent.delete(0, END)

        datos_notas.append(nota3_ent.get())
        nota3_ent.delete(0, END)

        datos_notas.append(nota4_ent.get())
        nota4_ent.delete(0, END)

    else:
        messagebox.showerror(title='Incorrecto', message='Por favor ingrese datos validos')

    contador = open('contador_notas.dat', 'w', encoding='utf-8')
    contador.write(str(cont))
    contador.close()
#=======================================
def volver_notas(app2):
    app2.destroy()
#=======================================
def alta_notas(menu2):
    app2 = Toplevel(menu2)
    app2.title('Notas')
    app2.geometry('500x500+650+0')
    app2.configure(background='gainsboro')

    #Labels===============================
    alumno = Label(app2, text='Id del Alumno: ', background='gainsboro')
    alumno.place(x= 75, y= 50)

    materia = Label(app2, text='Id de la Materia: ', background='gainsboro')
    materia.place(x= 62, y= 100)

    nota1 = Label(app2, text='Nota 1: ', background='gainsboro')
    nota1.place(x= 120, y= 150)

    nota2 = Label(app2, text='Nota 2: ', background='gainsboro')
    nota2.place(x=120, y=200)

    nota3 = Label(app2, text='Nota 3: ', background='gainsboro')
    nota3.place(x= 120, y=250)

    nota4 = Label(app2, text='Nota 4: ', background='gainsboro')
    nota4.place(x=120, y= 300)

    #Entrys==============================
    id_alum_ent = Entry(app2, width=15)
    id_alum_ent.place(x=200, y= 50)

    id_mate_ent = Entry(app2, width=15)
    id_mate_ent.place(x= 200, y= 100)


    nota1_ent = Entry(app2, width=15)
    nota1_ent.place(x= 200, y=150)

    nota2_ent = Entry(app2, width=15)
    nota2_ent.place(x= 200, y=200)

    nota3_ent = Entry(app2, width=15)
    nota3_ent.place(x= 200, y=250)

    nota4_ent = Entry(app2, width=15)
    nota4_ent.place(x= 200, y=300)

    #===================================
    datos_notas=[]
    cont= int(0)

    agregar_dat= Button(app2, text='Agregar Datos',
                        command=partial(alta_datos_notas, id_mate_ent, id_alum_ent, nota1_ent, nota2_ent, nota3_ent, nota4_ent, datos_notas, cont), borderwidth=4)
    agregar_dat.place(x=210, y=350, height=50, width=110)

    volver= Button(app2, text='VOLVER', borderwidth=4, command=partial(volver_notas, app2))
    volver.place(x=210, y= 430, height= 50, width= 110)
#=======================================
def volver_ventana_menu_notas(menu2):
    menu2.destroy()
#=======================================
def ventana_menu_notas(app0):
    menu2 = Toplevel(app0)
    menu2.title('Notas')
    menu2.geometry('600x300+0+350')
    menu2.configure(background='gainsboro')

    #Botones=============================
    alta = Button(menu2, text='ALTA DATOS', command=partial(alta_notas,menu2), borderwidth=4)
    alta.place(x= 60,  y= 100, height= 50, width= 110)

    baja = Button(menu2, text='BAJA DATOS',command=partial(ventana_baja_notas, menu2), borderwidth=4)
    baja.place(x=190, y=100, height=50, width=110)

    modificacion= Button(menu2, text='MODIFICACION' ,command=partial(ventana_modificar_notas, menu2),borderwidth=4)
    modificacion.place(x=320, y=100, height=50, width= 110)

    listado = Button(menu2, text='LISTADO', command=partial(listado_notas,menu2) ,borderwidth=4)
    listado.place(x=450, y= 100, height=50, width=110)

    volver= Button(menu2, text='VOLVER', borderwidth=4, command=partial(volver_ventana_menu_notas, menu2))
    volver.place(x=255, y= 200, height= 50, width= 110)





#Ventana Materias============================================================================================================================
def buscar_materias(buscador_ent, materia_nom, curso_combo_mate, datos_materias):
    if(len(buscador_ent.get()) > 0):
        dato = buscador_ent.get()

        materias = open('materias.dat', 'r', encoding='utf-8')
        linita = materias.readline()

        while(linita != ''):
            aux = linita.split(',', 3)
            if(aux[0] == dato):
                materia_nom.insert(0, aux[1])
                curso_combo_mate.insert(0, aux[2])

            linita = materias.readline()
        materias.close()
    else:
        messagebox.showerror(title='Incorrecto', message='Ingrese una id de materia valida')
#=======================================
def modificacion_materias(buscador_ent, materia_nom, curso_combo_mate, datos_materias):
    dato = buscador_ent.get()


    materias=open('materias.dat', 'r', encoding='utf-8')
    temporal=open('materias_temp.dat', 'w', encoding='utf-8')

    linita= materias.readline()
    while(linita != ''):
        aux= linita.split(', ', 3)
        if(dato != aux[0]):
            temporal.write(linita)
        else:
            m_mate = materia_nom.get()
            materia_nom.delete(0, END)
            m_curs = curso_combo_mate.get()
            curso_combo_mate.delete(0, END)

            buscador_ent.delete(0, END)

            lineaux = ''
            lineaux = dato + ', ' + str(m_mate) + ', ' + str(m_curs) + '\n'
            temporal.write(lineaux)
            messagebox.showinfo(title='Modificacion Exitosa', message='El dato se ha modificado con exito')

        linita = materias.readline()
    materias.close()
    temporal.close()

    #==============================
    materias = open('materias.dat', 'w', encoding='utf-8')
    temporal= open('materias_temp.dat','r', encoding='utf-8')

    nuevalinita= temporal.readline()
    while(nuevalinita != ''):
        materias.write(nuevalinita)
        nuevalinita=temporal.readline()
        
    materias.close()
    temporal.close()
    
    #========================================================
    temporal = open('materias_temp.dat','w', encoding='utf-8')
    temporal.close()
#=======================================
def volver_ventana_modificacion_materias(app3_3):
    app3_3.destroy()
#=======================================
def ventana_modificacion_materias(menu3):
    app3_3 = Toplevel(menu3)
    app3_3.geometry('600x350+650+0')
    app3_3.title('Modificacion Materias')
    app3_3.configure(background='gainsboro')

    #Labels=============================
    separacion = Label(app3_3, background= 'gainsboro', relief='raised', borderwidth=6)
    separacion.place(x= 280, y= 0, height= 350, width=30)

    buscador = Label(app3_3, text='Ingrese la Id de la materia a modificar', background='gainsboro')
    buscador.place(x=40, y= 120)

    nombre = Label(app3_3, text='Nombre de la Materia: ', background='gainsboro')
    nombre.place(x= 390, y= 50)

    curso  = Label(app3_3, text='Curso  de la Materia: ', background='gainsboro')
    curso.place(x= 395, y= 120)

    #Entry y Combo======================
    buscador_ent = Entry(app3_3, width=30)
    buscador_ent.place(x= 50, y= 150)

    materia_nom = Entry(app3_3, width=30)
    materia_nom.place(x= 360, y=80)

    vec_curso = ['', '1', '2', '3','4','5','6']

    curso_combo_mate= ttk.Combobox(app3_3, exportselect = True)
    curso_combo_mate.place(x = 380, y=150)

    curso_combo_mate['values'] = vec_curso

    #Botones============================
    datos_materias=[]
    cont= int(0)

    agregar_dat = Button(app3_3, text='MODIFICAR',command=partial(modificacion_materias,buscador_ent, materia_nom, curso_combo_mate, datos_materias), borderwidth=4)
    agregar_dat.place(x = 403, y= 200, width= 100, height= 50)

    buscar = Button(app3_3, text='BUSCAR', command=partial(buscar_materias,buscador_ent, materia_nom, curso_combo_mate, datos_materias),borderwidth=4)
    buscar.place(x=95, y= 200, width=100, height=50)

    volver = Button(app3_3, text='VOLVER', command=partial(volver_ventana_modificacion_materias, app3_3), borderwidth= 4)
    volver.place(x=403, y= 280, width=100, height=50)
#Listado================================
def volver_ventana_listado_materias(app3_2):
    app3_2.destroy()
#=======================================
def ventana_listado_materias(menu3):
    app3_2 = Toplevel(menu3)
    app3_2.title('Listado Materias')
    app3_2.geometry('450x500+650+0')
    app3_2.configure(background='gainsboro')
    
    arbol_materias = ttk.Treeview(app3_2, columns=(1, 2, 3), show='headings', height='10')
    arbol_materias.heading(1, text='ID')
    arbol_materias.column(1, width=50)

    arbol_materias.heading(2, text='Nombre Materia')
    arbol_materias.column(2, width=150)

    arbol_materias.heading(3, text='Curso')
    arbol_materias.column(3, width=50)

    arbol_materias.place(x=100, y=100)
    
    mat = open('materias.dat', 'a', encoding='utf-8')
    mat.close()

    mat = open('materias.dat', 'r', encoding='utf-8')
    
    linita = mat.readline()
    while(linita != ''):
        aux = linita.split(', ', 3)
        arbol_materias.insert('','end', values=aux)
        linita = mat.readline()

    mat.close()

    volver= Button(app3_2, text='VOLVER', command=partial(volver_ventana_listado_materias, app3_2), borderwidth=4)
    volver.place(x=180, y=400, height=50, width=100)  
#Baja===================================
def baja_materias(bajon_ent):
    baja = bajon_ent.get()
    bajon_ent.delete(0, END)
    bajon_ent.focus_set()

    materias= open('materias.dat', 'r', encoding='utf-8')
    temporal= open('materias_temp.dat', 'w', encoding='utf-8')

    linita= materias.readline()

    while(linita != ''):
        aux = linita.split(', ', 3)
        if(baja != aux[0]):
            temporal.write(linita)
        else:
            messagebox.showinfo(title='Baja de Materias', message='Se elimino el dato de la materia con exito')
        linita= materias.readline() 

    materias.close()
    temporal.close()

    #===============================
    materias= open('materias.dat', 'w', encoding='utf-8')
    temporal= open('materias_temp.dat', 'r', encoding='utf-8')

    linita = temporal.readline()
    while(linita != ''):
        materias.write(linita)
        linita = temporal.readline()

    materias.close()
    temporal.close()

    temporal= open('materias_temp.dat','w', encoding='utf-8')
    temporal.close()
#=======================================
def volver_baja_materias(app3_1):
    app3_1.destroy()
#=======================================
def ventana_baja_materias(menu3):
    app3_1 = Toplevel(menu3)
    app3_1.title('Baja Materias')
    app3_1.geometry('500x400+650+0')
    app3_1.configure(background='gainsboro')

    ingrese= Label(app3_1,text='Ingrese la ID del dato que quiere borrar', background='gainsboro')
    ingrese.place(x=150,y=100)

    bajon_ent = Entry(app3_1,width=30)
    bajon_ent.place(x= 160, y= 150)
    
    volver= Button(app3_1, text='VOLVER', command=partial(volver_baja_materias, app3_1), borderwidth=4)
    volver.place(x=200, y=300, height=50, width=100)
    
    bajar= Button(app3_1, text='BORRAR', borderwidth=4, command=partial(baja_materias, bajon_ent))
    bajar.place(x=200, y=200, height=50, width=100)
#Alta===================================
def alta_datos_materias(cont, datos_materias, materia_nom, curso_combo_mate):
    llenar_vector_materias(cont, datos_materias, materia_nom, curso_combo_mate)

    archi_materias = open('materias.dat','a', encoding='utf-8')
    for n in range(3):
        if(n < 2):
            archi_materias.write(str(datos_materias[n]) + ', ')
        else:
            archi_materias.write(str(datos_materias[n]) + '\n')

    datos_materias.clear()
    archi_materias.close()
#=======================================
def llenar_vector_materias(cont, datos_materias, materia_nom, curso_combo_mate):


    if(len(materia_nom.get()) > 0 and len(curso_combo_mate.get()) != ''):
        
        contador = open('contador_materias.dat', 'r', encoding='utf-8')
        linea = contador.read()
        cont = int(linea)+1
        contador.close()

        datos_materias.append(cont)

        datos_materias.append(materia_nom.get())
        materia_nom.delete(0, END)

        datos_materias.append(curso_combo_mate.get())
        curso_combo_mate.delete(0, END)

    else:
        messagebox.showerror(title='Datos Incorrectos', message='Ingrese datos validos')

    contador = open('contador_materias.dat', 'w', encoding='utf-8')
    contador.write(str(cont))
    contador.close()
#=======================================
def volver_alta_materias(app3):
    app3.destroy()
#=======================================
def alta_materias(menu3):
    app3 = Toplevel(menu3)
    app3.title('Alta Materias')
    app3.geometry('500x350+650+0')
    app3.configure(background='gainsboro')
    
    #Labels=============================
    nombre = Label(app3, text='Nombre de la Materia: ', background='gainsboro')
    nombre.place(x= 80, y= 100)

    curso  = Label(app3, text='Curso  de la Materia: ', background='gainsboro')
    curso.place(x= 80, y= 150)

    #Entry y Combo======================
    materia_nom = Entry(app3, width=30)
    materia_nom.place(x= 220, y=100)

    vec_curso = ['', '1', '2', '3','4','5','6']

    curso_combo_mate= ttk.Combobox(app3, exportselect = True)
    curso_combo_mate.place(x = 220, y=150)

    curso_combo_mate['values'] = vec_curso

    #Botones============================
    datos_materias=[]
    cont= int(0)

    agregar_dat = Button(app3, text='Agregar Datos', command=partial(alta_datos_materias,cont, datos_materias, materia_nom, curso_combo_mate), borderwidth=4)
    agregar_dat.place(x = 220, y= 200, width= 100, height= 50)

    volver = Button(app3, text='VOLVER', command=partial(volver_alta_materias, app3), borderwidth= 4)
    volver.place(x=220, y= 280, width=100, height=50)
#=======================================    
def volver_ventana_menu_materias(menu3):
    menu3.destroy()
#=======================================
def ventana_menu_materias(app0):
    menu3 = Toplevel(app0)
    menu3.title('MATERIAS')
    menu3.geometry('600x300+0+350')
    menu3.configure(background='gainsboro')

    #Botones=============================
    alta = Button(menu3, text='ALTA DATOS', command=partial( alta_materias,menu3), borderwidth=4)
    alta.place(x= 60,  y= 100, height= 50, width= 110)

    baja = Button(menu3, text='BAJA DATOS', command=partial(ventana_baja_materias,menu3), borderwidth=4)
    baja.place(x=190, y=100, height=50, width=110)

    modificacion= Button(menu3, text='MODIFICACION' , command=partial(ventana_modificacion_materias,menu3), borderwidth=4)
    modificacion.place(x=320, y=100, height=50, width= 110)

    listado = Button(menu3, text='LISTADO', command=partial(ventana_listado_materias, menu3), borderwidth=4)
    listado.place(x=450, y= 100, height=50, width=110)

    volver= Button(menu3, text='VOLVER', borderwidth=4, command=partial(volver_ventana_menu_materias, menu3))
    volver.place(x=255, y= 200, height= 50, width= 110)







#Listado de Boletines=========================================================================================================================
def limpiar_arbol(arbol_notas):
    arbol_notas.delete(*arbol_notas.get_children())
#=======================================
def buscar_nota(buscador, arbol_alum, arbol_notas):

    fila= ''
    dato = buscador.get()
    buscador.delete(0, END)
    
    notas = open('notas.dat', 'r', encoding='utf-8')
    temporal = open('temporal.dat','w', encoding='utf-8')
    
    linita= notas.readline()
    while(linita != ''):
        notas_aux = linita.split(', ', 7)
        if(notas_aux[1] == dato):
            materia = open('materias.dat', 'r', encoding='utf-8')
            materialinea = materia.readline()
            while(materialinea != ''):
                aux_materia = materialinea.split(', ', 3)
                if(aux_materia[0] == notas_aux[2]):
                    fila = str(dato) + ', ' + str(aux_materia[1]) + ', ' + str(notas_aux[3]) + ', ' + str(notas_aux[4]) + ', ' +  str(notas_aux[5]) + ', ' + str(notas_aux[6]) 
                    temporal.write(fila)
                materialinea = materia.readline()

        linita = notas.readline()
    
    materia.close()
    notas.close()
    temporal.close()

    temporal = open('temporal.dat', 'r', encoding='utf-8')
    linea = temporal.readline()
    while(linea != ''):
        aux = linea.split(', ', 6)
        arbol_notas.insert('', 'end', values=aux)
        linea= temporal.readline()
    temporal.close()

    temporal = open('temporal.dat', 'w', encoding='utf-8')
    fila = ''
    temporal.close()
#=======================================
def volver_boletines(app4):
    app4.destroy()
#=======================================
def ventana_boletines(app0):
    app4 = Toplevel(app0)
    app4.title('Boletines')
    app4.geometry('910x680+450+0')
    app4.configure(background='gainsboro')

    volver = Button(app4, text='VOLVER', command=partial(volver_boletines, app4), borderwidth=4)
    volver.place(x=715, y= 600, height=50, width=100)

    #Treeview=======================================

    arbol_alum = ttk.Treeview(app4, columns=(1,2,3,4,5,6,7), show='headings',height='10')

    arbol_alum.heading(1, text='Id')
    arbol_alum.column(1, width=30)

    arbol_alum.heading(2, text='Dni')
    arbol_alum.column(2, width=100)

    arbol_alum.heading(3, text='Apellido')
    arbol_alum.column(3, width=150)

    arbol_alum.heading(4, text='Nombre')
    arbol_alum.column(4, width=150)

    arbol_alum.heading(5, text='Email')
    arbol_alum.column(5, width=250)

    arbol_alum.heading(6, text='Curso')
    arbol_alum.column(6, width=50)

    arbol_alum.heading(7, text='Division')
    arbol_alum.column(7, width=70)
    arbol_alum.place(x=50, y=100)
    
    
    alum = open('alumnos.dat', 'r', encoding='utf-8')
    cad=''
    linea= alum.readline()
    while(linea != ''):
        aux=linea.split(', ', 7)
        cad= linea
        arbol_alum.insert('','end',values=aux)
        linea=alum.readline()
    alum.close() 

    #Treeview Notas=============================

    arbol_notas = ttk.Treeview(app4, columns=(1,2,3,4,5,6), show='headings', height='14')
    arbol_notas.heading(1, text='Id Alumno')
    arbol_notas.column(1, width=100)

    arbol_notas.heading(2, text='Materia')
    arbol_notas.column(2, width=180)

    arbol_notas.heading(3, text='Nota 1')
    arbol_notas.column(3, width=80)

    arbol_notas.heading(4, text='Nota 2')
    arbol_notas.column(4, width=80)

    arbol_notas.heading(5, text='Nota 3')
    arbol_notas.column(5, width=80)

    arbol_notas.heading(6, text='Nota 4')
    arbol_notas.column(6, width=80)
    
    arbol_notas.place(x= 50, y=350)
    
    #================================
    busca_lbl = Label(app4, text='Ingrese la id de alumno' + '\n' + 'del cual quiere saber la nota', background='gainsboro')
    busca_lbl.place(x=685, y= 345)

    buscador = Entry(app4, width= 30)
    buscador.place(x= 670, y= 400)

    buscar = Button(app4, text='BUSCAR', command=partial(buscar_nota,buscador, arbol_alum, arbol_notas), borderwidth=4)
    buscar.place(x=715, y= 450, height=50, width=100)

    limpiar = Button(app4, text='LIMPIAR', command=partial(limpiar_arbol, arbol_notas), borderwidth=4)
    limpiar.place(x=715, y= 525, height=50, width=100)







#Ventana Principal============================================================================================================================
def cerrar_ventana(app0):
    app0.destroy()
#========================
def creacion_archivos():
    #Creacion de Archivos por si no existe================
    alumnos = open('alumnos.dat', 'a', encoding='utf-8')
    alumnos.close()

    materias = open('materias.dat', 'a', encoding='utf-8')
    materias.close()

    notas = open('notas.dat', 'a', encoding='utf-8')
    notas.close()

    #Contadores===========================================
    contador = open('contador.dat', 'a', encoding='utf-8')
    contador.close()

    contador = open('contador.dat', 'r', encoding='utf-8')
    linosa = contador.read()
    contador.close()

    contador = open('contador.dat', 'a', encoding='utf-8')
    if(linosa == ''):
        contador.write(str(0))
    contador.close()


    contador_notas = open('contador_notas.dat', 'a', encoding='utf-8')
    contador_notas.close()

    contador_notas = open('contador_notas.dat', 'r', encoding='utf-8')
    lexen = contador_notas.read()
    contador_notas.close()

    contador_notas = open('contador_notas.dat', 'a', encoding='utf-8')
    if(lexen == ''):
        contador_notas.write(str(0))
    contador_notas.close()



    contador_materias = open('contador_materias.dat', 'a', encoding='utf-8')
    contador_materias.close()

    contador_materias = open('contador_materias.dat', 'r', encoding='utf-8')
    lixus = contador_materias.read()
    contador_materias.close()

    contador_materias = open('contador_materias.dat', 'a', encoding='utf-8')
    if(lixus == ''):
        contador_materias.write(str(0))
    contador_materias.close()

    print('Si este print aparece, es por que se crearon todos los archivos con exito')
#========================

app0 = Tk()
app0.title('Boletin')
app0.geometry('630x300+0+0')
app0.configure(background='gainsboro')

creacion_archivos()

alumnos = Button(app0, text='ALUMNOS',borderwidth=4, command=partial(ventana_menu_alumnos,app0))
alumnos.place(x = 100, y = 100, height= 50, width= 100)

notas = Button(app0, text='NOTAS',command=partial(ventana_menu_notas, app0), borderwidth=4)
notas.place(x = 340, y = 100, height= 50, width= 100)

materias = Button(app0, text='MATERIAS', command= partial(ventana_menu_materias, app0), borderwidth=4)
materias.place(x = 220, y = 100, height= 50, width= 100)

listado = Button(app0, text='BOLETINES', command= partial(ventana_boletines, app0), borderwidth=4)
listado.place(x= 460, y= 100, height=50, width=100)

volver= Button(app0, text='CERRAR', borderwidth=4, command=partial(cerrar_ventana, app0))
volver.place(x=280, y= 200, height= 50, width= 100)


app0.mainloop()