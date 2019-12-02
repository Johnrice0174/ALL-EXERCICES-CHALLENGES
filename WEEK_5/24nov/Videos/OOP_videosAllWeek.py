# coding=utf-8
#OOP

class PlayerCharacter:
	def __init__(self, name):
		self.name = name

	def run(self):
		print('run')

player1 = PlayerCharacter()

print(player1) #line9, TypeError __init__() missing required 
                                 #postional argument: 'name'

#__init__ > init = special method / __ = magic method
#we have to simply give a name to our new player !!
player1 = PlayerCharacter('Ashe')

print(player1) 
#<__main__.PlayerCharacter object at 0x7fc55028eeb8>

#self is a way to define...
#self refers to PlayerCharacter that we going to create Player1
#and says that we want self.name to define what is the name of Player1

print(player1.name) #Ashe

#self is like APPEND in lists...
#[].append(new_object) = self.name = name
#name is an Attribute
player1 = PlayerCharacter('Ashe')
player2 = PlayerCharacter('Braum')

print(player1.name) #Ashe
print(player2.name) #Braum

#We can add attributes (name, age...):
class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)

print(player1.age) #25
print(player2.run) 
#<bound method PlayerCharacter.run of <__main__.PlayerCharacter object at 0x7fc55028eeb8>
#RUN is a METHOD (not an attribute Be Careful)

print(player1.age)
print(player2.run())
#results:
#25
#run
#None

#WHY NONE ? cause our run function doesnt return anything
class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')
		return 'is running'

print(player1.age)
print(player2.run())
#results:
#25
#run
#is running

print(player1)#<...PlayerCharacter object at 0x7fc55028eeb8>
print(player2)#<...PlayerCharacter object at 0x7f2d4cc71048>

#Each Player is Stored in DIFFERENT Memory Location!

player1.attack = 50

print(player1.attack) #50
print(player2.attack) #ERROR 
#this object has no attribute 'attack'

help() #get all info on a method

---------------
class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')
		return 'is running'

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1) #<.... object at ...>
print(player1.membership) #True
print(player2.membership) #True

#this membership = True is NOT dynamic...
#it will be AUTOMATICALLY TRUE FOR ALL OBJECTS Created
#by the PlayerCharacter Class.... so :
#let's add Condition:
class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		if (self.membership): #dont forget self.
			self.name = name
		    self.age = age

	def run(self):
		print('run')
		return 'is running'

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.membership) #True
print(player2.membership) #True
print(player1.name) #Ashe
print(player2.membership) #True
#We Can Also write refer by PlayerCharacter:
#if (PlayerCharacter.membership):

print(player1.name) #Ashe
print(player2.membership) #True
----------
class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self):
		print(f'For Frejlord, {name} is here')    
	# def run(self):
	# 	print('run')
	# 	return 'is running'

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.shout())
print(player2.shout()) 
#ERROR name is not defined... WHY ? Just add SELF :

class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self):
		print(f'For Frejlord, {self.name} is here!') #SELF 
	# def run(self):
	# 	print('run')
	# 	return 'is running'

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.shout()) #For Frejlord, Ashe is here!
					   #None
print(player2.shout()) #For Frejlord, Braum is here!
					   #None

#in this line : print(f'For Frejlord, {self.name} is here!')
#if we write PlayerCharacter.name (au lieu de self)
#it will fail : ERROR 'PlayerCharacter has no attribute name'

#Cause Name is not a CLASS OBJECT ATTRIBUTE,
#It is not actually a property/attribute of PlayerCharacter
#it is defined in our structure/Init Function.

# A CLASS OBJECT ATTRIBUTE is something that does NOT 
#change accross different instances.
#Versus in ATTRIBUTE/Class-Attribute ARE DYNAMICS and SPECIFIC 
#to each class object

#ALL TIME WE USE/CALL A METHOD WE USE SELF !!

class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self, hello):
		print(f'For Frejlord, {self.name} is here!') #SELF 
	
	def run(self):
		print('run')
		return 'is running'

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.shout('hello')) #For Frejlord, Ashe is here!
					   #hello
print(player2.shout()) #For Frejlord, Braum is here!
					   #None

-------------------------------
# @CLASSMETHOD & @STATICMETHOD

class PlayerCharacter:
	#Class Object Attribute
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self, hello):
		print(f'For Frejlord, {self.name} is here!') #SELF 
	
	def run(self):
		print('run')
		return 'is running'

	@classmethod
	def adding_things(num1, num2):
		return num1 + num2

player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.adding_things(2,3))
#ERROR adding_things() takes 3 positionals arguments
#but 3 were given!

#WE HAVE TO USE CLS:
class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self, hello):
		print(f'For Frejlord, {self.name} is here!') #SELF 
	
	def run(self):
		print('run')
		return 'is running'

	@classmethod
	def adding_things(cls, num1, num2):
		return num1 + num2
#cls = class. here it is PlayerCharacter
player1 = PlayerCharacter('Ashe', 25)
player2 = PlayerCharacter('Braum', 60)
player1.attack = 50

print(player1.adding_things(2,3)) #5

---
#if i make:
class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
		    self.age = age

	def shout(self, hello):
		print(f'For Frejlord, {self.name} is here!') #SELF 
	
	def run(self):
		print('run')
		return 'is running'

	@classmethod
	def adding_things(cls, num1, num2):
		return num1 + num2


print(PlayerCharacter.adding_things(2,3))
#5 (IT WORKS!!)
#adding_things is a METHOD of 
#the actual class (PlayerCharacter) 
# so a @classmethod
---
#if i change 
	@classmethod
	def adding_things(cls, num1, num2):
		return cls('Zoe', num1 + num2)

player3 = PlayerCharacter.adding_things(4,6)
print(player3.age) #10 !!

----------
@staticmethod
def adding_things2(num1, num2):
	return num1 + num2

----------------------------------
# __init__

class PlayerCharacter:
	membership = True
	def __init__(self, name='anonymous', age=0):
		if (age > 18):
			self.name = name
		    self.age = age

	def shout(self, hello):
		print(f'Name: {self.name} , Age: {self:age}')

player1 = PlayerCharacter()
player2 = PlayerCharacter()
player1.attack = 50

print(player1.shout())
#ERROR 'PlayerCharacher' object has no attribute 'name'
#we verify, all is well, we have put self, and 
#anonymous is only default values so it is ok...
#BUT the default age is 0... so if we dont add a value
#to our player so it is automaticaly 0 so less than 18
#so the player is NOT Created... so we get an error.

player1 = PlayerCharacter('Tom', 10)
print(player1.shout())
#SAME ERROR cause 10 is less than 18.

#the instantiation of an object where we’re able 
#to add these different controls and
#safeguards to perhaps make sure that we receive 
#their right data type in order to create the object
#or maybe the age is over 18 in order to make sure
#that when we actually instantiate this player one
#object we’re doing it the right way.
So __init__ gives you a lot of control.

--------------------------------
class NameOfClass():
	class_attribute = 'value'
	def __init__(self, arg): #arg= param1, param2...
			self.arg = arg #self.param1 = param1

def method(self)
	#code

@classmethod
def cls_method(cls, arg)
	#code

@staticmethod
def stc_method(arg)
	#code

-------------------------------
#EXERCICE CAT 

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Felix', 4)
cat2 = Cat('Croquette', 2)
cat3 = Cat('Goldy', 8)

# 2 Create a function that finds the oldest cat

def oldest():
	if cat1.age > cat2.age and cat1.age > cat3.age:
		print(f'{cat1.name} is {cat1.age} and he is the oldest cat here')
	elif cat2.age > cat1.age and cat2.age > cat3.age:
		print(f'{cat2.name} is {cat2.age} and he is the oldest cat here')
	elif cat3.age > cat1.age and cat3.age > cat2.age:
		print(f'{cat3.name} is {cat3.age} and he is the oldest cat here')
	else:
		print('error')

	return()
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest()

# ------------ 4 PILLARS OF OOP ------------
# 1) ENCAPSULATION
class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')

	def speak(self):
		print(f'my name is {self.name}, and I am {self.age} years old')

player1 = PlayerCharacter('Bard', 50)
print(player1.name) #Bard
print(player1.age) #100

player2 = {'name': 'Bard', 'age': 100}
print(player2['name']) #Bard
print(player2['age']) #100

# 2) ABSTRACTION

class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')

	def speak(self):
		print(f'my name is {self.name}, and I am {self.age} years old')

player1 = playerCharacter('Bard', 100)
print((1,2,3,1)).count(1) #We have to make Abstaction of few things
#we dont have to know how they were implemented in pyhon
player1.name = '!!!!'
player1.speak = 'BOOOO'
print(player1.speak()) #ERROR
print(player1.speak) #BOOO (it works)
# ------
# Private and Public Variables
# private?
class PlayerCharacter:
	def __init__(self, name, age):
		# private self.name = name #Only in Java (but in Python there is not TRUE
		# private variables
		self._name = name
		self._age = age
# TO MAKE A VARIABLE PRIVATE JUST PUT AN UNDERSCORE BEFORE
# The Underscore doesnt change ANYTHING but it is only a CONVENTION with Developers
# That when we see Underscore before a var it is a Private variable
	def run(self):
		print('run')

	def speak(self):
		print(f'my name is {self._name}, and I am {self._age} years old')
#So if we want to put a method or attribute private put an underscore but
# IT IS NOT GUARANTEE
player1 = playerCharacter('Bard', 100)

# What about __init__ DOUBLE UNDERSCORE ? it is DUNDER METHOD
# it is ONLY a Convention but there are others DUNDER METHODS ready to use,
# so it is say Dont Modify that

# 3) INHERITANCE
class User():
	def sign_in(self):
		print('logged in')

class Wizard():
	pass

class Archer():
	pass

#How can we make sure that all of these users/classes also have access to sign in
#WE USE A INHERITANCE
#How do we do ? IN THE BRACKETS PASS THE PARENT CLASS (here User)

class User(): # MAIN CLASS
	def sign_in(self):
		print('logged in') #

class Wizard(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, power):
	 	self.name = name
		self.power = power

	def attack(self):
		print(f'attacking with power {self.power}')

class Archer(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, num_arrows):
	 	self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Legolas', 100)
wizard1.attack() #attacking with power of 50
archer1.attack() #attacking with arrows: arrows left- 100

# 3) POLYMORPHISM (PLUSIEURS FORMES)

class User(object): # MAIN CLASS
	def sign_in(self):

class Wizard(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, power):
	 	self.name = name
		self.power = power
	def attack(self):
		print(f'attacking with power {self.power}')

class Archer(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, num_arrows):
	 	self.name = name
		self.num_arrows = num_arrows
	def attack(self):
		print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Gandalf', 60)
archer1 = Archer('Legolas', 40)

def player_attack(char):
	char.attack()

player_attack(wizard1) # attacking with power of 60
player_attack(archer1) # attacking with arrowa: arroews left- 40
# THE SAME FUNCTION GIVES ME A DIFFERENT OUTPUT
#BECAUSE OF THE OBJECT THAT WE PASS INTO IT > POLYMORPHISM

class User(object): # MAIN CLASS
	def sign_in(self):

class Wizard(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, power):
	 	self.name = name
		self.power = power
	def attack(self):
		print(f'attacking with power {self.power}')

class Archer(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, num_arrows):
	 	self.name = name
		self.num_arrows = num_arrows
	def attack(self):
		print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Gandalf', 60)
archer1 = Archer('Legolas', 40)

for char in [wizard1, archer1]:
	char.attack()
# attacking with power of 60
# attacking with arrowa: arroews left- 40
# THE SAME FUNCTION GIVES ME A DIFFERENT OUTPUT
#BECAUSE OF THE OBJECT THAT WE PASS INTO IT > POLYMORPHISM

class User(object): # MAIN CLASS
	def sign_in(self):

	def attack(self):
		print('do nothing') # we give default attack to user

class Wizard(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, power):
	 	self.name = name
		self.power = power
	def attack(self):
		print(f'attacking with power {self.power}')

class Archer(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, num_arrows):
	 	self.name = name
		self.num_arrows = num_arrows
	def attack(self):
		print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Gandalf', 60)
archer1 = Archer('Legolas', 40)
print(wizard1.attack()) # attacking with power of 60 \n None
#ITS GOING TO OVERIDE WHEREVER THE ORIGINAL ATTACK WAS
#BECAUSE WE ALREADY HAVE THAT METHOD IN OUR WIZARD CLASS !

class User(object): # MAIN CLASS
	def sign_in(self):

	def attack(self):
		print('do nothing') # we give default attack to user

class Wizard(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, power):
	 	self.name = name
		self.power = power
	def attack(self):
		User.attack(self) #we can use User cause it is innitialized in parameters
		print(f'attacking with power {self.power}')

class Archer(User): # SUBCLASSE = DERIVED CLASS
	def __init__(self, name, num_arrows):
	 	self.name = name
		self.num_arrows = num_arrows
	def attack(self):
		print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Gandalf', 60)
archer1 = Archer('Legolas', 40)
print(wizard1.attack()) # do nothing
						# attacking with power of 60
						# None
# SO POLYMORPHISM ALLOWS US TO HAS MANY FORMS/WAYS

# ---------------------------------
# Super()

class Wizard(User):
	def __init__(self, name, power, email):
		self.__init__(self, email)
		self.name = name
		self.power = power

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)

# With SUPER() we don't need self !
class Wizard(User):
	def __init__(self, name, power, email):
		super().__init__(email)
		self.name = name
		self.power = power
# Super() allows us to refer to User so we dont have to care about self

# --------------------------------------------
# INTROSPECTION
# Ability to determine the type of an object while the program is running

print((dir(wizard1.)))
 # Show us all DUNDER METHODS !
 #Explain Dunder Methods

 class Toy():
	 def __init__(self,color,age):
		 self.color = color
		 self.age = age

action_figure = Toy('red', 0)
print(action_figure.__str__()) #<__main__.Toy object at 0x7fce56778>
print(str(action_figure)) #<__main__.Toy object at 0x7fce56778>
#THE SAME THING jut the first is DUNDER STR (Special Method)
 class Toy():
	 def __init__(self, color, age):
		self.color = color
		self.age = age
		#dictionary added for the def __getitem__
	 	self.my_dict = {
			'name': 'Bernard',
			'has_pets': False
		}

	def __str__(self):
		return f'{self.color}' #we have modified the dunder string method

	def __len__(self):
		return 5

	def __del__(self):
		print('deleted')

	def __call__(self):
		return ('yess?')

	def __getitem__(self, i):
	return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure)) # red
print(len(action_figure)) # 5
del action_figure # deleted
print(action_figure()) # yess?
print(action_figure['name']) # Bernard

# ----------------------------------------
# create a super list

class SuperList():
	def __len__(self):
		return 1000

super_list1 = SuperList();

print(len(super_list1)) #1000
super_list1.append(5) # ERROR SuperList object has no attribute append
# super_list1[5]
# ----
class SuperList(list):
	def __len__(self):
		return 1000

super_list1 = SuperList();

print(len(super_list1)) # 1000
super_list1.append(5) # ERROR SuperList object has no attribute append
super_list1[0] # 1000 (you have to PRINT)
print(super_list1[0]) # 5
# --- VERIFY IF OBJECTS ARE SUBCLASS ETC...
print(issubclass(SuperList,list)) # True
print(issubclass(list,object)) # True

# ----------------------------
# MODULES (differents files main.py, utility.py...)
#main.py
import utility #or utility.py
#by importing you make connection between different files
print(utility)
#we have generated a folder __pycache__ with file .pyc
#we always generate that by using import
#

#utility.py
def multiply(num1,num2):
	return num1*num2

def divide(num1,num2):
	return num1/num2
# -------
# If we have a package under another package
import utility
import packagename.packagename.module

print(packagename.packagename.module.buy('apple')) # ['apple']
# make SHORTER :
import utility
#or
from utility import multiply, divide #(max)
from packagename.packagename.module import function #func is buy here
print(buy('apple'))
print(divide(5,2))
print(multiply(5,2))
print(max([1,2,3]))

# from module import * (* = everything)

# __name__
print(__name__) #file dir. ex: course.exos.filename

if __name__ = '__main__':
	print('Lectoise de Lect? On s\'en delecte')
# Notre fichier principal, bidule.py ou autre,
# sera toujours considéré comme MAIN FILE
# cad que peut importe le nom de notre fichier principal
# duquel nous lançons le programme (le compiler)
# si le __name__ (nom du fichier)
# = '__main__' (est le main file le ficher principal)
# alors ecris 'Lectoise....'
# mais si on met if __name__ = '__main__'
# dans un fichier secondaire que l'on IMPORTE via import...
# alors 'lectoise...' ne saffichera pas car le name != main

# on the main file called university.py :
class Student():
	pass

std1 = Student()
print(type(std1)) #<class '__main__.Student"> our class is in the MAIN File.

# now in the other file utility.py we write:
class Student():
	pass

std1 = Student()
# and in our main file university.py we write:
import utility

print(type(utility.std1)) #<class 'utility.Student'>
#cause our class was created in utility file

# -----
import random

my_list = [1,2,3,4,5]
random.shuffle(my_list) #Shuffle is to melanger
print(my_list) #[4,3,5,1,2]

import random as SanPellegrino #we can rename as we want!

my_list = [1,2,3,4,5]
SanPellegrino.shuffle(my_list)
print(my_list) #[4,3,5,1,2]
# ------------------------
#SPECIALIZED DATA TYPES

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7]
print(Counter(li)) #it is creating a dict
#Counter({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7})

li2 = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
#Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
print(Counter(sentence))
#Counter({'h': 5, ' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 3, 'i': 2, 'o': 2, 'k': 1, 'g': 1, 'u': 1, 'p': 1, 'y': 1})

dictionary = {'a': 1, 'b': 2}
print(dictionary['a']) #1
print(dictionary['c']) #ERROR cause c doesnt exist
#but the function defaultdict sert à corriger ça
dictionary = defaultdict({'a': 1, 'b': 2})
print(dictionary['c']) #ERROR first arg must be callable or None

dictionary = defaultdict(int,{'a': 1, 'b': 2})
print(dictionary['c']) #0 cause it is like print(int())

dictionary = defaultdict(lambda: 4,{'a': 1, 'b': 2})
print(dictionary['c']) #5

dictionary = defaultdict(lambda: 'doesnt exist',{'a': 1, 'b': 2})
print(dictionary['c']) #doesnt exit
print(dictionary['a']) #1

# -----
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['a'] = 1
d['b'] = 2

print(d2 == d) #True

#but
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['a'] = 2
d['b'] = 1

print(d2 == d) #False

#------
d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d['b'] = 2
d['a'] = 1

print(d2 == d) #True

# -----------------------------
# ERROR HANDLING
# When there is an error, the program stops working and
# send an error message.
# it is bas and can cost thousands of money to a company
# of their service is crashing like that
# so HANDLING ERRORS are used BY the developer
# In The Code to make the program still working even if there
# are errors.
