num = 10
# 0, nth fibonacci no.
fib = []
for i in range (num) :
    if i == 0 :
        fib.append(0)
    elif i == 1 :
        fib.append(1)
    else :
        fib.append(fib[i-1]+fib[i-2])
print(fib)

# nth fibonacci no.
def fib(num) :
    if num == 0 or num == 1 :
        return num
    return fib(num-1) + fib(num-2)
print(fib(num))