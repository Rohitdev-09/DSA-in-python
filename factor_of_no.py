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


#factors of the number with less time and space complexity than second method
from math import sqrt
num = int(input("Enter no. "))
result = []

for i in range (1, int(sqrt(num))+1) :
    if num % i == 0 :
        result.append(i)
        if num//i != i :
            result.append(num//i)
result.sort()
print(result)