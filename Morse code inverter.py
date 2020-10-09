###################################
#                                 #
#       Morse Code Converter      #
# Date: 09/10/2020 14:15          #
# Author: CryptoLover705          #
#      This code removes all      #
#        the  whitespaces;        #
#       special characters.       #
#    I hope that it is useful.    #
#                                 #
###################################

# The Morse Table.
morse_table = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',}

# The input to be encrypted.
plain_text = input() or "Sololearn"

# Removing whitespaces.
plain_text = plain_text.replace(" ","")

# Removing special characters.
special_characters = [i for i in plain_text if not i.isalnum()]

for i in special_characters:
    if i in plain_text:
        plain_text = plain_text.replace(i,"")

# Encrypting.
encrypted_text = [morse_table[i] for i in plain_text.upper()]

# Visualition.
print("The plain text:\n"+"".join(plain_text))
print("\nThe Morse equivalent:\n"+" ".join(encrypted_text))
 
