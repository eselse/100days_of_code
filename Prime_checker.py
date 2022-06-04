import time

# Write your code below this line 👇
def prime_checker(number):
    if number in [0, 1]:
        return False

    for num in range(2, number, 2):
        if number in [2, 3]:
            return True
        if number % 2 == 0:
            return False
        elif number % num == 0:
            return False
    else:
        return True




# def miller_rabin(n, k):
#
#     # Implementation uses the Miller-Rabin Primality Test
#     # The optimal number of rounds for this test is 40
#     # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
#     # for justification
#
#     # If number is even, it's a composite number
#
#     if n == 2:
#         return True
#
#     if n % 2 == 0:
#         return False
#
#     r, s = 0, n - 1
#     while s % 2 == 0:
#         r += 1
#         s //= 2
#     for _ in xrange(k):
#         a = random.randrange(2, n - 1)
#         x = pow(a, s, n)
#         if x == 1 or x == n - 1:
#             continue
#         for _ in xrange(r - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
#     return True
# @halbGefressen

start = time.time()
result = []
for i in range(15000):
    if prime_checker(i):
        result.append(i)
end = time.time()
print(f'Total time {round(end - start)} seconds')