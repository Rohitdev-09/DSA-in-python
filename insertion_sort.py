num = [1,3,5,7,9,2,4,6,8,0]

# Increasing order
for i in range (1, len(num)) :
    key = num[i]
    j = i-1
    while j >= 0 and num[j] > key :
        num[j+1] = num[j]
        j -= 1
    num[j+1] = key
print(num)


# Decreasing order
for i in range (1, len(num)) :
    key = num[i]
    j = i-1
    while j>=0 and num[j]<key :
        num[j+1] = num[j]
        j -= 1
    num[j+1] = key
print(num)