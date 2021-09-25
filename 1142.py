N = int(input())
L = 0
U = 1
while L < N:
    P = ""
    for V in range(3):
        P = P+str(U) +" "
        U = U+1
    P = P+"PUM"
    U = U+1
    L = L+1
    print(P)