######################################################
def szyfr(klucz,txt):
    txts=""
    for i in range(len(txt)):
        j = i%len(klucz)
        kodt = ord(txt[i])
        kodk = ord(klucz[j])
        kod = kodt ^ kodk
        #print(kod)
        txts += chr(kod)
    return txts

######################################################
klucz="Czterej pancerni i pies"
txt1="To jest tekst do zakodowania, żółw, 18.07.2019"
txt2=szyfr(klucz,txt1)
txt3=szyfr(klucz,txt2)

print(txt1, end='\n\n')

print(txt2, end="\n\n")
print(txt2.encode(), end="\n\n")
print(txt3, end="\n\n")
