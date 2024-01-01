import random
from tkinter import messagebox
import tkinter as tk


m=tk.Tk()

m.wm_title("TICKET")

'''pl1 =tk.PhotoImage(file=r"D:\1.png")
po=tk.Label(image=pl1).grid(row=7,column=4)

pl2 =tk.PhotoImage(file=r"D:\2.png")
po=tk.Label(image=pl2).grid(row=7,column=1)

pl3 =tk.PhotoImage(file=r"D:\3.png")
po=tk.Label(image=pl3,width=280).grid(row=7,column=6)'''


#m.geometry("500x300")


def correct1(inpp):
    if inpp.isalpha():
        return True
    elif " " in inpp:
        return True
    elif inpp == "":
        return True
    else:
        return False
    

def correct2(inpp):
    if (inpp.isdigit() and len(inpp)<4 and int(inpp)<110):
        return True
    elif inpp == "":
        return True
    else:
        return False


def correct3(inpp):
    if (inpp.isdigit() and int(inpp)<20000 and int(inpp) ):
        return True
    elif inpp == "":
        return True
    else:
        return False    
    
def correct4(inpp):
    if (inpp.isalpha() and len(inpp)<20 ):
        return True
    elif inpp == "":
        return True
    elif " " in inpp:
        return True
    else:
        return False   
    
def correct5(inpp):
    if (inpp.isdigit() and int(inpp)<50):
        return True
    elif inpp == "":
        return True
    else:
        return False    


def correct6(inpp):
    if(inpp=="S1" and inpp=="S2" and inpp=="S3" and inpp=="S4" and inpp=="S5" 
       and inpp=="A1" and inpp=="A2" and inpp=="A3"):
        return True
    elif inpp == "":
        return True
    else:
        return False  
    
    
def correct7(inpp):
    if inpp.isalpha():
        return True
    elif inpp == "":
        return True
    elif " " in inpp:
        return True
    else:
        return False
    
def correct8(inpp):
    if inpp.isalpha():
        return True
    elif " " in inpp:
        return True
    elif inpp == "":
        return True
    else:
        return False

def correct9(inpp):
    if (inpp.isdigit() and int(inpp)<5000 and int(inpp)>0):
        return True
    elif inpp == "":
        return True
    else:
        return False  
    
def correct10(inpp):
    if(inpp=="Male" or inpp=="Female" or inpp=="Transgender"):
        return True
    elif inpp == "":
        return True
    else:
        return False 
p=str()


c1=None
ce1=None
cb=None

def confirma():
    
    global c1,ce1,cb
    if(e12.get()=="IndRail"):
        c1=tk.Label(m,text="Please Enter PNR Number").grid(row=4,column=5)
        ce1=tk.Entry(m,bd=5)
        ce1.grid(row=5,column=5)
        cb=tk.Button(m,text="Confirm",bg="red",bd=5,command=pnr).grid(row=6,column=5)

        
def pnr():
    global p,c1,ce1,cb
    j=open("LIST.txt","r")        
        
    if(ce1.get() in j.read()):
        l1=tk.Label(m,text="Name ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=10,column=0)
        ll1=tk.Label(m,text=e1.get(),fg="red",font=("Comic Sans MS",13)).grid(row=10,column=1)
        
        
        l2=tk.Label(m,text="AGE ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=11,column=0)
        ll2=tk.Label(m,text=e2.get(),fg="red",font=("Comic Sans MS",13)).grid(row=11,column=1)
        
        l3=tk.Label(m,text="Train Number ---> ",fg="blue",font=("Palatino Linotype",12)).grid(row=11,column=0)
        ll3=tk.Label(m,text=e3.get(),fg="red",font=("Comic Sans MS",13)).grid(row=11,column=1)
        
        l4=tk.Label(m,text="Train Name ---> ",fg="blue",font=("Palatino Linotype",13)).grid(column=0,row=12)
        ll4=tk.Label(m,text=e4.get(),fg="red",font=("Comic Sans MS",13)).grid(row=12,column=1)

        l5=tk.Label(m,text="Seat Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=10,column=3)
        ll5=tk.Label(m,text=e5.get(),fg="red",font=("Comic Sans MS",13)).grid(row=10,column=4)  
        
        l6=tk.Label(m,text="Coach Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=11,column=3)
        ll6=tk.Label(m,text=e6.get(),fg="red",font=("Comic Sans MS",13)).grid(row=11,column=4)
        
        l7=tk.Label(m,text="From ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=12,column=3)
        ll7=tk.Label(m,text=e7.get(),fg="red",font=("Comic Sans MS",13)).grid(row=12,column=4)
        
        l8=tk.Label(m,text="To ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=10,column=5)
        ll8=tk.Label(m,text=e8.get(),fg="red",font=("Comic Sans MS",13)).grid(row=10,column=6)
        
        l10=tk.Label(m,text="Distance ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=11,column=5)
        ll10=tk.Label(m,text=e9.get(),fg="red",font=("Comic Sans MS",13)).grid(row=11,column=6)
        
        l11=tk.Label(m,text="Amount ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=12,column=5)
        if(e6.get()=="S1" or e6.get()=="S2" or e6.get()=="S3" or e6.get()=="S4" or e6.get()=="S5" ):
            amo=int(e9.get())*1.5
            am=str(amo)
            ll10=tk.Label(m,text=am,fg="red",font=("Comic Sans MS",13)).grid(row=12,column=6)
        if(e6.get()=="A1" or e6.get()=="A2" or e6.get()=="A3"):
            amo=int(e9.get())*1.75
            am=str(amo)
            ll10=tk.Label(m,text=am,fg="red",font=("Comic Sans MS",13)).grid(row=12,column=6)
        
        for i in range(10):
            pn=str(random.randint(0,9))
            p+=pn
        l9=tk.Label(m,text="PNR Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=13,column=5)
        ll9=tk.Label(m,text=p,fg="red",font=("Comic Sans MS",13)).grid(row=13,column=6)
        
    else:
        m.destroy()
        
        

def gen(): 
    
    Msg=tk.messagebox.askquestion("Exit Application","Are you sure you exit application")
    if Msg=='yes':  
        m1=tk.Tk()
        
        global p
        l1=tk.Label(m1,text="Name ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=0,column=0)
        ll1=tk.Label(m1,text=e1.get(),fg="red",font=("Comic Sans MS",13)).grid(row=0,column=1)
        
        
        l2=tk.Label(m1,text="AGE ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=1,column=0)
        ll2=tk.Label(m1,text=e2.get(),fg="red",font=("Comic Sans MS",13)).grid(row=1,column=1)
        
        l3=tk.Label(m1,text="Train Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=2,column=0)
        ll3=tk.Label(m1,text=e3.get(),fg="red",font=("Comic Sans MS",13)).grid(row=2,column=1)
        
        l4=tk.Label(m1,text="Train Name ---> ",fg="blue",font=("Palatino Linotype",13)).grid(column=0,row=3)
        ll4=tk.Label(m1,text=e4.get(),fg="red",font=("Comic Sans MS",13)).grid(row=3,column=1)

        l5=tk.Label(m1,text="Seat Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=0,column=3)
        ll5=tk.Label(m1,text=e5.get(),fg="red",font=("Comic Sans MS",13)).grid(row=0,column=4)  
        
        l6=tk.Label(m1,text="Coach Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=1,column=3)
        ll6=tk.Label(m1,text=e6.get(),fg="red",font=("Comic Sans MS",13)).grid(row=1,column=4)
        
        l7=tk.Label(m1,text="From ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=2,column=3)
        ll7=tk.Label(m1,text=e7.get(),fg="red",font=("Comic Sans MS",13)).grid(row=2,column=4)
        
        l8=tk.Label(m1,text="To ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=3,column=3)
        ll8=tk.Label(m1,text=e8.get(),fg="red",font=("Comic Sans MS",13)).grid(row=3,column=4)
        
        l10=tk.Label(m1,text="Distance ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=1,column=5)
        ll10=tk.Label(m1,text=e9.get(),fg="red",font=("Comic Sans MS",13)).grid(row=1,column=6)
        
        l11=tk.Label(m1,text="Amount ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=2,column=5)
        if(e6.get()=="S1" or e6.get()=="S2" or e6.get()=="S3" or e6.get()=="S4" or e6.get()=="S5" ):
            amo=int(e9.get())*1.5
            am=str(amo)
            ll10=tk.Label(m1,text=am,fg="red",font=("Comic Sans MS",13)).grid(row=2,column=6)
        if(e6.get()=="A1" or e6.get()=="A2" or e6.get()=="A3"):
            amo=int(e9.get())*1.75
            am=str(amo)
            ll10=tk.Label(m1,text=am,fg="red",font=("Comic Sans MS",13)).grid(row=2,column=6)
        if(e9.get()==None):
            ll10=tk.Label(m1,text="0",fg="red",font=("Comic Sans MS",13)).grid(row=2,column=6)
        
        for i in range(10):
            pn=str(random.randint(0,9))
            p+=pn
        l9=tk.Label(m1,text="PNR Number ---> ",fg="blue",font=("Palatino Linotype",13)).grid(row=0,column=5)
        ll9=tk.Label(m1,text=p,fg="red",font=("Comic Sans MS",13)).grid(row=0,column=6)
    
        g=tk.Button(m1,text="Done",bd=5,command=done,width=9).grid(row=5,column=6)
        
        m1.mainloop()
        
    else:
        print()
    
    
    
    

def done():   
    
    print("NAME : %s\nAGE : %s\nTrain no. : %s\nTrain Name : %s\nSeat Number : %s\nCoach Number : %s" 
          % (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()))
    
    j=open("LIST.txt","a")
    j.write("\nName : ")
    j.writelines(e1.get())
    j.write("\nAGE : ")
    j.write(e2.get())
    j.write("\nTrain No. : ")
    j.write(e3.get())
    j.write("\nTrain Name : ")
    j.write(e4.get())
    j.write("\nSeat Number : ")
    j.write(e5.get())
    j.write("\nCoach Number: ")
    j.write(e6.get())
    j.write("\n______________________")
    j.close()    
    
    
    
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)
    e6.delete(0,tk.END)

    
    

#CREATING LABEL (NAME, AGE, TRAIN NUMBER, TRAIN NAME, SEAT NUMBER, COACH NUMBER, FROM, TO, DISTANCE, GENDER,CANCLELATION PASSWORD)
l1=tk.Label(m,text="NAME").grid(row=0)
l2=tk.Label(m,text="AGE").grid(row=1)
l3=tk.Label(m,text="Train Number").grid(row=2)
l4=tk.Label(m,text="Train Name").grid(column=3,row=0)
l5=tk.Label(m,text="Seat Number").grid(row=1,column=3)
l6=tk.Label(m,text="Coach Number").grid(row=3)
l7=tk.Label(m,text="From").grid(row=2,column=3)
l8=tk.Label(m,text="To").grid(row=3,column=3)
l9=tk.Label(m,text="Distance").grid(row=4,column=0)
l11=tk.Label(m,text="Gender").grid(row=4,column=3)
l12=tk.Label(m,text="Cancelation Password").grid(row=0,column=5)

#CREATING ENTRY SECTION FOR NAME
e1=tk.Entry(m,bd=5) #Making Entry box for passenger name
reg=m.register(correct1)
e1.config(validate="key",validatecommand=(reg,'%P'))

e2=tk.Entry(m,bd=5)
reg=m.register(correct2)
e2.config(validate="key",validatecommand=(reg,'%P'))

e3=tk.Entry(m,bd=5)

e3.insert(10, "1")

reg=m.register(correct3)
e3.config(validate="key",validatecommand=(reg,'%P'))

e4=tk.Entry(m,bd=5)
reg=m.register(correct4)
e4.config(validate="key",validatecommand=(reg,'%P'))


e7=tk.Entry(m,bd=6)
reg=m.register(correct7)
e7.config(validate="key",validatecommand=(reg,'%P'))

e8=tk.Entry(m,bd=5)
reg=m.register(correct8)
e8.config(validate="key",validatecommand=(reg,'%P'))

e9=tk.Entry(m,bd=5)
reg=m.register(correct9)
e9.config(validate="key",validatecommand=(reg,'%P'))
e9.insert(10, "1")

e12=tk.Entry(m,bd=5)


e5=tk.Spinbox(m,from_=1,to=49,bd=5,width=18)
reg=m.register(correct5)
e5.config(validate="key",validatecommand=(reg,'%P'))


t = ('Male','Female','Transgender')
v = t[2]
var = tk.StringVar()
var.set(v)
e10 = tk.Spinbox(m, values=t, textvariable=var, width=18,bd=5)
e10.place(x=150, y=5)

reg=m.register(correct10)
e10.config(validate="key",validatecommand=(reg,'%P'))


t = ('S1','S2','S3','S4','S5','A1','A2','A3')
v = t[3]
var = tk.StringVar()
var.set(v)
e6 = tk.Spinbox(m, values=t, textvariable=var, width=18,bd=5)
e6.place(x=150, y=5)

reg=m.register(correct6)
e6.config(validate="key",validatecommand=(reg,'%P'))

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=0,column=4)
e5.grid(row=1,column=4)
e6.grid(row=3,column=1)
e7.grid(row=2,column=4)
e8.grid(row=3,column=4)
e9.grid(row=4,column=1)
e10.grid(row=4,column=4)
e12.grid(row=1,column=5)



b=tk.Button(m,text="DONE",bd=5,command=gen,width=9).grid(row=5,column=2)
b1=tk.Button(m,text="Confirm",bd=5,command=confirma,width=9).grid(row=2,column=5)



m.mainloop()
