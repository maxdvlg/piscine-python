#exercice15
liste = [17, 38, 10, 25, 72]
print("notre liste est :", liste)
liste.sort()
print("liste triée : ", liste)
liste.append(12)
print("on ajoute 12 a la liste", liste)
liste.reverse()
print("On retourne la liste", liste)
print("index de 17", liste.index(17))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[2:])
print(set(liste))

#exercice 16
s = "inversez moi"
print(s)
print(s[::-1])

#exercice 17
a = "sonos"
b = a [:: -1]
if a==b:
    print("ceci est un palindrome")
else:
    print("ce n'est pas un palindrome")

#exerice 19
truc = []
print(truc)
machin = ["0.0", "0.0", "0.0", "0.0", "0.0",]
print(machin)

#exercice 20

print(" ------ ")
for x in range(0,4) :
    print(x)
print(" ------ ")
for x in range(4,8) :
    print(x)
print(" ------ ")
for x in range(2,9) :

    print(x)
print(" ------ ")

chose = [0, 1, 2, 3, 4, 5]

if 3 in chose :
    print("3 is ok")
else : 
    print("3 is not ok")
if 6 in chose : 
    print("6 is ok")
else : 
    print("6 is not ok")