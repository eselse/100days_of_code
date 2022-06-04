# Write your code below this line 👇
def prime_checker(number):
    if number in [0, 1]:
        return False

    for num in range(2, number):
        if number in [2, 3]:
            return True
        elif number % num == 0:
            return False
    else:
        return True


for i in range(150):
    if prime_checker(i):
        print(i)
