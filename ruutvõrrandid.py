from tkinter import*
from math import*
import matplotlib.pyplot as plt 
import numpy as np
global D, t
D=-1
t="no sol"
graf=False

def lahenda():
    global a,b,c,D, t
    if(a.get()!=""and b.get()!=""and c.get()!=""):
        if type(a) and type(b) and type(c)!=str:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4+a_*c_
            graf=True
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_},\nX2={x2_}"
            graf=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="ruutjuur puudub"
            graf=False
            vastus.configure(text=f"D={D}\n{t}")
            a.configure(bg="Lightblue")
            b.configure(bg="Lightblue")
            c.configure(bg="Lightblue")
    else:
        t="ruutjuur puudub"
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
        graf=True
    return graf,D,t
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x=np.arange(x0-10,x0+10,0.5)#min max step
        y=a_*x*x+b_*x+c_
        fig=plt.figure()
        plt.plot(x,y,"b:o")
        plt.title("ruutvõrrand")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"porabooli tipp ({x0},{y0})"
    else:
        text=f"ei ole võimalusi teha graafikut"
    vastus.configure(text=f"D={D}\n{text}")
aken=Tk()
aken.geometry("650x200")
aken.title("ruutvõrrand")
lbl=Label(aken,text="ruutvõrrandite lahendus",font="Calibri 26",fg="green",bg="lightblue")
lbl.pack()
vastus=Label(aken,text="lahendus",height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
lah=Button(aken,text="lahenda",font="Calibry 26", fg="black",bg="green",relief=GROOVE,command=lahenda)
lah.pack(side=RIGHT)
grafik=Button(aken,text="graafik",font="Calibry 26", fg="black",bg="green",relief=GROOVE,command=graafik)
grafik.pack(side=RIGHT)
a=Entry(aken,font="Calibri 26",fg="green",bg="lightblue",width=3)
a.pack(side=LEFT) #padx=10,pady=10
x2=Label(aken,text="x**2+",font="Calibri 26",fg="green",padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26",fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26",fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Calibri 26",fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26",fg="green")
y.pack(side=LEFT)

aken.mainloop()