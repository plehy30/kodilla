######################################################
def cezar(txt):
    klucz = 3
    txts = ""
    for i in range(len(txt)):
        kod=ord(txt[i])
        if kod!=ord(" "):
            kod+=klucz
            if kod>ord('Z'):
                kod -= 26
        txts += chr(kod)
    return txts
######################################################
def dcezar(txt):
    klucz = 3
    txts = ""
    for i in range(len(txt)):
        kod=ord(txt[i])
        if kod!=ord(" "):
            kod-=klucz
            if kod<ord('A'):
                kod += 26
        txts += chr(kod)
    return txts
######################################################
txt1="TO JEST TEKST DO ZAKODOWANIA"
txt2=cezar(txt1)
txt3=dcezar(txt2)

print(txt1)
print(txt2)
print(txt3)
