# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name_1 = name1.lower()
lower_name_2 = name2.lower()
score = 0

score += lower_name_1.count("t")
score += lower_name_1.count("r")
score += lower_name_1.count("u")
score += lower_name_1.count("e")

score += lower_name_2.count("t")
score += lower_name_2.count("r")
score += lower_name_2.count("u")
score += lower_name_2.count("e")

score *= 10

score += lower_name_1.count("l")
score += lower_name_1.count("o")
score += lower_name_1.count("v")
score += lower_name_1.count("e")

score += lower_name_2.count("l")
score += lower_name_2.count("o")
score += lower_name_2.count("v")
score += lower_name_2.count("e")

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
