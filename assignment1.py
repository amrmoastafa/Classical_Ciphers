from support_functions import *
import sys

print(sys.argv[1])
selected_algorithm = sys.argv[1]
if selected_algorithm == 'caesar':        
    plains = readfile("input/caesar_plain.txt") # Caeser
    keys = [3,6,12]
    ciphers = []
    for k in keys:
        ciphers.append("key: " + str(k))
        for p in plains:
            ciphers.append(caeser_cypher(p,k))
        ciphers.append("\n")
    writefile("output/caesar_cipher.txt", ciphers)
elif selected_algorithm == 'vigenere':
    plains = readfile("input/vigenere_plain.txt") # Vigenere
    keys = [("PIE",False), ("AETHER", True)]
    ciphers = []
    for k in keys:
        ciphers.append("key: " + str(k[0]) + ", mode: " + ("auto mode" if k[1] else "repeating mode"))
        for p in plains:
            ciphers.append(viegenere_cypher(p,k[0],k[1]))
        ciphers.append("\n")
    writefile("output/vigenere_cipher.txt", ciphers)
elif selected_algorithm == 'playfair':    
    plains = readfile("input/playfair_plain.txt") # playfair
    keys = [ "RATS", "ARCHANGEL"]
    ciphers = []
    for k in keys:
        ciphers.append("key: " + str(k))
        for p in plains:
            ciphers.append(playfair_cypher(p,k))
        ciphers.append("\n")
    writefile("output/playfair_cipher.txt", ciphers)
elif selected_algorithm =='vernam':
    plains = readfile("input/vernam_plain.txt") # vernam
    keys = ["SPARTANS"]
    ciphers = []
    for k in keys:
        ciphers.append("key: " + str(k))
        for p in plains:
            ciphers.append(vernam_cypher(p,k))
        ciphers.append("\n")
    writefile("output/vernam_cipher.txt", ciphers)
elif selected_algorithm == 'hill':    
    plains = readfile("input/hill_plain_2x2.txt") # hill_2x2
    key = np.array([[5,17],[8,3]])
    ciphers = []
    for p in plains:
        ciphers.append(hill_cypher(p,key,2))
    writefile("output/hill_cipher_2x2.txt", ciphers)

    plains = readfile("input/hill_plain_3x3.txt") # hill_3x3
    key = np.array([[2,4,12],[9,1,6],[7,5,3]])
    ciphers = []
    for p in plains:
        ciphers.append(hill_cypher(p,key,3))
    writefile("output/hill_cipher_3x3.txt", ciphers)