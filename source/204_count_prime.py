#!/usr/bin/python
def count_prime(n):
    if n < 2:
        return 0

    prime_bit = [True]*n
    num = 0
    for i in range(2,n):
        if prime_bit[i]:
            num += 1
            for j in range(2,n):
                if i*j >= n:
                    break

                prime_bit[i*j] = False

    return num,[i for i,v in enumerate(prime_bit) if v]



case = (1,2,10,100)
for i in case:
    print i,count_prime(i)
