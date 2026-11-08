# checking a plaindrome no.   -> Brute method
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


# checking a plaindrome no.   -> Recursion method
def fun(string, left, right) :
    if left >= right :
        return "it is plaindrome"
    if string[left] != string[right] :
        return "it is not a plaindrome"
    return fun(string, left+1, right-1)

print(fun(string, 0, len(string)-1))


# checking a plaindrome no.   -> while loop method
def fun1(string) :
    left = 0
    right = len(string)-1
    while left<right :
        if string[left] != string[right] :
            return "it is not a plaindrome"
        left += 1
        right -= 1 
    return "it is plaindrome"  

print(fun1(string))