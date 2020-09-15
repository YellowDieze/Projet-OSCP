#Olivier Czuper

import string

#On entre le texte chiffré dans une variable
cipher_text = """444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!"""

#on crée le dictionnaire qui contiendra les valeurs des lettres à décrypter
mon_dictionnaire = dict()
mon_dictionnaire ={'2':'A','22':'B','222':'C','3':'D','33':'E','333':'F','4':'G','44':'H','444':'I','5':'J','55':'K','555':'L','6':'M','66':'N','666':'O','7':'P','77':'Q','777':'R','7777':'S','8':'T','88':'U','888':'V','9':'W','99':'X','999':'Y','9999':'Z','.':'.', ' ':' ',',':',', '!!':'!!','\n\n':'\n\n',':':':'}

#on crée deux copie du texte crypté pour les comparer
n = d = cipher_text[0]
plain_text = ""

#On compare chaque élément du du texte et on vérifie si la lettre suivante est la même que la lettre actuelle sur laquelle on pointe
for i in range(1,len(cipher_text)):
    #si oui on vérifie la suivante
    if n==cipher_text[i]:
        d += cipher_text[i]
    #sinon on entre la valeur correspondant à la clé d du dictionnaire et on passe au caractère suivant
    else:
        plain_text += mon_dictionnaire[d]
        n = d = cipher_text[i]
        i = i+1
plain_text += mon_dictionnaire[d]

print("Le texte converti est : \n '{}'".format(plain_text))

#Nous avons toujours quelque chose de crypté qui ressemble a un chiffrement de César
#brute force

message="GSV XLWV GL GSV HZU OLXP : TLIVGRIVNVMGUFMW!!"

#On vérifie pour chaque lettre de l'alfabet
for i in range(26):
    code =""
    #On se déplace dans le message
    for y in message:
        #Si ce n'est pas une lettre on passe au caractère suivant
        if y.isalpha() == False:
            code += y
        #On décale les lettres et on les ajoute au code
        else:
            n=i - string.ascii_letters.index(y)
            code += string.ascii_letters[n]

    print("Pour la clé : {0} le contenu est : {1} \n ".format(i, code))
