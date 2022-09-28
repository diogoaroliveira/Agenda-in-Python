# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:11:08 2022

@author: diogo
"""

from tkinter import*
from tkcalendar import *

def dia():
    print(cal.get())

def dia2():
    if dia() != cal.get():
        return cal.get()

eventos = {}
strEventos = ""

'''def callback(*args):
    for hora in eventos[cal.get()]:
        global strEventos
        strEventos = strEventos + "➜" + hora +"\t" + eventos[cal.get()][hora]
    texto.set(strEventos)'''

def addEvento():
    nome = txtEvento.get()
    date = str(cal.get())
    if not date in eventos:
        eventos[date] = {opcao.get(): ""}
    eventos[date][opcao.get()] = nome
    print(eventos[date])
    print(eventos)

def verEventos():
    date = str(cal.get())
    if date in eventos:
        lb1=Label(root,text=0)
        lb2=Label(root,text=0)
        if  eventos[date] == "":
            lb2.place_forget()
            lb1.place_forget()
            lb1=Label(root, text="Agenda vazia para hoje", font=("Titillium Web", 10, "bold")) \
            .place(x=122, y=190)
        else:
            lb2.place_forget()
            lb1.place_forget()
            lb2=Label(root, text= eventos[date], font=("Titillium Web", 10, "bold")) \
                .place(x=122, y=190)

    else:
        btverEventos = Button(command=0)



mycolor = '#%02x%02x%02x' % (105,13,13)

root=Tk()
root.title("Agenda")
root.geometry("350x500")
f1=Frame(root,width=500,height=20,relief=SUNKEN,bd=4,bg=mycolor)
f1.pack(side=TOP)
f2=Frame(root,width=500,height=550,relief=SUNKEN,bd=4,bg='white')
f2.pack()
root.iconbitmap(r'15may.ico')


#Creating the date column

l4=Label(f2,text='DATA',font=('Titillium Web',20,'bold'),fg='black',anchor='w')
l4.grid(row=0,column=3)

cal=DateEntry(f2,dateformat=3,width=12,date_pattern='dd/mm/yyyy' , background=mycolor,foreground='white',
              borderwidth=4,Calendar =2019, command=dia)
cal.grid(row=1,column=3,sticky='nsew')


# dropdown

horas = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00",
              "08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00",
              "16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]

opcao = StringVar(root)
opcao.set(horas[0])

opt = OptionMenu(root, opcao, *horas)
opt.config(width=29, font=('Helvetica', 12))
opt.pack()



'''opcao.trace('w', callback)'''

#
txtEvento = Entry(root, width = 50)
txtEvento.pack()

btCriar = Button(root, text="Adicionar Evento", command=addEvento)
btCriar.pack()

btverEventos = Button(root, text=("Ver agenda para este dia"), command=verEventos)
btverEventos.place(x=122,y=170)

texto = StringVar()




root.mainloop()