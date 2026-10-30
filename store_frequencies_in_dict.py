# store_frequencies_in_dict
num = [1,1,1,4,4,3,6,8,6,7,5,9]
dict = {}
for i in range (len(num)):
    if num[i] not in dict :
        dict[num[i]] = 1
    else :
        dict[num[i]] += 1
print(dict)



# store_frequencies_in_dict
num = [1,1,1,4,4,3,6,8,6,7,5,9]
hashmamp = {}
for i in range (len(num)) :
    hashmamp[num[i]] = hashmamp.get(num[i],0) +1
print(hashmamp)
