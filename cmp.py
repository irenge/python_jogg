x = "reset"
y = "rest"
def near(x,y):
    count = 0
    if ((len(y) + 1) == len(x)):
        for i in range(len(y)):
            for j in range(len(x)):
                if count == len(x):
                    return False
                elif y[i] == x[j]:
                    count = 0
                    continue
                else:
                    count += 1           
        return True
    else:
        return False
print(near(x,y))