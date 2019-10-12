import wikipedia
from tkinter import *
from tkinter import messagebox

def search():
    srh=e1.get()
    tx.delete(1.0, END)
    try:
        wiki = wikipedia.summary(srh)
        tx.insert(INSERT, wiki)
    except:
        messagebox.showerror('Error','Invalid Input')



w=Tk(className='Pocket WikiPedia')
tf=Frame(w)
l1=Label(w,text='Search here :',bg='lightblue').pack()
e1=Entry(w,width=20,bd=2)

e1.pack()
b1=Button(w,text='search',command=search,activeforeground='lightblue')
b1.pack()
tf.pack()

bf=Frame(w)
sc=Scrollbar(bf)
sc.pack(side=RIGHT,fill=Y)
tx=Text(bf,width=150,height=35,yscrollcommand=sc.set,wrap=WORD)
sc.config(command=tx.yview)
tx.pack()

bf.pack()

w.geometry('1250x1000+120+120')
w.mainloop()