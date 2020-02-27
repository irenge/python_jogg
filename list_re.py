num =345762374627462742674
x = list(str(num))
xy = list(map(int, x))
xy.sort(reverse=True)
xy = list(map(str, xy))
print(xy)
strr =""
for i in range(0,len(xy)):
    strr += xy[i]
print(strr)

print(int("".join(sorted(str(num), reverse=True))))