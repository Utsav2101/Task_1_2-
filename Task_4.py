num = int(input("Enter the limit to find the fibonacci series : "))
num1 = 0
num2 = 1
i = 0
while (i < num):
    if(i <= 1):
        next = i
    else:
        next = num1 + num2
        num1 = num2
        num2 = next
    print(next)
    i = i+1

