

from tkinter import*

fen1=Tk()
text1=Label(fen1,text='G.M everyone !',fg='violet')
text1.pack()
b=Button(fen1,text='Quit',command=fen1.destroy)
b.pack()

text1=Label(fen1,text='Bye Bye!',fg='blue')
text1.pack()
champ_label=Label(fen1,text='contenu de notre champ label')
champ_label.pack()
var_texte=StringVar()
ligne_texte=Entry(fen1,textvariable=var_texte,width=30)
ligne_texte.pack()
champ_label=Label(fen1,text="Saisir vos options")
champ_label.pack()
var_case1=IntVar()
case1=Checkbutton(fen1,text="programmation",variable=var_case1)
case1.pack()
var_case2=IntVar()
case2=Checkbutton(fen1,text="web",variable=var_case2)
case2.pack()

champ_label=Label(fen1,text="choisir votre couleur:")
champ_label.pack()
var_choix=StringVar()

choix_pink=Radiobutton(fen1,text="Pink",variable=var_choix,value="pink")
choix_green=Radiobutton(fen1,text="Green",variable=var_choix,value="green")
choix_orange=Radiobutton(fen1,text="Orange",variable=var_choix,value="orange")

choix_pink.pack()
choix_green.pack()
choix_orange.pack()
fen1.mainloop()
