N = int(input())
N2 = input().split()
x = []
for i in N2:
    x.append(int(i))

for j in range (N):
    linha=[]
    for num in x:
        if num==j:
            linha.append(1)
        else:
            linha.append(0)
    print(linha)
            

