import csv
import json

def citeste_produse_csv(fisier):
    produse = {}
    f = open(fisier, 'r')
    continut = list(csv.reader(f))
    f.close()

    for linie in continut:
        if linie[0] == "id":
            continue

        id_produs = linie[0]
        nume = linie[1]
        pret = float(linie[2])
        stoc = int(linie[3])

        produse[id_produs] = {
            "nume": nume,
            "pret": pret,
            "stoc": stoc
        }
    return produse


def citeste_reduceri_json(fisier):
    f = open(fisier, 'r')
    reduceri = json.load(f)
    f.close()
    return reduceri


def scrie_bon_txt(fisier, text):
    f = open(fisier, 'w')
    f.write(text)
    f.close()


produse = citeste_produse_csv("produse.csv")
reduceri = citeste_reduceri_json("reduceri.json")

comanda = {}   # in loc de lista
reducere_curenta = 0


def afisare_meniu(produse):
    print("\nProduse disponibile:")
    for id_produs in produse:
        p = produse[id_produs]
        print(id_produs, p["nume"], p["pret"], "lei", "stoc:", p["stoc"])


def adaugare_produs(comanda, produse, id_produs, cantitate):
    if id_produs in produse:
        if cantitate > 0:
            stoc = produse[id_produs]["stoc"]
            deja = comanda.get(id_produs, 0)

            if cantitate <= stoc - deja:
                comanda[id_produs] = deja + cantitate
                print("produs adaugat")
            else:
                print("stoc insuficient")
        else:
            print("cantitate invalida")
    else:
        print("id invalid")


def scadere_produs(comanda, id_produs, cantitate):
    if id_produs in comanda:
        if cantitate > 0:
            if cantitate < comanda[id_produs]:
                comanda[id_produs] -= cantitate
            else:
                del comanda[id_produs]
            print("produs actualizat")
        else:
            print("cantitate invalida")
    else:
        print("produsul nu este in comanda")


def calcul_total(comanda, produse):
    total = 0
    for id_produs in comanda:
        total += comanda[id_produs] * produse[id_produs]["pret"]
    return total


def stabilire_reducere(total, tip, reduceri):
    if tip not in reduceri:
        return 0

    r = reduceri[tip]

    if total < r["prag"]:
        print("Prag neindeplinit")
        return 0

    if r["tip"] == "procent":
        return total * r["valoare"] / 100
    else:
        return r["valoare"]


def afisare_bon(produse, comanda, reducere):
    total = 0
    text = "\nBON\n"
    print("\nBON")

    for id_produs in comanda:
        cant = comanda[id_produs]
        pret = produse[id_produs]["pret"]
        nume = produse[id_produs]["nume"]

        subtotal = cant * pret
        total += subtotal

        print(nume, "x", cant, "=", subtotal, "lei")
        text += f"{nume} x {cant} = {subtotal} lei\n"

    print("total:", total)
    print("reducere:", reducere)
    print("total final:", total - reducere)

    text += f"total: {total}\n"
    text += f"reducere: {reducere}\n"
    text += f"total final: {total - reducere}\n"

    return text


def finalizare_comanda(produse, comanda):
    for id_produs in comanda:
        produse[id_produs]["stoc"] -= comanda[id_produs]
    comanda.clear()


def anulare_comanda(comanda):
    comanda.clear()

while True:
    print("\nMENIU")
    print("1 afisare meniu")
    print("2 adaugare produs")
    print("3 scadere produs")
    print("4 aplicare reducere")
    print("5 finalizare comanda")
    print("6 anulare comanda")
    print("0 iesire")

    optiune = input("optiune:")

    if optiune == "1":
        afisare_meniu(produse)

    elif optiune == "2":
        id_produs = input("id produs:")
        cant = int(input("cantitate:"))
        adaugare_produs(comanda, produse, id_produs, cant)

    elif optiune == "3":
        id_produs = input("id produs:")
        cant = int(input("cantitate de scazut:"))
        scadere_produs(comanda, id_produs, cant)

    elif optiune == "4":
        total = calcul_total(comanda, produse)

        if total == 0:
            print("Comanda este goala")
        else:
            print("1 student")
            print("2 happy")
            print("3 cupon")
            print("4 fara reducere")

            alegere = input("alege:")

            if alegere == "1":
                reducere_curenta = stabilire_reducere(total, "student", reduceri)
            elif alegere == "2":
                reducere_curenta = stabilire_reducere(total, "happy", reduceri)
            elif alegere == "3":
                reducere_curenta = stabilire_reducere(total, "cupon", reduceri)
            elif alegere == "4":
                reducere_curenta = 0

    elif optiune == "5":
        total = calcul_total(comanda, produse)

        if total == 0:
            print("nu exista produse in comanda")
        else:
            text_bon = afisare_bon(produse, comanda, reducere_curenta)

            scrie_bon_txt("bon.txt", text_bon)

            finalizare_comanda(produse, comanda)

            reducere_curenta = 0

    elif optiune == "6":
        anulare_comanda(comanda)
        reducere_curenta = 0
        print("comanda anulata")

    elif optiune == "0":
        print("program inchis")
        break

    else:
        print("optiune invalida")
