A = int( input() )
print(A)
for X in [100,50,20,10,5,2,1]:
    B = int(A/X)
    A = A-B*X
    print("{:0} nota(s) de R$ {:0},00".format(B,X))