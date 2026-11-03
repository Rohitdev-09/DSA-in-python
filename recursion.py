# 1-n head recursion
def fun1(x,n) :
    if n==0:
        return
    print(x)
    fun1(x+1,n-1)
fun1(1, 10)

def fun2(x,n) :
    if x>n :
        return
    print(x)
    fun2(x+1,n)
fun2(1, 10)

# n-1 head recursion
def fun3(n) :
    if n==0 :
        return
    print(n)
    fun3(n-1)
fun3(10)

# n-1 tail recursion
def fun4(x,n) :
    if x>n :
        return
    fun4(x+1,n)
    print(x)
fun4(1,10)

