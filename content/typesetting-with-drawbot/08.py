someText = """Considerare l’esistenza di un insieme di strumenti convenzionali di organizzazione e interpretazione dello spazio concatenati, il quale in qualche modo interagisca con la lingua parlata, è utile perché conviene dal punto di vista progettuale"""

size(200, 200)
myBox = (20, 30, 150, 150)

fill(.8)
rect(*myBox)

fill(0)
textBox(someText, myBox, align='left') 