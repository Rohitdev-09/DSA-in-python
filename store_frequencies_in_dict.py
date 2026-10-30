num = [1,1,1,4,4,3,6,8,6,7,5,9]
dict = {}

for i in range (len(num)):
    if num[i] not in dict :
        dict[num[i]] = 1
    else :
        dict[num[i]] += 1

print(dict)
