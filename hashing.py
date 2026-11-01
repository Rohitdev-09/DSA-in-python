n1 = [10,1,0,5,9,7,8,6,9,8,7,6,5,4,3,2,1,4,2,1,8,6,4,7,5,1,7,2,4,5,4,8,5,2,1,5,2,0,5,1,5,5,2]      # 0<n1<11
n2 = [1,2,3,4,5,6,7,8,9,10,78,111]

# Brute Force  (t.c = O(n × m))
dict = {}
for i in range (len(n2)) :
    count = 0
    for j in range (len(n1)) :
        if n2[i] == n1[j] :
            count += 1
    dict[n2[i]] = count
print(dict)


# Hashing using Frequency Array    (t.c = O(n + m))
hash_list = [0]*11
for num in n1 :
    hash_list[num] += 1
for num in n2 :
    if num<0 or num>10 :
        print (0)
    else :
        print(hash_list[num])


# Hashing using Dictionary    (t.c = O(n + m)) 
dict = {}
for num in n1 :
    if num in dict:
        dict[num] += 1
    else :
        dict[num] = 1
 
for num in n2 :
    print(dict.get(num,0))