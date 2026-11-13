num = [1,3,5,7,9,2,4,6,8,0]

# Merging technique


num1 = [1,3,5,7,9]
num2 = [2,4,6,8,0]
result = []
def fun(i) :
    for i in range (len(num1)) :
        r1 = num1[i]
    for i in range (len(num2)) :
        r2 = num2[i]
    if r1 < r2 :
        result.append(r1)
    elif r2 < r1 :
        result.append(r2)
    else :
        result.append(r1)
    fun(i+1)




fun(0)
print(result)