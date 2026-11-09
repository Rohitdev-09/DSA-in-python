num = [1,3,5,7,9,2,4,6,8,0]

# Increasing order
for i in range (len(num)) :
    min_index = i 
    for j in range (i+1,len(num)) :
        if num[j] < num[min_index] :
            min_index = j
    num[i], num[min_index] = num[min_index], num[i]
print(num)


# decreasing order
for i in range (len(num)) :
    max_index = i
    for j in range (i+1, len(num)) :
        if num[j] > num[max_index] :
            max_index = j
    num[i], num[max_index] = num[max_index], num[i]
print(num)