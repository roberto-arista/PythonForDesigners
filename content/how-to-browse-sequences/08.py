from string import ascii_lowercase, ascii_uppercase
# convert from strings to lists using the list() constructor
latinLowercase = list(ascii_lowercase)
latinUppercase = list(ascii_uppercase)
# create an empty list for the complete alphabet
latinAlphabet = []
# extend the empty list with uppercase and lowercase
latinAlphabet.extend(latinUppercase)
latinAlphabet.extend(latinLowercase)
# result: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']