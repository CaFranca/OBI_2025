E =int(input())
S =int(input())
L =int(input())
total = int(0)
if (E<S):
    total += S-E
    if S<L:
        total += L-S
    else:
        total += S-L
else:
    total += E-S
    if S<L:
        total += L-S
    else:
        total += S-L
if (E<L):
    total += L-E
else:
    total += E-L
print(total)
