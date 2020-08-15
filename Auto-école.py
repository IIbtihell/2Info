
from tkinter import*

fen1=Tk()
fen1.geometry("400x400")
text=Label(fen1,text='Auto-école',fg='purple')
text.grid(row=0,   column=1)
txt1=Label(fen1,text ='Nom et prénom :')
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

fen1.mainloop()
