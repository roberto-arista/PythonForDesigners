someText = """Considerare l’esistenza di un insieme di strumenti convenzionali di organizzazione e interpretazione dello spazio concatenati, il quale in qualche modo interagisca con la lingua parlata, è utile perché conviene dal punto di vista progettuale: porre il testo in contrapposizione all’immagine è utile solamente a replicare un modello di editoria libraria affermatosi alla fine del XV secolo, vincolato dalle tecniche produttive esistenti all’epoca (stampa a caratteri mobili e xilografia) e applicabile in buona sostanza principalmente all’editoria libraria legata alla narrativa, che è solo una piccola parte della produzione scritta."""

myBox = (20, 30, 150, 150)
while someText:
    newPage(200, 200)

    fill(.9)
    rect(*myBox)

    fill(0)
    someText = textBox(someText, myBox, align='left')