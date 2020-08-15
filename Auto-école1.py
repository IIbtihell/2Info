from Tkinter import*
from Tkinter import messagebox as mbox


fen1=Tk()
fen1.geometry("400x400")
text=Label(fen1,text='Auto-ecole',fg='purple')
text.grid(row=0,   column=1)
txt1=Label(fen1,text ='Nom et prenom :')
txt2=Label(fen1,text ='G.S.M  :')
txt3=Label(fen1,text ='C.I.N  :')

e1=Entry(fen1)
e2=Entry(fen1)
e3=Entry(fen1)

txt1.grid(row=1)
txt2.grid(row=2)
txt3.grid(row=3)

e1.grid(row=1,   column=1)
e2.grid(row=2,   column=1)
e3.grid(row=3,   column=1)


champ_label=Label(fen1,text="Saisir vos options:")
champ_label.grid(row=4)
champ_label=Label(fen1,text="Circuit :")
champ_label.grid(row=5)
var_case1=IntVar()
case1=Checkbutton(fen1,text="Kalaa",variable=var_case1)
case1.grid(row=6,      column=0)
var_case2=IntVar()
case2=Checkbutton(fen1,text="Akouda",variable=var_case2)
case2.grid(row=6,      column=1)
var_case1=IntVar()
case3=Checkbutton(fen1,text="Sousse",variable=var_case1)
case3.grid(row=6,      column=2)

champ_label=Label(fen1,text="Voitures :")
champ_label.grid(row=7)
var_choix=StringVar()

choix_Polo=Radiobutton(fen1,text="Polo",variable=var_choix,value="Polo")
choix_Peugeot=Radiobutton(fen1,text="Peugeot",variable=var_choix,value="Peugeot")
choix_Clio=Radiobutton(fen1,text="Clio",variable=var_choix,value="Clio")

choix_Polo.grid(row=8,   column=0)
choix_Peugeot.grid(row=8, column=1)
choix_Clio.grid(row=8,   column=2)
txt5=Label(fen1,text ='Nombre H  :')
txt5.grid(row=9)

txt6=Label(fen1,text ='Prix H  :')
txt6.grid(row=10)

e4=Entry(fen1)
e5=Entry(fen1)

e4.grid(row=9,   column=1)
e5.grid(row=10,   column=1)

b=Button(fen1,    text='valider')
b.grid(row=11,  column=1)
res=Label(fen1, text='resultat')
res.grid(row=12, column=1)

def valider ():
    contenu1=e4.get()
    contenu2=e5.get()
    montant=contenu1*contenu2
    if montant<45000:
        montant=montant-((montant*10)/100)
    elif montant<90000:
        montant=montant-((montant*20)/100)
    elif montant<180000:
        montant=montant-((montant*30)/100)
    else:
        montant=montant-((montant*40)/100)
    b.config(command=valider)
    res.config(text='resultat-'+str(montant),fg='blue')
    mbox.showinfo("Information", 'resultat ='+str(montant))
    if IntVar() == 'kalaa' and StringVar() == 'Polo':
      mbox.showinfo('resultat =('votre circuit : 'Kalaa', votre voiture :'Polo')')
    if IntVar() == 'Akouda' and StringVar() == 'Polo':
      mbox.showinfo('resultat =('votre circuit : 'Akouda', votre voiture :'Polo')')
    if IntVar() == 'Sousse' and StringVar() == 'Polo':
       mbox.showinfo('resultat =('votre circuit : 'Sousse', votre voiture :'Polo')')
    if IntVar() == 'Kalaa' and StringVar() == 'Peugeot':
      mbox.showinfo('resultat =('votre circuit : 'kalaa', votre voiture :'Peugeot')')
    if IntVar() == 'Akouda' and StringVar() == 'Peugeot':
      mbox.showinfo('resultat =('votre circuit : 'Akouda', votre voiture :'Peugeot')')
    if IntVar() == 'Sousse' and StringVar() == 'Peugeot':
       mbox.showinfo('resultat =('votre circuit : 'Sousse', votre voiture :'Peugeot')')
    if IntVar() == 'kalaa' and StringVar() == 'Clio':
       mbox.showinfo('resultat =('votre circuit : 'kalaa', votre voiture :'Clio')')
    if IntVar() == 'Akouda' and StringVar() == 'Clio':
      mbox.showinfo('resultat =('votre circuit : 'Akouda', votre voiture :'Clio')')
    if IntVar() == 'Sousse' and StringVar() == 'Clio':
      mbox.showinfo('resultat =('votre circuit : 'Sousse', votre voiture :'Clio')')


              
         


fen1.mainloop()

