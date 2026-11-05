arr = [9,1,8,2,7,3,6,4,5,0]
rev = []

# reverse of an array from index 0-n
for i in range (len(arr)-1, -1, -1) :
    rev.append(arr[i])
print(rev)


# reverse of an array from index 2-5
for i in range (0, 2) :
    rev.append(arr[i])
for i in range (4, 1, -1) :
    rev.append(arr[i])
for i in range (5,len(arr)) :
    rev.append(arr[i])
print(rev)

# reverse of an array from index 0-n by recursion
num = [9,1,8,2,7,3,6,4,5,0]
def reverse(num, left, right) :
    if left >= right :
        return
    num[left], num[right] = num[right], num[left]
    reverse(num, left+1, right-1)

reverse(num, 0, len(num)-1)
print(num)
