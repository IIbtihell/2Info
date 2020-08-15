x1=0
x2=0
nb=0
nom1= input('saisir nom 1')
nom2= input('saisir nom 2')
while x1<50 and x2<50 and nb<5:
   nb=nb+1
   print( 'essez numero',nb)
   m1=input( 'donner mot 1')
   m2=input( 'donner mot 2')
   x1=x1+len(m1)
   x2=x2+len(m2)
if(x1>50):
   print (nom1,' gagnant avec bonnus')
elif(x2>50):
   print (nom2,' gagnant avec bonnus')
if nb==5:
   if x1>x2:
      print(nom1,' gagnant sans bonnus')
   elif x2>x1:
      print(nom2,' gagnant sans bonnus')
   else:
       print('egalite')
       
