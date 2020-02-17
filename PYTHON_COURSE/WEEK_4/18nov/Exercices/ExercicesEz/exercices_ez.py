#EXERCICE_EZ 1.1
False
True
False
Error
False

#EXERCICE_EZ 1.2
my_fav_numbers = set()
my_fav_numbers.add(4)
my_fav_numbers.add(14)
my_fav_numbers.add(74)
my_fav_numbers.add(18)

my_fav_numbers.remove(18)

print(my_fav_numbers)

friend_fav_numbers = set()
friend_fav_numbers.add(73)
friend_fav_numbers.add(90)

print(friend_fav_numbers)

our_fav_numbers = set(my_fav_numbers).union(set(friend_fav_numbers))
print(our_fav_numbers)

#EXERCICE_EZ 2.1
my_fav_numbers = (4,14)
my_fav_numbers +=(18,20)
print(my_fav_numbers)

friend_fav_numbers = (73,90)

our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

#EXERCICE_EZ 1.3
#1.1)
a = list(range(0, 10))
b = list(range(1, 11))
c = list(range(-9, 5))
d = list(reversed((range(5, 11)))) #voir intro.py
e = list(range(1,14,2))
f = [2**i for i in range(1,8)]
g = [0.5*i for i in range(3,10)]

#1.2)
motiv = "You can do it"
count = 0
while count < 3:
  print(motiv)
  count += 1
#2)
for i in range(1,4):print(str(i)+"."+motiv)

#EXERCICE 2.2
#1)
integer = 1
float_number = 1.0
print(float(integer))
print(int(float_number))

#2)
yes

#3)
i have found some on internet but it didnt work :(

#4)
list = [0.5*i for i in range(3,10)]

#EXERCICE 1.4
user_height = input("What is your height (in inches)? ")
height_min = 35
if int(user_height) < int(height_min):
  print("Sorry, You aren't tall enough to ride a roller coaster")
else:
  print("Nice! You are tall enough to ride a roller coaster")

#EXERCICE 2.3
num = int(input("Enter an integer: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))