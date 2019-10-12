from searchapp import *
from tkinter import messagebox
from tkinter import *

w=Tk(className='Pocket Notebook')
w.geometry('600x300+80+20')

def about():
    w2=Tk(className='About Pocket Notebook')
    w2.geometry('600x300+500+200')
    Label(w2,text='Hello user').grid()
    Label(w2, text='This App is built for Students,Employees,Salesman,Businessmen,Teachers and so..on.').grid()
    Label(w2,text='To create their own quick Todo lists,schedules, short notes.')
def exit():
    ans=messagebox.askquestion('Exit task?','Do you want to exit?.')
    if(ans=='yes'):
        w.quit()

def schedule():
    w3=Tk()
    w3.geometry('600x400+80+20')
    Button(w3,text='Personal schedule').grid(row=0,column=0)
    Button(w3,text='Daily schedule').grid(row=0,column=1)


def todo():

    msg='Enter the size of Your ToDo list :'
    Label(w,text=msg,bg='green').grid()
    l1=IntVar()
    Entry(w,textvariable=l1).grid()
    l1.set(value=0)

    def click():
        b1=l1.get()
        text2=b1
        if(b1==0 or b1<0):
            ans = messagebox.showerror('Invalid Number', 'List cannot be 0 or negative')
        else:
            Label(w, text='Enter your lists:').grid()
            for i in range(1, b1 + 1):
                Label(w, text=i).grid()
                Entry(w).grid()


    Button(w,text='Click here',command=click).grid()








def save():

    messagebox.showinfo('Save','File saved successfully')

def dark():
    w.configure(background='black')

def light():
    w.configure(background='white')

def lblue():
    w.configure(background='lightblue')


main_menu=Menu(w)
w.config(menu=main_menu)
filemenu=Menu(main_menu)
main_menu.add_cascade(label='File',menu=filemenu,activeforeground='white',activebackground='blue')

new=Menu(main_menu)
filemenu.add_cascade(label='New',menu=new,activebackground='orange',activeforeground='white')
new.add_command(label='Notes',activebackground='lightgreen',activeforeground='white')
new.add_command(label='ToDo List',activebackground='lightgreen',activeforeground='white',command=todo)
new.add_command(label='Schedule',activebackground='lightgreen',activeforeground='white',command=schedule)
new.add_command(label='Wikipedia',activebackground='lightgreen',activeforeground='white',command=callme)

filemenu.add_command(label='Open',activebackground='orange',activeforeground='white')
filemenu.add_command(label='Save',activebackground='orange',activeforeground='white',command=save)
filemenu.add_command(label='Save as',activebackground='orange',activeforeground='white')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit,activebackground='red',activeforeground='white')
editmenu=Menu(main_menu)
main_menu.add_cascade(label='Edit',menu=editmenu,activeforeground='white',activebackground='blue')
editmenu.add_command(label='Undo',activebackground='orange',activeforeground='white')
editmenu.add_command(label='Redo',activebackground='orange',activeforeground='white')
editmenu.add_separator()
editmenu.add_command(label='Cut',activebackground='orange',activeforeground='white')
editmenu.add_command(label='Copy',activebackground='orange',activeforeground='white')
editmenu.add_command(label='Paste',activebackground='orange',activeforeground='white')

theme=Menu(main_menu)
main_menu.add_cascade(label='Theme',menu=theme,activebackground='blue',activeforeground='white')
theme.add_command(label='Dark Theme',activebackground='black',activeforeground='white',command=dark)
theme.add_command(label='White Theme',activebackground='white',activeforeground='black',command=light)
theme.add_command(label='Lightblue Theme',activebackground='lightblue',activeforeground='white',command=lblue)


helpmenu=Menu(main_menu)
main_menu.add_cascade(label='Help',menu=helpmenu,activeforeground='white',activebackground='blue')
helpmenu.add_command(label='About pocket Editor',activebackground='orange',activeforeground='white',command=about)
#helpmenu.add_command(label='Feedback',activebackground='orange',activeforeground='white',command=feedback)


w.mainloop()