from tkinter import*
aken=Tk
aken.title("akna nimetus")
aken.geometry("400x600")
nupp=Button(aken,text="Vajuta \nsiia",height=4,width=15,bg="blue",fg="green", font="Arial 36") #.pack(side=TOP) command=vajutamine()
nupp.pack(side=TOP) # grid(), place()
nupp.bind('<Button-3>',vajutamine)
aken.mainloop()