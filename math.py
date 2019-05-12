from math import factorial

def nCr(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def g(x,y,n):
    return (x+y)**n

def f(n,k):
    return nCr(n,k)*5**(n-k)*2**k

def j():
    return 1

def sigma(Endwert,Funktion,startWert=0):
    sum = 0
    for k in range(startWert,Endwert+1):
        sum += Funktion(Endwert,k)
    return sum

print(sigma(3,f))
print(g(5,2,7))
print(7**7)
print(factorial(0))
