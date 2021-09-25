A = int( input() )

print(A)

if A >= 100:
    B = int(A/100)
    A = A-B*100
    print(B,"nota(s) de R$ 100,00")
else:
    print(0,"nota(s) de R$ 100,00")
    
if A >= 50:
    B = int(A/50)
    A = A-B*50
    print(B,"nota(s) de R$ 50,00")
else:
    print(0,"nota(s) de R$ 50,00")

if A >= 20:
    B = int(A/20)
    A = A-B*20
    print(B,"nota(s) de R$ 20,00")
else:
    print(0,"nota(s) de R$ 20,00")

if A >= 10:
    B = int(A/10)
    A = A-B*10
    print(B,"nota(s) de R$ 10,00")
else:
    print(0,"nota(s) de R$ 10,00")

if A >= 5:
    B = int(A/5)
    A = A-B*5
    print(B,"nota(s) de R$ 5,00")
else:
    print(0,"nota(s) de R$ 5,00")
    
if A >= 2:
    B = int(A/2)
    A = A-B*2
    print(B,"nota(s) de R$ 2,00")
else:
    print(0,"nota(s) de R$ 2,00")
    
if A >= 1:
    B = int(A/1)
    A = A-B*1
    print(B,"nota(s) de R$ 1,00")
else:
    print(0,"nota(s) de R$ 1,00")