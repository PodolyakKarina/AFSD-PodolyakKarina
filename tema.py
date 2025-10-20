import string

articol="Săptămânalul „Unirea“ din Blaj a apărut în 3 ianuarie 1891. Fiecare ediţie avea un subtitlu: „foaie bisericească-politică”, iar pe ultima pagină o rubrică, similară cu ceea ce apare în ziarele de astăzi la Sfaturi utile, or Ştiaţi că?"
jumatate = len(articol)//2
parte1=articol[:jumatate]
parte2=articol[jumatate:]
parte1 = parte1.upper()
parte1=parte1.strip()
partge2=parte2[::-1]
parte2=parte2.capitalize()
parte2 = parte2.translate(str.maketrans('', '', string.punctuation))
rezultate=parte1+parte2
print(rezultate)