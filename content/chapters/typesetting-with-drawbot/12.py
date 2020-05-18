someText = """Considerare l’esistenza di un insieme di strumenti convenzionali di organizzazione e interpretazione dello spazio concatenati, il quale in qualche modo interagisca con la lingua parlata, è utile perché conviene dal punto di vista progettuale: porre il testo in contrapposizione all’immagine è utile solamente a replicare un modello di editoria libraria affermatosi alla fine del XV secolo, vincolato dalle tecniche produttive esistenti all’epoca (stampa a caratteri mobili e xilografia) e applicabile in buona sostanza principalmente all’editoria libraria legata alla narrativa, che è solo una piccola parte della produzione scritta."""

myBox = (10, 30, 180, 150)

# justified alignment with no hyphenation makes no sense
newPage(200, 200)
hyphenation(False)
textBox(someText, myBox, align='justified')

# hyphenation helps, but it’s still far from optimal
newPage(200, 200)
hyphenation(True)
textBox(someText, myBox, align='justified')

# choosing the right language improves the composition
newPage(200, 200)
hyphenation(True)
language('Italian')
textBox(someText, myBox, align='justified')

# in this case I would just align to the left
# I see no problems in a slightly uneven right edge
# designers complaining about it only consider
# the frame and not the content
newPage(200, 200)
hyphenation(True)
textBox(someText, myBox, align='left')