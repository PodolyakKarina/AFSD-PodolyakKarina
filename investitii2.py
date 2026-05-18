import json
import os

investitii_selectate = []


# 1. incarcare + validare date
def incarca_si_valideaza_date():

    if not os.path.exists("investitii.json"):
        print("Fisierul nu exista!")
        return []

    with open("investitii.json", "r") as f:
        date = json.load(f)

    if len(date) == 0: #câte investiții există
        print("Fisierul este gol!")
        return []

    investitii_valide = [] #aici punem doar investițiile bune

    for inv in date: #ia fiecare investiție pe rând
        if ("nume" in inv and "cost" in inv and "profit" in inv and
            "categorie" in inv and "risc" in inv):  #Verifică dacă are toate câmpurile
            investitii_valide.append(inv) #daca e corecta o pastram

    return investitii_valide


# 2. afisare investitii
def afisare_investitii(investitii):

    print("\nLISTA INVESTITIILOR\n")

    for investitie in investitii:
        print("Nume:", investitie["nume"])
        print("Cost:", investitie["cost"])
        print("Profit:", investitie["profit"])
        print("Categorie:", investitie["categorie"])
        print("Risc:", investitie["risc"])
        print("-------------------------")


# 3. analiza investitii
def analiza_investitii(investitii):

    print("\nANALIZA INVESTITIILOR\n")
    print("Numar investitii:", len(investitii))

    investitie_minima = investitii[0]
    investitie_maxima = investitii[0]
    profit_maxim = investitii[0]

    for investitie in investitii:

        if investitie["cost"] < investitie_minima["cost"]:
            investitie_minima = investitie

        if investitie["cost"] > investitie_maxima["cost"]:
            investitie_maxima = investitie

        if investitie["profit"] > profit_maxim["profit"]:
            profit_maxim = investitie

    print("Investitie cost minim:", investitie_minima["nume"])
    print("Investitie cost maxim:", investitie_maxima["nume"])
    print("Investitie profit maxim:", profit_maxim["nume"])

    categorii = {}
    riscuri = {}

    for investitie in investitii:

        categorie = investitie["categorie"]
        risc = investitie["risc"]   #extrage informațiile din fiecare investiție

        if categorie not in categorii:
            categorii[categorie] = 1
        else:
            categorii[categorie] += 1

        if risc not in riscuri:
            riscuri[risc] = 1
        else:
            riscuri[risc] += 1

    print("\nDistributie categorii:")
    print(categorii)

    print("\nDistributie riscuri:")
    print(riscuri)


# 4. eliminare risc ridicat
def eliminare_risc_ridicat(investitii):

    investitii_noi = []

    for investitie in investitii:
        if investitie["risc"] != "ridicat":
            investitii_noi.append(investitie)

    return investitii_noi


# 5. optimizare (rucsac) #Din mai multe investiții, alegem combinația care aduce profit maxim, dar nu depășește bugetul.
def optimizare_investitii(investitii, buget):

    n = len(investitii)

    dp = [[0 for j in range(buget + 1)] for i in range(n + 1)] #un tabel în care salvăm rezultate intermediare

    for i in range(1, n + 1):

        cost = investitii[i - 1]["cost"] #cât costă investiția
        profit = investitii[i - 1]["profit"] #cât profit aduce

        for b in range(buget + 1): #testăm toate bugetele posibile

            if cost <= b: #daca investitia incape in budet
                dp[i][b] = max(
                    dp[i - 1][b], #ori nu luam investitia
                    dp[i - 1][b - cost] + profit #ori o luam
                )
            else:
                dp[i][b] = dp[i - 1][b] #altfel pastram valoarea veche

    selectie = []  #pastram lista de investitii alese
    b = buget
# dp[i]i[b]-profitul maxim folosind primele i investiții și bugetul b
    for i in range(n, 0, -1):#mergem invers

        if dp[i][b] != dp[i - 1][b]: #dacă valoarea s-a schimbat:,investiția a fost folosită
            selectie.append(investitii[i - 1])  #o adaugam si scadem costul din buget
            b -= investitii[i - 1]["cost"]

    return dp[n][buget], selectie


# 6. PROGRAM PRINCIPAL 
if __name__ == "__main__":

    investitii = incarca_si_valideaza_date()

    afisare_investitii(investitii)
    analiza_investitii(investitii)

    investitii = eliminare_risc_ridicat(investitii)
    print("\nAm eliminat investitiile cu risc ridicat.")

    # 🔁 RELUARE ANALIZA PENTRU MAI MULTE BUGETE
    while True:

        buget = int(input("\nIntrodu bugetul: "))

        # validare buget
        while buget <= 0:
            buget = int(input("Introdu un buget valid ( > 0 ): "))

        profit_optim, investitii_selectate = optimizare_investitii(investitii, buget)

        print("\nREZULTAT FINAL")
        print("Buget:", buget)
        print("Profit optim:", profit_optim)

        cost_total = 0

        print("\nInvestitii selectate:")

        for inv in investitii_selectate:
            print("-", inv["nume"])
            cost_total += inv["cost"]

        print("\nCost total:", cost_total)
        print("Buget ramas:", buget - cost_total)

        alegere = input("\nVrei sa incerci alt buget? (da/nu): ")

        if alegere.lower() != "da":
            break