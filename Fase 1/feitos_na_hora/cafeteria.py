a = int(input())
b = int(input())
c = int(input())
d = int(input())
i=int(0)
cafe = int(0)
while (True):
    i += 1
    cafe = d*i
    leite = c - cafe
    if (leite>a and leite<b) or (leite==b and leite == a):
        if (cafe+leite)==c:
            print("S")
            break
    elif cafe>c:
        print("N")
        break

#finalizado