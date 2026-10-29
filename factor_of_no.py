#factors of the number 
num = int(input("Enter no. "))
new = num

for i in range (1, new+1) :
    if new % i == 0 :
        print(i)


#factors of the number with less time and space complexity
num = int(input("Enter no. "))
result = []

for i in range (1, (num//2)+1) :
    if num % i == 0 :
        result.append(i)
result.append(num)
print(result)