from tkinter import*
from math import*
import matplotlib.pyplot as plt 
import numpy as np
global D, t
D=-1
t="ruutjuur puudub"
graf=False

def lahenda():
    global a,b,c,D, t
    if(a.get()!=""and b.get()!=""and c.get()!=""):
        if type(a) and type(b) and type(c)!=str:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4+a_*c_
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
            a.configure(bg="Lightblue")
            b.configure(bg="Lightblue")
            c.configure(bg="Lightblue")
        vastus.configure(text=f"D={D}\n{t}")
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
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        nupp_veel.config(text="väiksenda aken")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        nupp_veel.config(text="suurenda aken")
        t=0

def vaal():
    x1=np.arange(0,9.5,0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)#min max step
    y2=0.04*x2*x2-3
    x3=np.arange(-9,-2.5,0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.3,0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5)#min max step
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)#min max step
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("ruutvõrrand")
    plt.ylabel("y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def prillid():
    x1=np.arange(-9,-1,0.5)#min max step
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9,0.5)#min max step
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-1,0.5)#min max step
    y3=(1/4)*(x3+5)**2-3
    x4=np.arange(1,9,0.5)#min max step
    y4=(1/4)*(x4-5)**2-3
    x5=np.arange(-9,-6,0.5)#min max step
    y5=-(x5+7)**2+5
    x6=np.arange(6,9,0.5)#min max step
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1,0.5)#min max step
    y7=(-0.5*x7)**2+0.7
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("ruutvõrrand")
    plt.ylabel("y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()
def vihmavari():
    pass
aken=Tk()
aken.geometry("650x200")
aken.title("ruutvõrrand")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)

lbl=Label(f1,text="ruutvõrrandite lahendus",font="Calibri 26",fg="green",bg="lightblue")
lbl.pack()
vastus=Label(f1,text="lahendus",height=4,width=60,bg="yellow")
vastus.pack(side=BOTTOM)
lah=Button(f1,text="lahenda",font="Calibry 26", fg="black",bg="green",relief=GROOVE,command=lahenda)
lah.pack(side=RIGHT)
grafik=Button(f1,text="graafik",font="Calibry 26", fg="black",bg="green",relief=GROOVE,command=graafik)
grafik.pack(side=RIGHT)
a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
a.pack(side=LEFT) #padx=10,pady=10
x2=Label(f1,text="x**2+",font="Calibri 26",fg="green",padx=10)
x2.pack(side=LEFT)
b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
b.pack(side=LEFT)
x=Label(f1,text="x+",font="Calibri 26",fg="green")
x.pack(side=LEFT)
c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue",width=3)
c.pack(side=LEFT)
y=Label(f1,text="=0",font="Calibri 26",fg="green")
y.pack(side=LEFT)
nupp_veel=Button(f2,text="Suurenda aken",font="Calibri 26",bg="green",command=veel)
nupp_veel.pack(side=TOP)
var=IntVar()
r1=Radiobutton(aken,text="vaal",variable=var,var=1,font="Calibri 26",command=vaal)
r2=Radiobutton(aken,text="prillid",variable=var,var=2,font="Calibri 26",command=prillid)
r3=Radiobutton(aken,text="vihmavari",variable=var,var=3,font="Calibri 26",command=vihmavari)
r1.pack()
#r2.pack()
#r3.pack()


aken.mainloop()