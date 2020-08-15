

for i in range(1,3):
    print("Produit n°", i, ":")
    N=input("Donner le nom de votre produit: ")
    P=int(input(" Donner le prix:  "))
    Q=int(input(" Donne la quantité:  "))
    montant=P*Q
    if montant<5000:
        montant=montant-((montant*10)/100)
    elif montant<20000:
        montant=montant-((montant*20)/100)
    elif montant>20000:
        montant=montant-((montant*30)/100)
  
mt=montant*(i)

print(" Votre montant total est :"   , mt, "DT")
