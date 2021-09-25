A = int( input() )
S = ""
for I,X in enumerate([3600,60,1]):
    B = int(A/X)
    A = A-B*X
    S = S+str(B)
    if X > 1:
        S = S+":"
print(S)