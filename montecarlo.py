import random
import matplotlib.pyplot as plt

# functie pentru o singura runda
def runda():

    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)

    suma = zar1 + zar2

    # verificam daca jucatorul castiga
    if suma == 7 or suma == 11:
        return 1
    else:
        return 0


# functie pentru simulare
def simulare(N):

    castiguri = 0

    for i in range(N):
        castiguri = castiguri + runda()

    probabilitate = castiguri / N

    return probabilitate


# valori pentru test
simulari = [100, 1000, 10000]

rezultate = []

for N in simulari:

    p = simulare(N)

    rezultate.append(p)

    print("N =", N)
    print("Probabilitate =", p)
    print()


# grafic
plt.plot(simulari, rezultate, marker="o")

plt.xlabel("Numar simulari")
plt.ylabel("Probabilitate")

plt.title("Monte Carlo - zaruri")

plt.grid(True)

plt.savefig("monte_carlo.png")

plt.show()