def eratosthenes_array(n):
    """Returns array of n prime numbers. Primes are generated using Sieve of Eratosthenes"""
    array = []

    for i in range(n + 1):
        array.append(True)

    i = 2
    while i ** 2 <= n:
        if array[i] is True:
            j = i ** 2
            while j <= n:
                array[j] = False
                j += i
        i += 1
    print("ARRAY IS READY")
    # TODO: Check how long it takes to find primes and how much memory it consumes
    return array


def show_primes_between(start, stop, array):
    """Displays prime numbers from array in given range.
    Prime numbers are indexes of array fields which value is set to True"""
    if start < 2:
        start = 2
    if stop > len(array):
        stop = len(array)
    for p in range(start, stop):
        if array[p] is True:
            print(p, end=", ")


x = eratosthenes_array(10000000)

show_primes_between(9990000, 10000000, x)