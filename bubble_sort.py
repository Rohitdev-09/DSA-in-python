num = [1,3,5,7,9,2,4,6,8,0]

# Increasing order
for j in range (1, len(num)) :
    for i in range (len(num)-1) :
        if num[i] > num[i+1] :
            num[i], num[i+1] = num[i+1], num[i]
print(num)
