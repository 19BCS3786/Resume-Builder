from resume_4 import *
import tkinter as tk

def f_3():
  try:
    f=open("output_resume.txt","a")

    f.write('\t\t\t\t\t====================================\t\t\t\t\n')
    f.write('\t\t\t\t\t\t Educational Details\t\t\t\t\n')
    f.write('\t\t\t\t\t====================================\t\t\t\t\n\n')
    f.write('1. School Details-\n')
    f.write('______________________________________________________________________________________________________________________\nMatriculation-\nSchool-     ')
    f.write(s_10.get()+'\nPercentage- '+p_10.get()+'%\n')
    f.write('\n\n10+2->\nSchool-     ')
    f.write(s_12.get()+'\nPercentage- '+p_12.get()+'%\n______________________________________________________________________________________________________________________')
    f.write('\n2. University Details- \n\nGraduation-\n')
    f.write('College-'+u_g.get()+'\n')
    f.write('Course- '+u_d.get()+' in '+u_f.get()+'\n')
    f.write('Year-   '+u_y.get()+'\n')
    f.write('CGPA-   '+u_c.get())
    if p_g.get()!='':
        f.write('\n\n\nPost Graduation-\n')
        f.write('College-'+p_g.get()+'\n')
        f.write('Course- '+p_d.get()+' in '+p_f.get()+'\n')
        f.write('Year-   '+p_y.get()+'\n')
        f.write('CGPA-   '+p_c.get()+'\n\n')
    else:
        f.write('\n\n')
    f.write('______________________________________________________________________________________________________________________\n\n')

    f.close()

  except:
      pass


def f3():
    def f6():
        root.destroy()
        f_3()
        f5()

    root=tk.Tk()
    root.title('Step 2/3')

    canvas = tk.Canvas(root, height=600, width=850, bg='LightSkyBlue4')
    canvas.pack()
    windowWidth = 900
    windowHeight = 650

    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

    root.geometry("+{}+{}".format(positionRight, positionDown))

    frame = tk.Frame(root, bg='khaki3',highlightbackground='black',highlightthickness=1)
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    tk.Label(frame,text='Educational Details...',font='Calibiri 16 underline',fg='black',bg='khaki3').grid(row=0,column=1)

    global s_10
    global s_12
    global p_10
    global p_12
    global u_g
    global u_y
    global u_d
    global u_f
    global u_c
    global p_g
    global p_y
    global p_d
    global p_f
    global p_c

    s_10=tk.StringVar()
    s_12=tk.StringVar()
    p_10=tk.StringVar()
    p_12=tk.StringVar()
    u_g = tk.StringVar()
    u_y = tk.StringVar()
    u_d = tk.StringVar()
    u_f = tk.StringVar()
    u_c = tk.StringVar()
    p_g = tk.StringVar()
    p_y = tk.StringVar()
    p_d = tk.StringVar()
    p_f = tk.StringVar()
    p_c = tk.StringVar()

    tk.Label(frame,text='\n',bg='khaki3').grid(row=1,column=1)
    tk.Label(frame,text='School(X)      ',font='Calibiri 10 bold',bg='khaki3').grid(row=2,column=0)
    tk.Entry(frame,width='40',relief='raised',bg='silver',textvariable=s_10).grid(row=2,column=1,ipady=7)
    tk.Label(frame,text='                      ',bg='khaki3').grid(row=2,column=2)
    tk.Label(frame,text='Percentage(X)   ',font='Calibiri 10 bold',bg='khaki3').grid(row=2,column=4)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_10).grid(row=2,column=5,ipady=7)
    tk.Label(frame,text='%',bg='khaki3',font='Calibiri 10 bold').grid(row=2,column=6)
    tk.Label(frame,text='',bg='khaki3').grid(row=3,column=1)


    tk.Label(frame,text='School(XII)      ',font='Calibiri 10 bold',bg='khaki3').grid(row=4,column=0)
    tk.Entry(frame,width='40',relief='raised',bg='silver',textvariable=s_12).grid(row=4,column=1,ipady=7)
    tk.Label(frame,text='                      ',bg='khaki3').grid(row=4,column=2)
    tk.Label(frame,text='  Percentage(XII)   ',font='Calibiri 10 bold',bg='khaki3').grid(row=4,column=4)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_12).grid(row=4,column=5,ipady=7)
    tk.Label(frame,text='%',bg='khaki3',font='Calibiri 10 bold').grid(row=4,column=6)
    tk.Label(frame,text='\n\n',bg='khaki3').grid(row=5,column=0)

    tk.Label(frame,text='College/University',font='Calibiri 10 bold',bg='khaki3').grid(row=6,column=0)
    tk.Entry(frame,width='40',relief='raised',bg='silver',textvariable=u_g).grid(row=6,column=1,ipady=7)
    tk.Label(frame,text='                      ',bg='khaki3').grid(row=6,column=2)
    tk.Label(frame,text='Graduation Year',font='Calibiri 10 bold',bg='khaki3').grid(row=6,column=4)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=u_y).grid(row=6,column=5,ipady=7)
    tk.Label(frame,text='',bg='khaki3').grid(row=7,column=0)
    tk.Label(frame,text='Degree',font='Calibiri 10 bold',bg='khaki3').grid(row=8,column=0)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=u_d).place(x=100,y=254,height=30)
    tk.Label(frame,text='Field',font='Calibiri 10 bold',bg='khaki3').place(x=220,y=258)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=u_f).place(x=280,y=254,height=30,width=180)
    tk.Label(frame,text='CGPA',font='Calibiri 10 bold',bg='khaki3').place(x=500,y=258)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=u_c).place(x=560,y=254,height=30)
    tk.Label(frame,text='\n\n',bg='khaki3').grid(row=9,column=0)


    tk.Label(frame,text='Post Graduation',font='Calibiri 10 bold',bg='khaki3').grid(row=10,column=0)
    tk.Entry(frame,width='40',relief='raised',bg='silver',textvariable=p_g).grid(row=10,column=1,ipady=7)
    tk.Label(frame,text='                      ',bg='khaki3').grid(row=10,column=2)
    tk.Label(frame,text='P.G Year',font='Calibiri 10 bold',bg='khaki3').grid(row=10,column=4)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_y).grid(row=10,column=5,ipady=7)
    tk.Label(frame,text='',bg='khaki3').grid(row=11,column=0)
    tk.Label(frame,text='Degree',font='Calibiri 10 bold',bg='khaki3').grid(row=12,column=0)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_d).place(x=100,y=384,height=30)
    tk.Label(frame,text='Field',font='Calibiri 10 bold',bg='khaki3').place(x=220,y=388)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_f).place(x=280,y=384,height=30,width=180)
    tk.Label(frame,text='CGPA',font='Calibiri 10 bold',bg='khaki3').place(x=500,y=388)
    tk.Entry(frame,width='10',relief='raised',bg='silver',textvariable=p_c).place(x=560,y=384,height=30)
    tk.Label(frame,text='\n',bg='khaki3').grid(row=13,column=0)

    tk.Button(root,text='Continue',bg='khaki3',fg='black',height=2,width=9,relief='raised',font='Calibiri 10 bold',command=f6).place(x=370,y=550)


    root.mainloop()

