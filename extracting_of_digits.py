# extracting digits from the number
def extract() :
    num = int(input("Enter no. "))
    new = num
    while new > 0 :
        last_digit = new%10
        print(last_digit)
        new = new//10


# counting digits of the number
def count() :
    num = int(input("Enter no. "))
    new = num
    digit = 0
    while new > 0 :
        digit = digit + 1 
        new = new//10
    print(digit)


#reverse of digits of the numbers
def reverse() :
    num = int(input("Enter no. "))
    new = num
    reverse = 0
    while new > 0 :
        last_digit = new%10
        reverse = (reverse*10) + last_digit
        new = new//10
    print(reverse)


#palindrome of numbers
def palindrome() :
    num = int(input("Enter no. "))
    new = num
    reverse = 0
    while new > 0:
        last_digit = new%10
        reverse = (reverse*10) + last_digit
        new = new//10
    if num == reverse :
        print(f"{num} is a palindrome no. ")
    else :
        print(f"{num} is not a palindrome no. ")


#armstrong no.
def armstrong() :
    num = int(input("Enter no. "))
    new = num 
    digit = 0
    while new > 0 :
        digit = digit + 1
        new = new//10
    print(digit)

    arm = num
    sum = 0
    while arm > 0:
        last_digit = arm % 10
        sum += last_digit ** digit
        arm = arm//10
    print(sum)

    if num == sum :
        print(f"{num} is an Armstrong no. ")
    else :
        print(f"{num} is not an Armstrong no. ")


