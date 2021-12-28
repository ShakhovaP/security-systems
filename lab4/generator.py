# import random

# def sieve_eratosthenes(n):
#     """
#     Решето Эратосфена
#     """
#     a = range(n + 1)
#     a = list(a)
#     a[1] = 0
#     result_list = []
#     i = 2
#     while i <= n:
#         if a[i] != 0:
#             result_list.append(a[i])
#             for j in range(i, n + 1, i):
#                 a[j] = 0
#         i += 1
#     return random.choice(result_list)

# print(sieve_eratosthenes(100000))
########################################################################
# from random import randint

# def isPrime(n, k=5): # miller-rabin
    
#     if n < 2: return False
#     for p in [2,3,5,7,11,13,17,19,23,29]:
#         if n % p == 0: return n == p
#     s, d = 0, n-1
#     while d % 2 == 0:
#         s, d = s+1, d/2
#     for i in range(k):
#         x = pow(randint(2, n-1), d, n)
#         if x == 1 or x == n-1: continue
#         for r in range(1, s):
#             x = (x * x) % n
#             if x == 1: return False
#             if x == n-1: break
#         else: return False
#     return True

# print(isPrime(103))
# print(isPrime(99))


#######################################################33
import math
from random import randint

def is_prime(num):
    if num < 2:         return False
    elif num < 4:       return True
    elif not num % 2:   return False
    elif num < 9:       return True
    elif not num % 3:   return False
    else:
        for n in range(5, int(math.sqrt(num) + 1), 6):
            if not num % n:
                return False
            elif not num % (n + 2):
                return False

    return True

# print(is_prime(103))    
# print(is_prime(99))    


if __name__ == '__main__':
    number = randint(math.pow(10, 10), math.pow(10, 15))
    res = is_prime(number)
    while not res:
        number += 1
        res = is_prime(number)
    print(number, is_prime(number))


