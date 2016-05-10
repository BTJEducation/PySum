print("Input a number to work out the sum of all numbers below it :")
x = int(input("Number : "))
y = 0
while x != 0 :
    y = y + x
    x = x - 1
    print(y)

print(y)
