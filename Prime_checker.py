# Write your code below this line 👇
def prime_checker(number):
    if number in [0, 1]:
        print("It's a prime number")
        return False

    for i in range(2, number):
        if number in [2, 3]:
            print("It's a prime number")
            return True
        elif number > 3 and number % i == 0:
            print("It's not a prime number.")
            return False
    else:
        print("It's a prime number.")
        return True


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
