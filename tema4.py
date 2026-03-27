import json

# Citire din JSON
def incarca_date():
    f = open("competitori.json", "r")
    lista = json.load(f)
    f.close()
    return lista

# Afisare competitori
def afisare(lista):
    if not lista:
        print("Lista este goala.")
        return
    for c in lista:
        print(c["nume"], "-", c["punctaj"], "puncte,", c["timp"], "sec")

# Adaugare competitor
def adauga(lista):
    nume = input("Nume: ")
    if nume == "":
        print("Numele nu poate fi gol!")
        return
    punctaj = int(input("Punctaj: "))
    timp = int(input("Timp: "))

    lista.append({
        "nume": nume,
        "punctaj": punctaj,
        "timp": timp
    })

# Actualizare competitor
def actualizeaza(lista):
    nume = input("Numele competitorului: ")
    for c in lista:
        if c["nume"] == nume:
            c["punctaj"] = int(input("Noul punctaj: "))
            c["timp"] = int(input("Noul timp: "))
            print("Actualizat!")
            return
    print("Competitor inexistent!")

# Funcție de comparare
def este_mai_bun(a, b):
    if a["punctaj"] != b["punctaj"]:
        return a["punctaj"] > b["punctaj"]
    if a["timp"] != b["timp"]:
        return a["timp"] < b["timp"]
    return a["nume"] < b["nume"]

# Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]
    stanga = []
    dreapta = []

    for x in lista[1:]:
        if este_mai_bun(x, pivot):
            stanga.append(x)
        else:
            dreapta.append(x)

    return quicksort(stanga) + [pivot] + quicksort(dreapta)

def clasament(lista):
    if not lista:
        print("Lista este goala.")
        return

    lista_sortata = quicksort(lista)

    print("\nClasament:")
    print("Loc | Nume | Punctaj | Timp")

    loc = 1
    for i in range(len(lista_sortata)):
        if i > 0:
            prev = lista_sortata[i-1]
            curr = lista_sortata[i]
            if prev["punctaj"] != curr["punctaj"] or prev["timp"] != curr["timp"]:
                loc = i + 1

        c = lista_sortata[i]
        print(loc, "|", c["nume"], "|", c["punctaj"], "|", c["timp"])

def statistici(lista):
    if not lista:
        print("Lista este goala.")
        return

    punctaje = [c["punctaj"] for c in lista]
    timpi = [c["timp"] for c in lista]

    print("\nStatistici:")
    print("Numar competitori:", len(lista))
    print("Punctaj maxim:", max(punctaje))
    print("Punctaj minim:", min(punctaje))
    print("Media:", sum(punctaje)/len(punctaje))
    print("Cel mai bun timp:", min(timpi))

def meniu():
    lista = incarca_date()

    while True:
        print("\n1. Afisare")
        print("2. Adaugare")
        print("3. Actualizare")
        print("4. Clasament")
        print("5. Statistici")
        print("0. Iesire")

        opt = input("Alege optiunea: ")

        if opt == "1":
            afisare(lista)
        elif opt == "2":
            adauga(lista)
        elif opt == "3":
            actualizeaza(lista)
        elif opt == "4":
            clasament(lista)
        elif opt == "5":
            statistici(lista)
        elif opt == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida!")

# Pornire program
meniu()