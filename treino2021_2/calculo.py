igual = int(0)

S = int(input())
A = int(input())
B = int(input())

for i in range (A,B+1):
    total = 0
    num = str(i)
    for n in num:
        total += int(n)
    if total == S:
        igual +=1
print(igual)






