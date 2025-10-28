elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9, 7, 10, 4, 8]

elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]
absente = [1, 0, 2, 3, 0]
#partea 1
#1
print("1.Lista elevilor si notele lor:")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()

#2
nota_max = max(note)
nota_min = min(note)

print("2. Nota max si nota min:")
for i in range(len(elevi)):
    if note[i] == nota_max:
        print(f"Nota maximă {nota_max} - {elevi[i]}")
for i in range(len(elevi)):
    if note[i] == nota_min:
        print(f"Nota minimă {nota_min} - {elevi[i]}")
print()
print("3.Media:")
media = sum(note) / len(note)
print(f"Media clasei este: {media:.2f}\n")
print()
print("4.Promovati:")
for i in range(len(elevi)):
    if note[i] >=5:
        print(elevi[i])
        print()
        #partea 2
print("5. Un punct fiecărei note:")
for i in range(len(note)):
    if note[i] < 10:
        note[i] += 1

print(note)
print()
print("6.Adaugarea elevului predefinit:")
elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)
print()
print("7.Stergerea elevului predefinit:")

poz=elevi.index(elev_de_sters)
elevi.pop(poz)
note.pop(poz)
print(elevi)
print(note)
print()
print("7.Afisarea listei din nou:")

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print()

#partea 3
print("8.Cautari de nume:")
i = 0
while interogari_nume[i]!="stop":
    if interogari_nume[i]==elevi[i]:
        print(note[i])
    else: print("Nu exista")
    i=i+1
print()
print("8.Numar promovati si respinsi:")
promovati=0
respinsi=0
for i in range(len(note)):
    if note[i]>=5:
        promovati+=1
    else:
        respinsi+=1
print(f"Promovati si respinsi: {promovati} si respinsi: {respinsi}")
print()
print("9.Media promovatilor")
promovati=[]
for i in range(len(note)):
    if note[i]>=5:
        promovati.append(note[i])
if len(promovati)>0:
    media = sum(promovati)/len(promovati)
print(f"Media promovatilor: {media:.2f}")
print()











