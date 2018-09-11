def find_primes(how_much_primes):
    """Func returns array of primes which length is specified by argument.
    O(n2), checks all possible numbers in range and foreach it tries if (number % all numbers before it but not 1
    and the number) are not zero"""
    counter = 0
    to_check = 2
    primes = []
    while counter < how_much_primes:
        is_prime = True
        for d in range(2, to_check):
            if to_check % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(to_check)
            counter += 1
        to_check += 1
    return primes


print(find_primes(1000))
