


import heapq as h

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

def abr_to_dict(abr, val="", dictionnaire=None): 
    #creer un dictionnaire vide lors de la première loop de la fonction
    if dictionnaire is None:
        dictionnaire = {}

    # creer un str additionnant tous les valeurs composant un charactère
    Nou_Val = val + str(abr.dir)
  
    #voir si l'arbre continu
    #si oui, on encode l'intérieur
    if abr.gauche: 
        abr_to_dict(abr.gauche, Nou_Val, dictionnaire) 
    if abr.droite: 
        abr_to_dict(abr.droite, Nou_Val, dictionnaire) 
  
        #si l'arbre arrête alors sauver la charactère correspondant dans le dictionnaire
    if not abr.gauche and not abr.droite : 
        #print(f"{abr.char}:{NouVal}")
        dictionnaire[abr.char] = Nou_Val
    
    return dictionnaire


def combine(abr): #pour combiner les arbres de huffman
    while len(abr)>1: #loop jusqua ce qu'il rest un arbre
        g = h.heappop(abr)
        g.dir = 1
        d = h.heappop(abr)
        d.dir = 0
        #créer un nouvel arbre
        nouv_abr = arbre(None, g.freq + d.freq)
        nouv_abr.gauche = g
        nouv_abr.droite = d
        h.heappush(abr,nouv_abr)# remettre l'arbre dans la liste abr
        h.heapify(abr)
        """for i in abr:
            print (i.freq)
        print("......")"""


def abr_to_str(abr):#format l'arbre huffman dans un string     https://stackoverflow.com/a/15083564
    data =''
    if (abr.droite or abr.gauche) or (abr.droite and abr.gauche):
        data += '0'
        data += abr_to_str(abr.gauche)
        data += abr_to_str(abr.droite)
    else:
        data += '1'
        data += abr.char
    return data


def str_to_abr(file_str):
   
    if not file_str:
        return None, ''

    #   Creer la racine de l'arbre
    racine = arbre(None, None)

    if file_str[0] == '0':  #monceau parent
        file_str = file_str[1:]

        #décoder les 2 branches de l'arbre
        racine.gauche, file_str = str_to_abr(file_str)
        racine.gauche.dir = 1
        racine.droite, file_str = str_to_abr(file_str)
        racine.droite.dir = 0
    else:  # Monceau feuille(fin)
        racine.char = file_str[1]
        file_str = file_str[2:]

    return racine, file_str

def reverse_dict(diction={}):
    dictionnaire = dict((value, key) for key, value in diction.items())
    return dictionnaire

def dict_to_str(txt_encode,dictionnaire={},txt_decode = ""): #pour décompresser le txt à partir d'un dictionnaire inversé comme { 10001:t ,  ...}

    while len(txt_encode)>0 :
        for bin in dictionnaire:
            if txt_encode.startswith(bin):
                txt_decode += dictionnaire[bin]
                txt_encode = txt_encode[len(bin):]
    return txt_decode
                
