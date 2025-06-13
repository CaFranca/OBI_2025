N = int(input())
entrada= input().split()
x = []
for i in entrada:
    x.append(int(i))
H = max(x)  # altura máxima do gráfico
for linha in range(H):
    atual = []
    for valor in x:
        if valor >= H - linha:
            atual.append('1')
        else:
            atual.append('0')
    print(' '.join(atual))
