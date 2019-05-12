import random

range_a = 1
range_b = 1*10**10


# es ist egal ob g größer ist als p oder ob p eine primzahl ist --> es kommt immernoch die selbe zahl heraus
print(range_b)

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True

#primes = [i for i in range(range_a,range_b) if isPrime(i)] test

#p = random.choice(primes)
p = random.randint(range_a,range_b)

while isPrime(p)== False:
    p = random.randint(range_a,range_b)

g = random.randint(range_a,range_b)

while g>p:
    g = random.randint(range_a,range_b)

print("g:",g)
print("p:",p)


#secrets
a = random.randint(range_a,range_b -1)
b = random.randint(range_a,range_b -1)


print("a: ",a," b:",b)

#A = g**a%p
#B = g**b%p

A = pow(g,a,p)
B = pow(g,b,p)


#print("K1: ",A**b%p)
#print("K2: ",B**a%p)

print("K1: ", pow(A,b,p))
print("K2: ",pow(B,a,p))
