#Integer prime factorization
def prime_factorization(n):
    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1

        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

    

print( prime_factorization(10)  )
print( prime_factorization(12)  )
print( prime_factorization(81)  )
print( prime_factorization(25)  )
print( prime_factorization(356) )
