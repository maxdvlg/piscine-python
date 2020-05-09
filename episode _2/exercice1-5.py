from math import * 

## exercie 1 :
temps = 6.892
distance = 19.7
vitesse_f = float("%0.1f" % (distance / temps))
print(vitesse_f)


## exercice 2 :
Nom = str(input("Quel est ton nom ?"))
Age = int(input("Quel age as tu ?"))
print("Bonjour", Nom, "tu as", Age)


##exercice 3 :
new_float = float(input("Give me a float : "))
if new_float >= 0 :
    print(sqrt(new_float))
else :
    print("tu sais pas ecrire fwer")


##exercice 4 :
Mot1 = str(input("donne moi un premier mot :"))
Mot2 = str(input("donne moi un deuxieme mot :"))
print(min(Mot1, Mot2))


##exercice 5 : 
max_pSeuil = 2.3
max_vSeuil = 7.41

pressure = float(input("Quel est la pression ?"))
volume = float(input("Quel est le volume ?"))

if pressure > max_pSeuil and volume > max_vSeuil : 
    print("arrêt immediat")
elif pressure > max_pSeuil and volume < max_vSeuil :
    print("augmente le volume")
elif pressure < max_pSeuil and volume > max_vSeuil :
    print("baisser le volume")
else :
    print("ok")
