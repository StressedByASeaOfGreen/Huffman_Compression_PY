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
file_str = file.read()
file.close()

#reconstruire l'arbre
abr, str_restant =own.str_to_abr(file_str)

#recréer un dict a partir de l'arbre
dict={}
own.abr_to_dict(abr,dictionnaire=dict)
#print(dict)

#reverse le dict pour chercher key en fonction de leur valeur
reverse_dict = own.reverse_dict(diction = dict)
#print(reversedict)

file_binaire = open('binaire.txt',"r")
file_output = open('textoutput',"w")
binaire = file_binaire.read()
txt_decode = own.dict_to_str(binaire, dictionnaire = reverse_dict)#encoder le text
#print(txtdecode)
file_output.write(str(txt_decode))#storer le texte décomprèssé