lst = list("hello ")
for i in range(0,len(lst)):
    print(lst[i])

### reverse 
def descending_order(num):
    x=str(num)
    return int(x[::-1])
print(descending_order(09876543211234567890))
