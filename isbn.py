num = input("Enter ISBN number: ")
num = list(map(int, num))
total = 0
for i in range(0,len(num)):
    if i <= 12:
        if(i % 2 != 0):
            num[i] = num[i] * 3
        total = total + num[i]
final = 10 - (total % 10)
print(final)
