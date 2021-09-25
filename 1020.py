A = int( input() )
P = ["ano(s)","mes(es)","dia(s)"]
for I,X in enumerate([365,30,1]):
    B = int(A/X)
    A = A-B*X
    print("{:0}".format(B),P[I])