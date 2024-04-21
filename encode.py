


import heapq as h
import module as own
#read txt file
read = open("textinput.txt" , "r")
txt = read.read()
read.close()
print(f'la longeur du texte original en binaire est de {len(txt)*8} bits')
#on crée une nouvelle class représentant un arbre à 2 branche
class arbre:
    def __init__(self,char, freq):
        self.char = char
        self.freq = freq
        self.droite = None
        self.gauche = None
        self.dir = "" #valeur directionnel de cet arbre
    def __lt__(self,other):
        return self.freq < other.freq

#on crée un dictionnaire(freq) contenant touts les charactères du texte(txt) et leur frequance
freq = {}
for char in txt:
    if char in freq.keys():
        freq[char] += 1
    else:
        freq[char] = 1
##freq[' '] = txt.count(' ')
#print(freq)
#réorganiser le dictionnaire en ordre décroissant et le mettre dans une list Lfreq

Lfreq = sorted(freq, key=freq.get, reverse=True)
#print (Lfreq)
#creer un liste d'arbre à une valeur
abr = []
for i in range(len(Lfreq)):
    abr.append(arbre(Lfreq[i],freq[Lfreq[i]]))

#combinons les arbre
own.combine(abr)


#creer un dictionnaire avec les valeurs binaire de tous les charactères
dictbinaire = {}
own.abrtodict(abr[0],dictionnaire= dictbinaire) #abr[0] car il y a juste 1 arbre dans abr
#print(dictbinaire)

#encode txt
txtencode = ''
for char in txt:
    txtencode += dictbinaire[char]


#print(f"texte encodé:{txtencode}")
#sauver le binaire dans un doc txt
bin = open('binaire.txt' , 'wt')
bin.write(txtencode)
bin.close()
open('ArbreHuffman.txt', 'w').close()# clear doc
abrh = open('ArbreHuffman.txt' , 'wt')

txttree = own.abrtostr(abr[0])
#print(txttree)
abrh.write(txttree)
abrh.close()
#le compte final compréssé
#
print(f'la longeur du texte compressé en binaire est de {(len(txtencode)+len(txttree)+ (sum(1 for char in txttree if char not in ("0", "1"))*7))} bits')
#print(f"une longueur de {len(txtencode)} charactères")
#print('done')
