info = input().split()
n=int(info[0])
m=int(info[1])
total = 0
for _ in range(n):
    info_food=input().split()
    p=int(info_food[0])*4
    g=int(info_food[1])*9
    c=int(info_food[2])*4
    total += p+g+c
print(m-total)

#funcionando