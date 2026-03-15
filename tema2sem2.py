import csv
glosar={
  "variabilă": {
    "definitie": "nume asociat unei valori",
    "categorie": "fundamente",
    "exemplu": "x = 10"
  },
  "dicționar": {
    "definitie": "structură de date bazată pe perechi cheie-valoare",
    "categorie": "structuri de date",
    "exemplu": "{'a': 1, 'b': 2}"
  }
}
def afisare_meniu():
    print("---MENIU GLOSAR---")
    print("Optiuni:")
    print("1. Adaugare termen")
    print("2. Cautare exacta termen")
    print("3. Cautare partiala termeni")
    print("4. Actualizare termen")
    print("5. Stergere termen")
    print("6. Afisare glosar")
    print("7. Statistici")
    print("8. Salvare")
    print("9. Incarcare")
    print("0. Iesire")
def afisare_glosar():
    for termen in glosar:
        print("Termen:", termen)
        print("Definitie:", glosar[termen]["definitie"])
        print("Categorie:", glosar[termen]["categorie"])
        print("Exemplu:", glosar[termen]["exemplu"])
def adaugare_termen():
    termen=input("Introduceti termenul: ")
    definitie=input("Introduceti definitia: ")
    categorie=input("Introduceti categoria: ")
    exemplu=input("Introduceti exemplu: ")
    if termen in glosar:
        print("Termenul deja exista in glosar")
        return
    glosar[termen]={
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu,
    }
def cautare_exacta():
    termen=input("Introduceti termenul: ")
    if termen in glosar:
        print(glosar[termen])
    else:
        print("Termenul nu exista in glosar")
def cautare_partiala():
    fragment= input("Introduceti fragment: ")
    gasit=False
    for termen in glosar:
        if fragment in termen:
            gasit=True
            print("Termen:", termen)
            print("Definitie:", glosar[termen]["definitie"])
            print("Categorie:", glosar[termen]["categorie"])
            print("Exemplu:", glosar[termen]["exemplu"])
            print()
    if gasit==False:
            print("Nu exista termeni care contin acest fragment")
def actualizare_termen():
    termen=input("Introduceti termenul: ")
    print("Ce doriti sa modificati? (definitie/categorie/exemplu)")
    camp=input("Introduceti camp: ")
    if termen not in glosar:
        print("Termenul nu exista in glosar")
        return
    if camp not in glosar[termen]:
        print("Camp nu exista in glosar")
        return
    valoare=input("Introduceti valoare: ")
    glosar[termen][camp]=valoare
    print("Actualizarea a fost realizata.")
def stergere_termen():
    termen=input("Introduceti termenul: ")
    if termen in glosar:
        del glosar[termen]
        print("Termenul a fost sters din glosar.")
    else:
        print("Termenul nu exista in glosar")
def statistici():
    total_termeni = len(glosar)
    categorii = {}
    for termen in glosar:
        categ = glosar[termen]["categorie"]
        if categ not in categorii:
            categorii[categ] = 0
        categorii[categ] += 1
    print("Numarul total de termeni este : ", total_termeni)
    print("Termenii pe categorii sunt : ")
    for categ, num in categorii.items():
        print(categ, " : ", num)
def salvare_csv():
    with open("glosar.csv", "w", newline="", encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["termen", "definitie", "categorie", "exemplu"])
        for termen, info in glosar.items():
            writer.writerow([termen, info["definitie"], info["categorie"], info["exemplu"]])
        print("Glosarul a fost salvat.")

def incarcare_csv():
    try:
        with open("glosar.csv", "r", encoding="utf-8") as f:
            reader=csv.DictReader(f)
            glosar.clear()
            for row in reader:
                glosar[row["termen"]]={
                    "definitie": row["definitie"],
                    "categorie": row["categorie"],
                    "exemplu": row["exemplu"]
                }
        print("Glosarul a fost incarcat.")
    except FileNotFoundError:
        print("Fisierul nu exista.")


if __name__ == '__main__':
    while(True):
        afisare_meniu()
        optiune=input("Alege o optiune: ")
        if optiune=="6":
            afisare_glosar()
        elif optiune=="1":
            adaugare_termen()
        elif optiune=="2":
            cautare_exacta()
        elif optiune=="3":
            cautare_partiala()
        elif optiune=="4":
            actualizare_termen()
        elif optiune=="5":
            stergere_termen()
        elif optiune=="7":
            statistici()
        elif optiune=="8":
            salvare_csv()
        elif optiune=="9":
            incarcare_csv()
        elif optiune=="0":
            print("Iesire")
            break
        else:
            print("Nu exista acteasta optiune")


