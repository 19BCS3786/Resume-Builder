from tkinter import *
import os
from resume_2 import *
from PIL import ImageTk,Image

def f_1():
    try:
        os.remove('output_resume.txt')
    except:
        pass

def welcome():
    def done():
        root.destroy()

    def f2():
        root.destroy()
        f_1()
        f1()
    root = tk.Tk()
    root.title("Resume Builder")
    logo = Image.open('resumebuilder.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.pack()

    canvas=tk.Canvas(root,height=400,width=500,bg="#263D42",highlightbackground='black',highlightthickness=2)
    canvas.pack()

    windowWidth = 500
    windowHeight = 650

    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2 )

    root.geometry("+{}+{}".format(positionRight, positionDown))

    frame=tk.Frame(root,bg='silver',highlightbackground='gold1',highlightthickness=2)
    frame.place(relwidth=0.6, relheight=0.4, relx=0.2, rely=0.5)

    tk.Label(frame,text='',bg='silver').grid(row=0,column=1)
    tk.Label(frame,text="  Welcome",bg='silver',fg='black',font='Calibiri 20 bold').grid(row=1,column=1)
    tk.Label(frame,text='',bg='silver').grid(row=2,column=1)
    tk.Label(frame,text='Provide us the details,\n    We will build your resume!',bg='silver',fg='blue').grid(row=3,column=1)
    tk.Label(frame,text='',bg='silver').grid(row=4,column=1)
    tk.Label(frame,text='',bg='silver').grid(row=5,column=1)
    tk.Label(frame,text='Lets begin ->',fg='red',bg='silver',font='Calibiri 10 underline').grid(row=6,column=1)

    tk.Button(frame,text="Continue",bg='light grey',fg='black',height=2,width=8,relief='raised',font='Calibiri 10 bold',command=f2).grid(row=6,column=2)
    tk.Button(frame,text="Exit",bg='light grey',fg='black',height=2,width=8,relief='raised',font='Calibiri 10 bold',command=done).grid(row=7,column=2)

    root.mainloop()

welcome()

