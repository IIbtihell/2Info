from tkinter import*


fen1=Tk()
def calculer ():
    c1=int(e1.get())
    c2=int(e2.get())
    montant=c1*c2
    if montant<2000000:
        montant=montant-((montant*10)/100)
    elif montant<4000000:
        montant=montant-((montant*20)/100)
    elif montant<5000000:
        montant=montant-((montant*30)/100)
    else:
        montant=montant-((montant*40)/100)
    res.config(text='resultat='+str(montant),fg='red')
txt1=Label(fen1,text= 'prix unitaire')
txt2=Label(fen1,text= 'quantite')
e1=Entry(fen1)
e2=Entry(fen1)
txt1.grid(row=0)
txt2.grid(row=1)
e1.grid(row=0,   column=1)

e2.grid(row=1,   column=1)

B=Button(fen1,   text="calculer",command=calculer)
B.grid(row=2)

res=Label(fen1,text='resultat ')
res.grid(row=3)


fen1.mainloop( )
