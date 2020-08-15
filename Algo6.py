from Tkinter import*
fen1=Tk()

txt1=Label(fen1,text ='Donner N à  2 chiffres  :'  ,fg="pink" )
e1=Entry(fen1)
txt1.grid(row=0)
e1.grid(row=0,   column=1)
b=Button(fen1,    text='Inverser')
b.grid(row=2)
res=Label(fen1,text='')
res.grid(row=3)
def fonction ():
    contenu1=e1.get()
    b.config(command=fonction)
    res.config("Resultat" ,text=N1 ,fg='blue' )
while N<10 or N>99:
   N=int(input("Donner N à  2 chiffres  : "))
   

b=N // 10
a=N % 10
N1=a*10+b
print("Résultat=" ,N1)

print("Fin Ex1")

fonction()
fen1.mainloop()
