print("Bienvenue cher client!")
montant=0
budget=int(input("Donner votre budget: "))

while montant<budget:

    N=input("Donner le nom de votre produit: ")
    P=int(input(" Donner le prix:  "))
    Q=int(input(" Donne la quantite:  "))
    montant=P*Q
    if montant<5000:
        montant=montant-((montant*10)/100)
    if montant<20000:
        montant=montant-((montant*20)/100)
    if montant>20000:
        montant=montant-((montant*30)/100)
  
montant=montant

print(" Votre montant total est :"   , montant, "DT")
