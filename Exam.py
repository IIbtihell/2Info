from tkinter import*
fen1=Tk()
text1=Label(fen1,text="Nombre1: ", fg="purple")
text2=Label(fen1,text="Nombre2: ", fg="purple")
e1=Entry(fen1)
e2=Entry(fen1)
text1.grid(row=0)
text2.grid(row=1)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b=Button(fen1,text="Calculer", bg="green")
b.grid(row=2,column=1)

res=Label(fen1,text=" ")
res.grid(row=3,column=1)

def fonction():
    n1=int(e1.get())
    n2=int(e2.get())
    a=n1//10
    b=n1%10
    T=a*1000+n2*10+b
    res.config(text="Totale:"+" "+ str(T))
b.config(command=fonction)


fonction()
fen1.mainloop()

