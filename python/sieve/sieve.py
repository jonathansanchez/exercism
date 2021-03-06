def sieve(limit):
    primes = []
    unmarked = list(range(2, limit + 1))
    while len(unmarked) > 0:
        prime = unmarked.pop(0)
        for mult in range(2, limit / prime + 1):
            if mult * prime in unmarked:
                unmarked.remove(mult * prime)
        primes.append(prime)
    return primes
