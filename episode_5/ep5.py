myList = ["\b\t80cm\t60cm\n" , "\b\t81cm\t51cm\n" , "\b\t105cm\t145cm\n" ]
print(myList)

for x in range(len(myList)) :
 temp = re.findall(r'\d+', myList[x])
 res = list(map(int, temp))
 if res[0] < res[1] :
   print(res[0])