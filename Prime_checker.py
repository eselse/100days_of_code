def prime_checker(number):
    if number < 0 or number in [0, 1]:
        return False
    elif number in [2, 3]:
        return True
    else:
        for num in range(3, number, 2):
            if number > 3 and number % 3 == 0:
                return False
            elif number > 5 and number % 5 == 0:
                return False
            elif number > 7 and number % 7 == 0:
                return False
            elif number > 9 and number % 9 == 0:
                return False
            elif number % num == 0:
                return False
        else:
            return True

for i in range(-10, 150):
    if prime_checker(i):
        print(i)
