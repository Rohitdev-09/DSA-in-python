string = "nitin"
test1 = []
test2 = []
for i in range (len(string)) :
    asci = ord(string[i]) - 97
    test1.append(asci)
for i in range (len(string)-1, -1, -1) :
    ascii = ord(string[i]) - 97
    test2.append(ascii)
if test1 == test2 :
    print ("it is plaindrome")
else :
    print("it is not a plaindrome")



def fun(string, left, right) :
    if left >= right :
        return "it is plaindrome"
    asci1 = ord(string[left]) - 97
    asci2 = ord(string[right]) - 97
    if asci1 != asci2 :
        return "it is not a plaindrome"
    return fun(string, left+1, right-1)

print(fun(string, 0, len(string)-1))