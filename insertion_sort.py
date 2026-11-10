num = [1,3,5,7,9,2,4,6,8,0]

for i in range (len(num)) :
    if num[i+1] > num[i] :
        key = num[i+1]
    for j in range (i-1, -1, -1) :
        if num[j] > key :
