#http://en.wikipedia.org/wiki/Prime_number#Distribution
n_cons_non_primes = lambda n: [factorial(n+1)+m for m in range(2,n+2)]
