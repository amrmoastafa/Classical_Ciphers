import numpy as np

def caeser_cypher(plain_text ,encryption_key):

    """Implementation for caeser encryption algorithm

    Args:
        plain_text (string): The message that is required to be encrypted.
        encryption_key (string): The encryption key used to encrypt the message.
    """
    plain_text = plain_text.upper()
    cipher_text = str()
    for character in plain_text:
        cipher_text += chr(((ord(character) - ord('A') + encryption_key) % 26) + ord('A'))
    return cipher_text


def playfair_cypher(plain_text ,encryption_key):

    """Implementation for playfair encryption algorithm

    Args:
        plain_text (string): The message that is required to be encrypted.
        encryption_key (string): The encryption key used to encrypt the message.
    """
    encryption_key = encryption_key.upper()
    plain_text = str(plain_text).upper().replace("J","I")
    position_dictionary = dict() # represent the order of each letter in the encryption_key matrix if it was 1D
    current_LetterPosition = 0 # the current Letter Position in the position_dictionary
    letters = ""

    for key in encryption_key:
        if(key not in position_dictionary):
            letters+=key
            position_dictionary[key] = current_LetterPosition
            current_LetterPosition += 1

    for i in range(ord("A"),ord("Z") + 1):
        if(i == ord("J")):
            continue
        if(chr(i) not in position_dictionary):
            position_dictionary[chr(i)] = current_LetterPosition
            letters+=chr(i)
            current_LetterPosition += 1

    ListOfPairs = list()
    i = 0
    while i < len(plain_text):
        if i == len(plain_text) - 1: # only last letter left
            if(plain_text[i] == "X"): # if the single letter is x append z
                ListOfPairs.append(("X","z"))
            else: # if last letter not x append x
                ListOfPairs.append((plain_text[i],"X")) 
        elif plain_text[i] == plain_text[i+1]: # letter is same as next one
            ListOfPairs.append((plain_text[i],"X")) 
        else:
            ListOfPairs.append((plain_text[i],plain_text[i+1])) 
            i+=1
        i += 1

    def getitem(row,col):
        i = row * 5 + col
        return letters[i]
    def shiftright(row,col):
        return getitem(row,(col+1) % 5)
    def shiftdown(row,col):
        return getitem((row + 1) % 5,col)
    def encrypt(pair:tuple):
        row1 = position_dictionary[pair[0]] // 5 # 0,1,2,3,4 will ll return 0 which is required
        col1 = position_dictionary[pair[0]] % 5 # 0,5,10 all return 0 which is required
        row2 = position_dictionary[pair[1]] // 5 # 0,1,2,3,4 will ll return 0 which is required
        col2 = position_dictionary[pair[1]] % 5 # 0,5,10 all return 0 which is required
        ans = str()
        if row1 == row2:
            ans += shiftright(row1,col1)
            ans += shiftright(row2,col2)
        elif col1 == col2:
            ans += shiftdown(row1,col1)
            ans += shiftdown(row2,col2)
            pass
        else:
            ans += getitem(row1,col2)
            ans += getitem(row2,col1)
        return ans
    res = ""
    for i in ListOfPairs:
        res += encrypt(i)
    return res


def hill_cypher(plain_text ,encryption_key ,size):
    plain_text = plain_text.upper()
    plain_text = plain_text + "X" * ((size-len(plain_text) % size) % size)
    ListOfPairs = list()
    
    for j in range(0,len(plain_text),size):
        temp = list()
        for h in range(0,size):
            temp.append(ord(plain_text[j + h]) - ord("A"))
        ListOfPairs.append(np.array(temp))
    result = ""
    for l in range(0, ListOfPairs.__len__()):
        ListOfPairs[l] = np.dot(ListOfPairs[l],encryption_key)
        for i in ListOfPairs[l]:
            result = result + chr((((i%26) + 26) % 26) + ord("A"))
    return result


def viegenere_cypher(plain_text ,encryption_key ,mode):

    """viegenere_cypher implementiation

    Args:
        plain_text (string): The message that is required to be encrypted.
        encryption_key (string): The encryption key used to encrypt the message.
        mode (string) : select auto or repeat mode

    """
    plain_text = plain_text.upper()
    encryption_key = encryption_key.upper()
    if(mode):
        encryption_key = encryption_key + plain_text
    else:
        encryption_key = encryption_key * ( len(plain_text) // len(encryption_key) + 1)
    result = ""
    n = len(plain_text)
    for i in range(n):
        result = result + caeser_cypher(plain_text[i] ,ord(encryption_key[i]) - ord('A'))
    
    return result


def vernam_cypher(plain_text,encryption_key="spartans"):
    xkey = list()
    for i in encryption_key:
        xkey.append(ord(i) - ord('A'))
    l = len(xkey)
    ans = ""
    for i in range(0,len(plain_text)):
        p = (ord(plain_text[i]) - ord('A')) ^ xkey[i % l]
        ans += chr(p + ord('A'))
    return ans


def readfile(filename):
    file = open(filename, "r")
    ans = []
    for p in file.readlines():
        ans.append(p.replace("\n",""))
    return ans
    

def writefile(filename, strlist):
    file = open(filename, "w")
    for st in strlist:
        file.write(st + "\n")

