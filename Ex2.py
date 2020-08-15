from Tkinter import*
from tkinter import messagebox as mbox
from random import randint
fen1 = Tk() 
CHOIX = ["A", "Z", "E", "R", "T" ,"Y", "U","I", "O","p","Q", "S","D","F","G"]
numchoix = randint(0, 14)
choixOrdinateur=CHOIX[numchoix] 
captcha=" " 

for i in range(8): 
  numchoix=randint(0,14) 
  choixOrdinateur=CHOIX[numchoix]
  captcha=captcha+choixOrdinateur
  
def gerer (): 
  b1.config(command=gerer)
  cap.config(text='Captcha ='+captcha)
cap = Label(fen1, text = 'Captcha :') 
re=Label(fen1, text='Reecrire ce Captcha') 
e1=Entry(fen1) 
b1=Button(fen1, text="Gerer", bg="pink")
b1.grid(row =0)
cap.grid(row =1, column =1)
re.grid(row =2, column=0)
e1.grid(row=2,column=1) 
b2=Button(fen1, text="Verifier", bg="purple")
b2.grid(row=3)
res=Label(fen1, text=' ')
res.grid(row=4)
def verif():
  C2=e1.get() 
  if C2==captcha:
    mbox.showinfo("Information", " Tres bien Captcha correct")
  else:
    mbox.showerror("Error", "Desole captcha Incorrect") 
b1.config (command=gerer)
b2.config (command=verif) 
fen1.mainloop()
