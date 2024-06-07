number = 12345
n = str(number)
c = 0
for i in range(len(n)):
    c = c + int(int(n[i]))
print(c)