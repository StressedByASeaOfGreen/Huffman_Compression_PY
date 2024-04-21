


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

def abrtodict(abr, val="", dictionnaire=None): 
  
    # creer un str additionnant tous les valeurs composant un charactère
    NouVal = val + str(abr.dir)
  
    #voir si l'arbre continu
    #si oui, on encode l'intérieur
    if abr.gauche: 
        abrtodict(abr.gauche, NouVal, dictionnaire) 
    if abr.droite: 
        abrtodict(abr.droite, NouVal, dictionnaire) 
  
        #si l'arbre arrête alors sauver la charactère correspondant dans le dictionnaire
    if not abr.gauche and not abr.droite : 
        #print(f"{abr.char}:{NouVal}")
        dictionnaire[abr.char] = NouVal


def combine(abr): #pour combiner les arbres de huffman
    while len(abr)>1: #loop jusqua ce qu'il rest un arbre
        g = h.heappop(abr)
        g.dir = 1
        d = h.heappop(abr)
        d.dir = 0
        #créer un nouvel arbre
        nouvabr = arbre(None, g.freq + d.freq)
        nouvabr.gauche = g
        nouvabr.droite = d
        h.heappush(abr,nouvabr)# remettre l'arbre dans la liste abr
        h.heapify(abr)
        """for i in abr:
            print (i.freq)
        print("......")"""


def abrtostr(abr):#format l'arbre huffman dans un string     https://stackoverflow.com/a/15083564
    data =''
    if (abr.droite or abr.gauche) or (abr.droite and abr.gauche):
        data += '0'
        data += abrtostr(abr.gauche)
        data += abrtostr(abr.droite)
    else:
        data += '1'
        data += abr.char
    return data


def strtoabr(filestr):
   
    if not filestr:
        return None, ''

    #   Creer la racine de l'arbre
    racine = arbre(None, None)

    if filestr[0] == '0':  #monceau parent
        filestr = filestr[1:]

        #décoder les 2 branches de l'arbre
        racine.gauche, filestr = strtoabr(filestr)
        racine.gauche.dir = 1
        racine.droite, filestr = strtoabr(filestr)
        racine.droite.dir = 0
    else:  # Monceau feuille(fin)
        racine.char = filestr[1]
        filestr = filestr[2:]

    return racine, filestr

def reversedict(diction={}):
    dictionnaire = dict((value, key) for key, value in diction.items())
    return dictionnaire

def dicttostr(txtencode,dictionnaire={},txtdecode = ""): #pour décompresser le txt à partir d'un dictionnaire inversé comme { 10001:t ,  ...}

    while len(txtencode)>0 :
        for bin in dictionnaire:
            if txtencode.startswith(bin):
                txtdecode += dictionnaire[bin]
                txtencode = txtencode[len(bin):]
    return txtdecode
                
