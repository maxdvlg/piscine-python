##exercice 21
myfile = open("mytext.txt", mode="w")
mynumber = int(input("give me a number"))
i = 0

while i < mynumber :
    newelement = str(input("votre element ;"))
    myfile.write(newelement + "\n")
    i += 1

myfile.close()

#exercice 22
fh = open('data.txt')
for line in fh:
  if(re.search(r"^[^@]+@[^@]+\.[^@]+$", str(line))):
    print(line)
fh.close()

#exercice 23
def countWords(str):
  count = dict()
  words = str.split()
  for word in words:
      if word in count:
          count[word] += 1
      else:
          count[word] = 1
  return count
print(countWords("non rien de rien , je ne regrette rien"))

#exercice 24 outside this file

#exercice 25
def somme(a, b, c) :
    return print("la somme est de :",(a+b+c))

montuple = (1, 2, 1)
somme(montuple[0], montuple[1], montuple[2])