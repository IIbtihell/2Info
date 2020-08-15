from Tkinter import*
fen1=Tk()
txt1=Label(fen1,text ='Nom:')
txt2=Label(fen1,text ='Prenon:')
e1=Entry(fen1)
e2=Entry(fen1)
txt1.grid(row=0)
txt2.grid(row=1)
e1.grid(row=0,   column=1)

e2.grid(row=1,   column=1)

b=Button(fen1,    text='valider')
b.grid(row=2)

res=Label(fen1,text='')
res.grid(row=3)


def fonction ():
    contenu1=e1.get()
    contenu2=e2.get()
    b.config(command=fonction)
    res.config (text="bonjour  "+contenu1+"  "+contenu2)


fonction()
fen1.mainloop()


    
