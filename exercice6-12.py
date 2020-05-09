#exercice 6
adressemail = str(input("Saisisser votre adresse mail :"))

arobase_status = False
for i in range(len(adressemail)) :
    print(adressemail[i])
    if adressemail[i] == "@" :
        print("arrobase existe")
        arobase_status = True

lenght = len(adressemail) - 1     
if adressemail[lenght] == "m" and adressemail[(lenght-1)] == "o" and adressemail[(lenght-2)] == "c" and adressemail[(lenght-3)] == "." and arobase_status == True: 
    print("adresse email .com found") 
elif adressemail[lenght] == "r" and adressemail[(lenght-1)] == "f" and adressemail[(lenght-2)] == "." and arobase_status == True :
    print("adresse email .fr found") 


#exercice 7
i = 0
while i < 10:
  print("message", i)
  i += 1


#exercice 8 & 12
phrase = "bonjour à vous"
for e in phrase : 
    print(e)

#exercice 9
val1 = 0
val2 = 10
while val1 < val2 :
    print(val1)
    val1 += 1


#exercice 10
val1 = 0
val2 = 10
while val2 > val1 :
    val2 += -1 
    if val2 % 2 != 0 : 
        print(val2)


# exercice 11
while True:
    try:
        n = int(input("Entrez un nombre:"))
        if 1 < n < 10:
            print(n)
            break
    except ValueError:
        continue

#exercice 13
for i in range(0, 15):
    if i % 3 == 0:
        print(i)

##exercice 14 
n = 20
i = 0
while i <= n :
    if i % 2 == 0 : 
        print("while : ", i)
    i += 1


for e in range(0, 21) : 
    if e % 2 == 0 :
        print("for :", e) 