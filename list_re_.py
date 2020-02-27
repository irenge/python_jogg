num = input("Enter ISBN number: ")
total = 0
for i in range(0,len(num)):
    if i <= 12:
        if(i % 2 != 0):
           total = total +3*int(num[i])
        else:
           total = total + int(num[i])
            
final = 10 - (total % 10)
print(final)
