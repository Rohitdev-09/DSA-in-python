# paramaterised recursion
def sum(i,n,total = 0) :
    if i>n :
        print(total)
        return 
    total = total + i
    sum(i+1,n,total)

sum(1,10)

#functional recursion
def fun(n) :
    if n == 1 :
        return 1
    return n + fun(n-1)
print(fun(10))

#functional recursion
def fun2(n) :
    if n == 1 :
        return 1
    return n * fun2(n-1)
print(fun2(10))