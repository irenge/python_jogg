def fact(num):
    count = 1
    factorial = 1
    while count <= num:
        factorial = factorial * count 
        count += 1
    return factorial


number = int(input("Enter a number:"))
print(fact(number))