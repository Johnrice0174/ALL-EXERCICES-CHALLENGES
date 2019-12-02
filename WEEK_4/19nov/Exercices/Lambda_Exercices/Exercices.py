#EXERCICE 1
# a = input("Please enter a number: ")
# b = input("Please enter a number: ")

# while a > b:
# 	print("Hello World")
# 	break

# input()

#EXERCIE 2
# num1 = int(input("Input the 1st number: "))
# num2 = int(input("Input the 2nd number: "))
# num3 = int(input("Input the 3rd number: "))

# print(num1)
# print(num2)
# print(num3)
# if num1 > num2 and num1 > num3:
# 	print("The greatest number is {}: ".format(num1))

# elif num2 > num1 and num2 > num3:
# 	print("The greatest number is {}: ".format(num2))

# elif num3 > num1 and num3 > num2:
# 	print("The greatest number is {}: ".format(num3))

# else:
# 	print("srdrgrsdgrrdg")

#EXERCICE 3
# month = int(input("Please choose a month between 1 and 12: "))

# if month < 1 or month > 12:
# 	month = int(input("Be serious and choose a month between 1 and 12: "))

# elif month >= 3 and month <=5:
# 	print("Your month's season is SPRING!")

# elif month >= 6 and month <=8:
# 	print("Your month's season is SUMMER!")

# elif month >= 9 and month <=11:
# 	print("Your month's season is AUTUMN!")

# elif month == 12 or month == 1 or month == 2:
# 	print("Your month's season is WINTER!")

# else:
# 	print("bouffon(e) -_-' ")

#EXERCICE 4
# alphabet = input("Input a letter of the alphabet: ")
 
# if alphabet in ('a', 'e', 'i', 'o', 'u','y', 'A', 'E', 'I', 'O', 'U', 'Y'):
# 	print("%s is a vowel." % alphabet)
# else:
# 	print("%s is a consonant." % alphabet) 

#EXERCICE 5
import random #import keywoard to use classes like random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')