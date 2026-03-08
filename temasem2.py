produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]

reducere_curenta = 0


# functie afisare meniu
def afisare_meniu(produse,preturi,stoc):
 print("\nProduse disponibile:")
 for i in range(len(produse)):
  print(i,produse[i],preturi[i],"lei","stoc:",stoc[i])


# adaugare produs
def adaugare_produs(cant_comanda,stoc,index,cantitate):
 if index>=0 and index<len(stoc):
  if cantitate>0:
   disponibil=stoc[index]-cant_comanda[index]
   if cantitate<=disponibil:
    cant_comanda[index]=cant_comanda[index]+cantitate
    print("produs adaugat")
   else:
    print("stoc insuficient")
  else:
   print("cantitate invalida")
 else:
  print("index gresit")


# scadere produs
def scadere_produs(cant_comanda,index,cantitate):
 if index>=0 and index<len(cant_comanda):
  if cantitate>0:
   if cantitate<=cant_comanda[index]:
    cant_comanda[index]=cant_comanda[index]-cantitate
    print("produs scazut")
   else:
    print("nu exista atatea produse")
  else:
   print("cantitate invalida")
 else:
  print("index gresit")


# calcul total
def calcul_total(cant_comanda,preturi):
 total=0
 for i in range(len(cant_comanda)):
  total=total+cant_comanda[i]*preturi[i]
 return total


# stabilire reducere
def stabilire_reducere(total,tip):
 reducere=0

 if tip=="student":
  if total>=30:
   reducere=total*0.10
  else:
   print("Total insuficient pentru student")

 if tip=="happy":
  if total>=50:
   reducere=total*0.15
  else:
   print("Total insuficient pentru happy")

 if tip=="cupon":
  if total>=25:
   reducere=7
  else:
   print("Total insuficient pentru cupon")

 if reducere>total:
  reducere=total

 return reducere


# afisare bon
def afisare_bon(produse,preturi,cant_comanda,reducere):

 total=0
 print("\nBON")

 for i in range(len(produse)):
  if cant_comanda[i]>0:
   subtotal=cant_comanda[i]*preturi[i]
   total=total+subtotal
   print(produse[i],"x",cant_comanda[i],"=",subtotal,"lei")

 print("total:",total)
 print("reducere:",reducere)
 print("total final:",total-reducere)


# finalizare comanda
def finalizare_comanda(stoc,cant_comanda):
 for i in range(len(stoc)):
  stoc[i]=stoc[i]-cant_comanda[i]
  cant_comanda[i]=0


# anulare comanda
def anulare_comanda(cant_comanda):
 for i in range(len(cant_comanda)):
  cant_comanda[i]=0


while True:

 print("\nMENIU")
 print("1 afisare meniu")
 print("2 adaugare produs")
 print("3 scadere produs")
 print("4 aplicare reducere")
 print("5 finalizare comanda")
 print("6 anulare comanda")
 print("0 iesire")

 optiune=input("optiune:")

 if optiune=="1":

  afisare_meniu(produse,preturi,stoc)

 elif optiune=="2":

  index=int(input("index produs:"))
  cant=int(input("cantitate:"))
  adaugare_produs(cant_comanda,stoc,index,cant)

 elif optiune=="3":

  index=int(input("index produs:"))
  cant=int(input("cantitate de scazut:"))
  scadere_produs(cant_comanda,index,cant)

 elif optiune=="4":

  total=calcul_total(cant_comanda,preturi)

  if total==0:
   print("Comanda este goala")

  else:

   print("1 student")
   print("2 happy")
   print("3 cupon")
   print("4 fara reducere")
   print("5 inapoi")

   alegere=input("alege:")

   if alegere=="1":
    reducere_curenta=stabilire_reducere(total,"student")

   elif alegere=="2":
    reducere_curenta=stabilire_reducere(total,"happy")

   elif alegere=="3":
    reducere_curenta=stabilire_reducere(total,"cupon")

   elif alegere=="4":
    reducere_curenta=0

   elif alegere=="5":
    print("revenire la meniu")

   else:
    print("optiune invalida")

 elif optiune=="5":

  total=calcul_total(cant_comanda,preturi)

  if total==0:
   print("nu exista produse in comanda")

  else:

   if reducere_curenta>total:
    reducere_curenta=total

   afisare_bon(produse,preturi,cant_comanda,reducere_curenta)
   finalizare_comanda(stoc,cant_comanda)
   reducere_curenta=0

 elif optiune=="6":

  anulare_comanda(cant_comanda)
  reducere_curenta=0
  print("comanda anulata")

 elif optiune=="0":

  print("program inchis")
  break

 else:

  print("optiune invalida")