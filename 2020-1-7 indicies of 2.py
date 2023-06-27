n = int(input())
i = 1

while pow(2,i) <= n:
    i += 1

i -= 1
print(i, pow(2,i))
