string = "qwertyuiopasdfghjklzxcvbnmlkjhgfdsazserfvghujnjk"
value = ["r", "o", "h", "i", "t"]

# Brute Force  (t.c = O(n × m)) 
dict = {}
for ch in value :
    count = 0
    for char in string :
        if char == ch :
            count += 1
    dict[ch] = count
print(dict)

# Hashing using Frequency Array    (t.c = O(n + m)) 
dict = [0]*26
for ch in string :
    ascii = ord(ch) 
    index = ascii-97
    dict[index] += 1
for ch in value :
    ascii = ord(ch)
    index = ascii-97
    print(dict[index])

# Hashing using Dictionary    (t.c = O(n + m)) 
dict = {}
for ch in string :
    if ch in dict :
        dict[ch] += 1
    else :
        dict[ch] = 1
for ch in value :
    print(dict.get(ch,0))
