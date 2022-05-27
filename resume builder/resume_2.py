from resume_3 import *
import tkinter as tk

def f4():
    p1.destroy()
    f_2()
    f3()

def retrieve_input():
    global address
    address = text_box.get("1.0", "end-1c")
    f4()

def f_2():
    try:
        import datetime
        d1 = datetime.date.today()
        date = d1.strftime('%B %d,%Y')
        f=open("output_resume.txt","w")
        final=first_name.get()+' '+last_name.get()
        f.write('\t\t\t\t\t=================================\t\t\t\t\n')
        f.write('\t\t\t\t\t\t      RESUME\t\t\t\t\n')
        f.write('\t\t\t\t\t=================================\t\t\t\t\n\n')
        f.write('Made on: '+date+'\n')
        f.write('______________________________________________________________________________________________________________________\n\n')
        f.write('Name:          '+final+'\n')
        st=dob.get()
        dict={'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August','09':'September','10':'October',
              '11':'November','12':'December'}
        f.write('DOB:            ')
        f.write(st[0:2]+' ')
        f.write(dict[(st[3:5])]+', ')
        f.write(st[6:10]+'\n')
        f.write('Gender:       '+gender.get()+'\n')
        f.write('Mail:             '+mail.get()+'\n')
        f.write('Phone:         '+phone_no.get()+'\n')
        f.write(address+'\n')
        f.write(state.get()+', '+country.get()+'\n'+zip_code.get()+'\n\n')
        f.write('______________________________________________________________________________________________________________________\n\n')

        f.close()
    except:
        pass


def f1():
    global p1
    p1=tk.Tk()
    p1.title("Step 1/3")

    canvas = tk.Canvas(p1, height=730, width=790, bg='#263D42')
    canvas.pack()
    windowWidth = 800
    windowHeight = 800

    positionRight = int(p1.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(p1.winfo_screenheight() / 2 - windowHeight / 2)

    p1.geometry("+{}+{}".format(positionRight, positionDown))
    frame = tk.Frame(p1, bg='silver',highlightbackground='orange',highlightthickness=2)
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(frame,text='Personal Information...',font='Calibiri 16 underline',fg='black',bg='silver').grid(row=0,column=1)
    tk.Label(frame,text='',bg='silver').grid(row=1,column=0)
    global first_name
    global last_name
    global dob
    global country
    global state
    global zip_code
    global mail
    global gender

    first_name = tk.StringVar()
    last_name = tk.StringVar()
    dob = tk.StringVar()
    country = tk.StringVar()
    state = tk.StringVar()
    zip_code = tk.StringVar()
    mail = tk.StringVar()

    tk.Label(frame,text='First Name: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=2,column=0)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',fg='black',textvariable= first_name).grid(row=2,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=3,column=0)
    tk.Label(frame,text='Last Name: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=4,column=0)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable= last_name).grid(row=4,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=5,column=0)



    tk.Label(frame, text="Gender: ",fg='black',bg='silver',font='Calibiri 10 bold' ).grid(row=6,column=0)
    gender=tk.StringVar()
    gender.set('Male')
    tk.Radiobutton(frame,text='Male', variable=gender,value='Male',relief='sunken',bg='light grey',fg='blue',width=6).grid(row=6,column=1)
    tk.Radiobutton(frame, text='Female', variable=gender, value='Female',relief='sunken',bg='light grey',fg='red',width=6).grid(row=6, column=2)
    tk.Label(frame,text='                     ',bg='silver').grid(row=6,column=3)
    tk.Radiobutton(frame, text='Other', variable=gender, value='Other',relief='sunken',bg='light grey',fg='purple',width=6).grid(row=6, column=4)
    tk.Label(frame,text='',bg='silver').grid(row=7,column=0)
    tk.Label(frame,text='Date Of Birth: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=8,column=0)
    tk.Label(frame,text='(dd-mm-yyyy)',fg='black',bg='silver',font='Calibiri 9').grid(row=8,column=2)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable=dob).grid(row=8,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=9,column=0)

    def limit_phone(*args):
        value = phone_no.get()
        if len(value) > 10: phone_no.set(value[:10])

    global phone_no
    phone_no = tk.StringVar()
    phone_no.trace('w', limit_phone)

    tk.Label(frame,text='Phone no. : ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=10,column=0)
    tk.Entry(frame,width='30',relief='raised',textvariable=phone_no,bg='light blue').grid(row=10,column=1,ipady=7)
    tk.Label(frame,text='(Only 10 digits)',fg='black',bg='silver',font='Calibiri 8').grid(row=10,column=2)
    tk.Label(frame,text='',bg='silver').grid(row=11,column=0)
    tk.Label(frame,text='Country: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=12,column=0)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable=country).grid(row=12,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=13,column=0)
    tk.Label(frame,text='State: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=14,column=0)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable=state).grid(row=14,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=15,column=0)
    tk.Label(frame,text='Zipcode: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=16,column=0)
    zip=tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable=zip_code)
    zip.grid(row=16,column=1,ipady=7)

    tk.Label(frame,text='',bg='silver').grid(row=17,column=0)
    tk.Label(frame,text='Email address: ',fg='black',bg='silver',font='Calibiri 10 bold').grid(row=18,column=0)
    tk.Entry(frame,width='30',relief='raised',bg='light blue',textvariable=mail).grid(row=18,column=1,ipady=7)
    tk.Label(frame,text='',bg='silver').grid(row=19,column=0)
    tk.Label(frame, text='Address: ', fg='black', bg='silver', font='Calibiri 10 bold').grid(row=20, column=0)

    global text_box
    text_box=tk.Text(frame, width='50', relief='raised',bg='light blue',font='Calibiri 9')
    text_box.place(x=118,y=525,height=50)

    tk.Button(p1,text='Continue',bg='DarkOliveGreen1',fg='black',height=2,width=9,relief='raised',font='Calibiri 10 bold',command=retrieve_input).place(x=350,y=675)

    p1.mainloop()

