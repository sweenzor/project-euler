def euler_sieve(num):
    candidates = range(num+1)
    finish = int(num**0.5)

    for i in range(2, finish+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (num/i - 1)

    return [i for i in candidates[2:] if i]



primes =  euler_sieve(2000000)
print sum(primes)
