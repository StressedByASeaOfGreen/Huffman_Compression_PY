


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
for item in Lfreq:
    abr.append(arbre(item,freq[item]))

#combinons les arbre
own.combine(abr)
abr = abr[0]

#creer un dictionnaire avec les valeurs binaire de tous les charactères

dict_binaire = own.abr_to_dict(abr)
#print(dict_binaire)

#encode txt
txt_encode = ''
for char in txt:
    txt_encode += dict_binaire[char]


#print(f"texte encodé:{txtencode}")
#sauver le binaire dans un doc txt
bin = open('binaire.txt' , 'wt')
bin.write(txt_encode)
bin.close()
open('ArbreHuffman.txt', 'w').close()# clear doc
abr_h = open('ArbreHuffman.txt' , 'wt')

txt_tree = own.abr_to_str(abr)
#print(txttree)
abr_h.write(txt_tree)
abr_h.close()
#le compte final compréssé
#
print(f'la longeur du texte compressé en binaire est de {(len(txt_encode)+len(txt_tree)+ (sum(1 for char in txt_tree if char not in ("0", "1"))*7))} bits')
#print(f"une longueur de {len(txtencode)} charactères")
#print('done')
