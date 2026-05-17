import json

investitii_selectate = []


# functie pentru citirea fisierului json
def salvare_fisier_json_ca_lista():

    f = open("investitii.json", 'r')

    continut = json.load(f)

    f.close()

    return continut


# afisare investitii
def afisare_investitii(investitii):

    print("\nLISTA INVESTITIILOR\n")

    for investitie in investitii:

        print("Nume:", investitie["nume"])
        print("Cost:", investitie["cost"])
        print("Profit:", investitie["profit"])
        print("Categorie:", investitie["categorie"])
        print("Risc:", investitie["risc"])

        print("-------------------------")


# analiza descriptiva
def analiza_investitii(investitii):

    print("\nANALIZA INVESTITIILOR\n")

    print("Numar investitii:", len(investitii))

    investitie_minima = min(investitii, key=lambda x: x["cost"])
    investitie_maxima = max(investitii, key=lambda x: x["cost"])
    profit_maxim = max(investitii, key=lambda x: x["profit"])

    print("Investitie cost minim:", investitie_minima["nume"])
    print("Investitie cost maxim:", investitie_maxima["nume"])
    print("Investitie profit maxim:", profit_maxim["nume"])

    categorii = {}
    riscuri = {}

    for investitie in investitii:

        categorie = investitie["categorie"]
        risc = investitie["risc"]

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


# eliminare investitii cu risc ridicat
# restrictia suplimentara
def eliminare_risc_ridicat(investitii):

    investitii_noi = []

    for investitie in investitii:

        if investitie["risc"] != "ridicat":
            investitii_noi.append(investitie)

    return investitii_noi


# programare dinamica
def optimizare_investitii(investitii, buget):

    n = len(investitii)

    # construire tabel dp
    dp = [[0 for j in range(buget + 1)] for i in range(n + 1)]

    # completare tabel
    for i in range(1, n + 1):

        cost = investitii[i - 1]["cost"]
        profit = investitii[i - 1]["profit"]

        for b in range(buget + 1):

            if cost <= b:

                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - cost] + profit
                )

            else:
                dp[i][b] = dp[i - 1][b]

    # reconstruire solutie
    b = buget

    for i in range(n, 0, -1):

        if dp[i][b] != dp[i - 1][b]:

            investitii_selectate.append(investitii[i - 1])

            b = b - investitii[i - 1]["cost"]

    return dp[n][buget]


# program principal
if __name__ == '__main__':

    investitii = salvare_fisier_json_ca_lista()

    afisare_investitii(investitii)

    analiza_investitii(investitii)

    # aplicam restrictia suplimentara
    investitii = eliminare_risc_ridicat(investitii)

    print("\nInvestitiile cu risc ridicat au fost eliminate.")

    buget = int(input("\nIntrodu bugetul: "))

    while buget <= 0:
        buget = int(input("Introdu un buget valid: "))

    profit_optim = optimizare_investitii(investitii, buget)

    cost_total = 0

    print("\nREZULTAT FINAL\n")

    print("Buget disponibil:", buget)

    print("Profit optim:", profit_optim)

    print("\nInvestitii selectate:")

    for investitie in investitii_selectate:

        print("-", investitie["nume"])

        cost_total += investitie["cost"]

    print("\nCost total utilizat:", cost_total)

    print("Buget ramas:", buget - cost_total)