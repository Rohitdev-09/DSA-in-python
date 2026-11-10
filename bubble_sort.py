num = [1,3,5,7,9,2,4,6,8,0]

# Increasing order
for j in range (1, len(num)) :
    for i in range (len(num)-1) :
        if num[i] > num[i+1] :
            num[i], num[i+1] = num[i+1], num[i]
print(num)


# Increasing order
for i in range (len(num)-2, -1,-1) :
    is_swap = False
    for j in range (0, i+1):
        if num[j] > num[j+1] :
            num[j], num[j+1] = num[j+1], num[j]
            is_swap = True
    if is_swap == False :
        break
print(num)