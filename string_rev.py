x = list(str(230840676775955))
print(x)
y = list(map(int, x))
print(y.sort(reverse=True))
for i in range(0, len(y)-1):
    if i < (len(y)):
        if y[i] > y[i+1]:
            temp = y[i]
            y[i] = y[i+1]
            y[i+1] = temp

print(y)
y = str(y)
strr=""