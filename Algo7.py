from random import randint
score=0
score1=0
while score<10 and score1<10 :
  CHOIX=["rock","paper","scissors"]
  choixJoueur=input("Choose rock , paper, scissors : ")
  print("u choose :", choixJoueur )
  numchoix=randint(0,2)
  choixOrdinateur=CHOIX[numchoix]
  print("the computer choose",CHOIX[numchoix])
  if choixJoueur==choixOrdinateur:
    print("u had the same choice" , choixJoueur, "and u are equal  ")
  elif choixJoueur=="rock":
   if choixOrdinateur == "paper":
     score1=score1+5
     print(" paper covers the rock, u loose , Pc score:", score1)
  elif choixOrdinateur == "scissors":
     print(" scissors are broken by the rock,u win, ur score:", score)
     score=score+5
  elif choixJoueur=="paper":
   if choixOrdinateur=="scissors":
     print("scissors cut the paper, u loose, Pc score:", score1)
     score1=score1+5
  elif choixJoueur=="scissors":
   if choixOrdinateur=="rock":
     print(" scissors are broken by the rock, u loose, Pc score:", score1)
     score1=score1+5
   if choixOrdinateur=="paper":
     print("scissors cut the paper, u win,ur score:", score)
     score=score+5
   if score1<score:
     print("CONGRATULATIONS, U WIN!")
     print("ur score:", score)
     print("Pc score:", score1)
   elif score1>score:
     print("SADLY U LOOSE!")
     print("ur score:", score)
     print("Pc score:", score1)
   else:
     print("EQUALITY!")
     print("ur score:", score)
     print("Pc score:", score1)
print("EXIT")   
   

