X,Y,Z = input().split()
X = int(X)
Y = int(Y)
Z = int(Z)
S = (X + Y + abs(X - Y))/2
S = (S + Z + abs(S - Z))/2
S = int(S)
print(str(S) + " eh o maior")