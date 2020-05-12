import unicodedata

def getUnicodeName(char):
    """Provide a character and I will return a description
    if available in the Unicode database"""
    try:
        return unicodedata.name(char)
    except ValueError:
        return ''


if __name__ == '__main__':
    name = getUnicodeName('ü')
    # LATIN SMALL LETTER U WITH DIAERESIS
