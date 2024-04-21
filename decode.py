import heapq as h
import module as own

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
    
#lire l'arbre compressé
file = open("ArbreHuffman.txt", "r")
filestr = file.read()
file.close()

#reconstruire l'arbre
abr, strrestant =own.strtoabr(filestr)

#recréer un dict a partir de l'arbre
dict={}
own.abrtodict(abr,dictionnaire=dict)
#print(dict)

#reverse le dict pour chercher key en fonction de leur valeur
reversedict = own.reversedict(diction = dict)
#print(reversedict)

filebinaire = open('binaire.txt',"r")
fileoutput = open('textoutput',"w")
binaire = filebinaire.read()
txtdecode = own.dicttostr(binaire, dictionnaire = reversedict)#encoder le text
#print(txtdecode)
fileoutput.write(str(txtdecode))#storer le texte décomprèssé