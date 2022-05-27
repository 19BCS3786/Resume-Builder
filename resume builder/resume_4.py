import tkinter as tk
#from create import *
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def f_4():
  try:
    f=open('output_resume.txt','a')

    f.write('\t\t\t\t\t====================================\t\t\t\t\n')
    f.write('\t\t\t\t\t\t    Project Details\t\t\t\t\n')
    f.write('\t\t\t\t\t====================================\t\t\t\t\n\n')
    if n_1.get()!='':
        f.write('1. '+n_1.get()+' :\n\n')
        if des_1 != '':
            f.write('-> '+des_1+'\n\n')
        f.write('______________________________________________________________________________________________________________________\n\n')

    if n_2.get()!='':
        f.write('2. '+n_2.get()+' :\n\n')
        if des_2 != '':
            f.write('-> '+des_2+'\n\n')
        f.write('______________________________________________________________________________________________________________________\n\n')

    if n_3.get()!='':
        f.write('3. '+n_3.get()+' :\n\n')
        if des_3 != '':
            f.write('-> '+des_3+'\n\n')
        f.write('______________________________________________________________________________________________________________________\n\n')

    f.close()

  except:
      pass


def f5():

    def f8():
        import time
        tk.Button(root, text='Creating...', bg='silver', fg='black', height=2, width=9, relief='raised',
                  font='Calibiri 10 bold', command=f8).place(x=250, y=695)

        def bar():

            tk.progress['value'] = 0
            root.update_idletasks()
            time.sleep(0.5)

            tk.progress['value'] = 20
            root.update_idletasks()
            time.sleep(1)

            tk.progress['value'] = 40
            root.update_idletasks()
            time.sleep(0.5)

            tk.progress['value'] = 60
            root.update_idletasks()
            time.sleep(0.5)

            tk.progress['value'] = 80
            root.update_idletasks()
            time.sleep(1)
            tk.progress['value'] = 100

            tk.Button(root, text='Created', bg='silver', fg='black', height=2, width=9, relief='raised',
                      font='Calibiri 10 bold', command=f8).place(x=250, y=695)

            def retrieve_input():
                global des_1
                des_1 = d_1.get("1.0", "end-1c")
                global des_2
                des_2 = d_2.get("1.0", "end-1c")
                global des_3
                des_3 = d_3.get("1.0", "end-1c")
            retrieve_input()

            messagebox.showinfo("Created", 'Resume Created Successfully!')
            root.destroy()
            print('Thanks for using us!!')
            f_4()
            #f9()

        bar()


    root=tk.Tk()
    root.title('Step 3/3')

    canvas = tk.Canvas(root, height=750, width=770, bg='#263D42')
    canvas.pack()
    windowWidth = 800
    windowHeight = 830

    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    root.geometry("+{}+{}".format(positionRight, positionDown))

    frame = tk.Frame(root, bg='silver',highlightbackground='magenta',highlightthickness=2)
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.progress = Progressbar(root, orient=HORIZONTAL,
                              length=200, mode='determinate')
    tk.progress.place(x=400,y=700,height=30,width=300)

    global n_1
    global n_2
    global n_3

    n_1=tk.StringVar()
    n_2=tk.StringVar()
    n_3=tk.StringVar()
    tk.Label(frame,text='    Add project details...',font='Calibiri 16 ',fg='blue',bg='silver').grid(row=0,column=1)
    tk.Label(frame,text='',bg='silver').grid(row=1,column=0)
    tk.Label(frame,text='Name:      ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=2,column=0)
    tk.Entry(frame,width='40',relief='raised',textvariable=n_1).grid(row=2,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=3,column=0)

    global d_1
    d_1=tk.Text(frame, height=7, width=60,relief='raised')
    d_1.place(x=70,y=100)
    tk.Label(frame,text='',bg='silver').grid(row=4,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=5,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=6,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=7,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=8,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=9,column=0)

    global d_2
    tk.Label(frame,text='Name:      ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=10,column=0)
    tk.Entry(frame,width='40',relief='raised',textvariable=n_2).grid(row=10,column=1,ipady=7)
    d_2=tk.Text(frame, height=7, width=60,relief='raised')
    d_2.place(x=70,y=280)
    tk.Label(frame,text='',bg='silver').grid(row=11,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=12,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=13,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=14,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=15,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=16,column=0)
    tk.Label(frame,text='',bg='silver').grid(row=17,column=0)

    global d_3
    tk.Label(frame,text='Name:      ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=18,column=0)
    tk.Entry(frame,width='40',relief='raised',textvariable=n_3).grid(row=18,column=1,ipady=7)
    d_3=tk.Text(frame, height=7, width=60,relief='raised')
    d_3.place(x=70,y=460)

    tk.Button(root,text='Submit',bg='silver',fg='black',height=2,width=9,relief='raised',font='Calibiri 10 bold',command=f8).place(x=250,y=695)


    root.mainloop()

