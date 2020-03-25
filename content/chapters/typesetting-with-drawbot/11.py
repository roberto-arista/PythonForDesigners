someText = """Considerare l’esistenza di un insieme di strumenti convenzionali di organizzazione e interpretazione dello spazio concatenati, il quale in qualche modo interagisca con la lingua parlata, è utile perché conviene dal punto di vista progettuale"""

newPage(200, 200)
hyphenation(True)
language('English')
textBox(someText, (20, 30, 150, 150), align='left')

newPage(200, 200)
hyphenation(True)
language('Italian')
textBox(someText, (20, 30, 150, 150), align='left')