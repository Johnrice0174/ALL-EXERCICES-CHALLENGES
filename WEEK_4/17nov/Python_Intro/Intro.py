#FUNDAMENTAL DATA TYPES
int = integer
float = nombres à virgule
bool
str = string #letters
print()
input() #
type() #give us wich type is an element
list
tuple
set
dict
True  #CAPITAL T (not like others lang)
False #CAPITAL F (not like others lang)
#CLASSES -> Custom Types

#SPECIALIZED Data Types
#NONE
None = nothing

weapons = None
print(weapons) #None
None #[]

---------------------------
#OPERATORS
>
<
= #Assignment (we assign a value to an element)
== #Equal
!= #NotEqual
>=
<=
is #equal in STRINGS!! 'string' is 'string'(we can use ==)
is not #not equal...idem... (we can use !=)
and #True and False _ False
or #True or False _ True
----
#Operators PRECEDENCE
() #parentheses
** #power
*/ #mult and div
+- #add and sub
_____
print(True == 1) #True
print('' == 1) #False
print('1' == 1) #False
print([] == 1) #False
print(10 == 10.0) #True
print([] == []) #True
#ok but what ?
#the Double Equal Convert like bool()
#What about IS ?
print(True is 1) #False
print('' is 1) #False
print('1' is 1) #False
print([] is 1) #False
print(10 is 10.0) #False
print([] is []) #False
#Equals look for equality in VALUES and TYPES
#IS is chechking about the location in memory.
print('1' is '1') #True
print([] is []) #False
#WTF why ? cause each list has a different place in memory


----------------------
#INT AND FLOAT
print(2 + 4) #result : 6
print(2 - 4) #-2
print(2 * 4) #8
print(2 / 4) #0.5

print(type(2 + 4)) #<class "int">
print(type(2 - 4) #<class "int">
print(type(2 * 4) #<class "int">
print(type(2 / 4) #<class "float">

print(type(0.000001)) #<class "float">
print(type(5.09938401)) #<class "float">

print(type(0)) #<class "int">

print(type(20+1.1)) #<class "float">
print(type(9.9+1.1)) #<class "float"> cause result is 11.0 and not 11


print(2 ** 2) #Put 2 times the sign > return an INTEGER !
print(2 ** 2) #8
print(2 // 4) #0
print(5 // 4) #1

print(5 % 4) #modulo _ result: 1 (show the remainder)
print(6 % 4) #2

#MATH FUNCTIONS
round = arrondir 
print(round(3.1)) #result: 3
print(round(3.9)) #result: 4

abs = absolute =
print(abs(-20))


# VARIABLES 
iq = 190
esfgrdht = 324

print(iq)

# 5 RULES for a VARIABLE 

1) snake_case 
2) start with lowercase or underscore
3) Letters, numbers, underscores
4) case sensitive
5) don't overwrite keywords

#1-2-3) the variable has to be 
dog
strong_dog
str0ng_dog9
_strong_dog #underscore = private variable

#4) we cant call the variable if it is not called 
#EXACTLY like in the Declaration :

user_IQ = 190 -----> print(user_iq) #WON'T WORK
#it has to be like the first
user_IQ = 234   ----> print(user_IQ) #good

#5) we cant use a keyword as variable name
print = 4
print(print) #OMG NEVEEER !!
#dont use as variable name print int float etc....


#A GOOD DEVELOPER/PROGRAMER COMMENT/DESCRIBE/NAME THINGS !!
bulle = 10 
---
#bin()
#all int and float are stocked in BINARY MEMORY
#If we want convert int/float in his Binary version:
print(bin(5)) #0b101
print(int('0b101', 2)) #2 is basis
------------------------------
iq = 190
user_age = iq/4
a = user_age
print(a) #result: 47.5


#CONSTANTS variables
PI = 3.14
#UPPERCASE means that the variable is CONSTANT
#so can't change !! but we can change it manually :
PI = 0
PI = 4 #etc...
----------------------------

a,b,c = 1,2,3
print(a)
print(b)
print(c)
#result> 1 2 3

-------------------------------
#DEVELOPER FUNDAMENTAL
/!\ Dont read the dictionary
you dont have to memorize all!
YOU HAVE TO USE not just READ/MEMORIZE to Learn a language!/!\


----------------------------------
#17nov COURSE jonathan
immutable
strings are immutable...

array[1,2,3]
array[2] = 100
array[]
?????????????

x = 1
name = 'john'

print('hello' + name)

---------------------------
UN input NE RENVOIE QUE DES CHAINE DE CARACTERE (string);
donc il faut convertir en int !!

age = input('Enter age: ')
Enter age: 20
age
'20'

type(age)
<class 'str'>
age_as_number = int(age)
age_as_number
20

age_as_number+=1
age_as_number
21
age_as_str = str(age_as_number)
'40'

#way 1
print("Your age next year is " + str(int(input("Enter your age: "))+1))
Enter age: 20
Your age next year is 21
#way 2
age = input("Enter your age: ")
print("Your age next year will be " + str(int(age)+1))

------------------
#STRINGS ! STR >
str.upper()
str.lower()
str.capitalize() #mets un MAJ aux débuts de phrases
str.
--
quote = 'to be or not to be'
print(quote.upper()) #TO BE OR NOT TO BE 
--
print(quote.find('or')) #verifier si ce qu'on cherche
#est dans l'element (ici quote). Si oui, alors le resultat
#est l'index à partir duquel ce quon cherche commence.
--
print(quote.replace('be', 'me')) #remplacer les be par me
#mais en fait ça modifie pas la liste initiale
#car une liste est imutable donc ça va creer une autre
#liste mais qui ne sera pas gardée en memoire apres affichage
#car on ne l'a pas assigné à une var genre quote2.
------
print(type('hellolilol'))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
0 0
---
'''
print(long_string)
input() #to get the system paused after exectued
---
first_name = 'Adrien'
last_name = 'John' 
full_name  = first_name + ' ' + last_name
print(full_name)
input()
---
my_name = "John"
print(my_name[0]) #"R"
print(my_name[2]) #"h
print(my_name[-1]) #"n"
print(my_name[1:3]) #"oh"
---
#STRING CONCATENATION
meaning = Add strings together
print('hello' + 5) #wont work

print(type(str(100))) #we convert this number as String '100'
print(type(int(str(100)))) #we convert this number as String '100' and finally as number 100
---
#type convertion :
a = str(100)
b = int(a)
c = type(b)
print(c)
input() #get system pause after executing

----------------------------
BACKSLAH IS SPECIAL CHARACTER:
you cant print it like that 
print("this is a backslash \") !! #NOPE
you have to make :
print("this is a backslash \\")

FOR QUOTES :


-----------
Newline, backslash n > #\n
big space, backslash t > #\t

------------------------------------
#BOOLEANS
bool("True")
True
bool("False")
True

function bool()
----
#like in fb profil
name = 'John'
is_cool = False #myprofil isnot cool
is_cool = True #i have modified so yes it is now!

print(bool(1)) #True
print(bool(0)) #False
print(bool('True')) #True

#operators in Boolean
>
<
== #Equal
!= #NotEqual
>=
<=
is #equal in STRINGS!! 'string' is 'string'(we can use ==)
is not #not equal...idem... (we can use !=)
and #True and False _ False
or #True or False _ True

------
#TRUTHY AND FALSY VALUES !
#if we print the boolean conversion of a value:
print(bool('hello')) #True (so it is a truthy value)
print(bool(5)) #True (Truthy Value)

print(bool('')) #False (Falsy value)
print(bool(0)) #False (Falsy value)

#https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
--------------------------
%f #float
%d #int
%s #str
age = 100
print("Your age is %d" % (age))
print("Your age is %d, and next year you will be %d" % (age, age+1))

name = "John"
print("%s's age is %f, and next year you will nbe %d" % (name, age, age+1))

----------
print("Hello {}, your age is {}".format(name, age))
print("Hello {first}, your age is {second}".format(first=name, second=age))
print("Hello {name}, your age is {age}".format(name=name, age=age))

--------
My name is John, I am 20 years old.
print(f'This is text with a {variable}')
print("This is text with a {}".format(variable))
print("This is text with a {myvar}".format(myvar=variable))
print("This is text a %s or %d" % (variable)) %s = string %d = decimal

----------
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha[5] #display f 
alpha = alpha.replace("f","F") #replace f by F !you have to add into a var!

String addressing works like arrays. with [i] square brackets.
The square brackets have the form [start : end]
So how do we print letters d to j ?

alpha[3:10] #like that

Start is INCLUSIVE. #genre 4 affichera la 4e lettre
End is EXCLUSIVE.	#genre 4 affichera la 3e lettre

alpha[3:999] #cela affiche jusqu'à la fin du string donc ça marche mais USELESS !
alpha[3:] #sans mettre de nombre à la fin cela affiche jusqu'à la fin du string.
alpha[:10] #cela affiche les 10 premieres lettres
alpha[-1] #affiche le 1er caractere DEPUIS LA FIN du strinf, ici 'z'
alpha[-5] #les 5 dernieres lettre, ici 'vwxyz'
alpha[:] #affiche tout le contenu du string


Using [start : end : step] print the string backwards (afficher le string a lenvers)
alpha[26 : 0 : -1] #affiche de z à b... et pas le a car end is EXCLUSIVE-_-
alpha[27 : 0 : -1] #affiche de z à b... et pas le a car end is EXCLUSIVE-_-
alpha[27 : -1 : -1] #rien car -1 = z  -_-
alpha[:: -1] #WTF MAN Ça marche lol xD

Create a string containing the numbers 1 to 9
and print the even numbers #even=pair
num = "123456789"
num[1:10:2] #correct mais pas parfait
'2468'
num[1::2] #parfait car meme si on met rien ça va jusquà la fin du string
'2468'
num[::2] #dans ce cas ce sont les impairs car [0] = 1 !!
'13579'

display 963 >
num[10::-3] #correct 
num[::-3] #perfect

num[::3] #147
----
selfish = "me me me"
          #01234567 #ordre d'hébergement dans la memoire
print(selfish[0]) #result m
print(selfish[7]) #result e
print(selfish) #result me me me

# [start:stop:stepover]
print(selfish[0:2])
print(selfish[0:7]) #0123456
print(selfish[0:8]) #01234567
print(selfish[0:8:1]) #01234567
print(selfish[0:8:2]) #0246
print(selfish[1:]) #1234567 (de 1 à là ou ya plus rien)
print(selfish[::1]) #01234567 (de rien a rien 1 par 1)

print(selfish[-1]) #7 (commence à la fin)
print(selfish[-3]) #5
print(selfish[::-1]) #7654321 (REVERSED)
print(selfish[::-2]) #7531

-----
#FORMATED STRINGS
name = 'John'
age = 20
print('Hi ' + name + 'You are ' + age + 'year old')
#NE FONCTIONNE PAS IL FAUT CONVERTIR AGE EN STRING
print('Hi ' + name + 'You are ' + str(age) + 'year old')
#CI DESSOUS Formated String (f et {} dans le print)
print(f'Hi {name}. You are {age} years old')
#but (.format a la fin est PYTHON 2 mais work on Pyth3)
print(Hi {}. You are {} years old).format('John', '20')
#NE MARCHE PAS CAR FORMAT FONCTIONNE AVEC STRINGS
#ET PRINT NEST PAS UN STRING DONC INTEGRER LE
#.format A L'INTERIEUR !!! 
print('Hi {}. You are {} years old'.format('John', '20'))
#OR ALSO
print('Hi {}. You are {} years old'.format(name, age))
#OR ALSO
print('Hi {0}. You are {1} years old'.format(name, age))
#OR ALSO
print('Hi {1}. You are {0} years old'.format(age, name))
#ci dessus on comprend que a la fin l'ordre des var
#nest pas grave si on ecrit l'ordre par 0 1 etc...
#OR ALSO
print('Hi {new_name}. You are {age} years old'.format(new_name='Jack', age=280))
#FINALLY PREFERABLE TO USE Pyth3 syntax print(f"{}")

#CECI NE FONCTIONNE PAS :
print(f'Hello {name='Cindy'}, your balance is {amount='50'}.')
---------------------

# EXPRESSION vs STATEMENT
id = 100 #statement
user_age = id / 5
id / 5 # expresssion
user_age = id / 5 #statement !!

------------------------------

#Augmented Assignement Operator

counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2

print(counter)
#result 6 ! chaque s'ajoutent entre elles
0
1
2
3
4
3
3*2 = 6

--------------------------

#ESCAPE SEQUENCE

weather = 'It\'s sunny' #backslash pour apostrophe
#sauf si :
weather = "It's kind of sunny"
#pour faire un text entre guillement :
desc = 'I\'m the \"king\" of the school'
print(desc) #result I'm the "king" of the school

#Double backslash to display a backslash:
ingredients = "water\\sugar\\other..."
print(ingredients) #water\sugar\other...

---
#Backslash t > \t (add Tab Space)
#Backslash n > \n (newline)
-----------------------
#LISTS
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a', True]

#DATA STRUCTURE is a way to store.
#Lists help us to contain, stock datas...

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0]) #= notebooks
print(amazon_cart[1]) #= sunglasses
---
#display list  10,9,8,7,6,5
list(reversed((range(5, 11)))) #yes work but it is bad
list(range(10,4,-1)) #shorter so BETTER
[10-i for i in range(6)] #Professional PERFECT
--
#display list 2, 4, 8, 16, 32, 64, 128
[2**i for i in range(1,8)] #Professional PERFECT
#LISTS SLICING
# string = 'hellloo'
# string[0:2:1]
amazon_cart = [
	'notebooks', 
	'sunglasses',
	'toys',
	'grapes'
]
greet = 'hello'
greet[0] = 'bye' #String is immutable it will not change
#but list we can change :
print(amazon_cart[0::2])
amazon_cart[0] = 'laptopt' #laptop will replace notebooks
new_cart = amazon_cart[0:3] #now the new is same as amazon
new_cart = amazon_cart[:] #now the amazon is different
new_cart[0] = "gum"
print(amazon_cart[0:3])
print(amazon_cart)
---
#ADD ELLEMENT to LIST
append()
print(my_hobbies) #["Debatte", "Play", "Eat"]
my_hobbies.append("Sleep") #["Debatte", "Play", "Eat", ""]
my_hobbies.insert(position, 'element')
my_hobbies.extend(['women']) 

#REMOVE-DELETE ELEMENT from LIST
my_hobbies.remove("element")
my_hobbies.pop("element") #pop remove the last element
#or the element you have writed
my_hobbies.clear() #remove all
----
#COPY != EQUAL
list1 = ["a","b","c"]
list2 = list1 #Now List2 has a different place in memory but he is referring to THE SAME ID REF MEMORY of list1
#so
list2.append("d") #list1 will ALSO get "d" !!!!

#now if COPY
list2 = list1.copy()
list2.append("e") #list1 will NOT get "e" !!! because you have only COPIED the value, not the ID REF in Memory.

---
#LENGTH !!
fruits = ['mango', 'apple', 'banana']
length_of_fruits = len(fruits) #result 3 here
print(len(fruits))
-
greet = 'heellloooo'
print(greet) #heellloooo
print(greet[:]) #heellloooo
print(greet[0:len(greet)]) #heellloooo
--
#ORDONNER TRIER (CROISSANT ou ALPHABETIQUE)
sorted_fruits = sorted(fruits)
print(sorted_fruits)
#['apple', 'banana', 'mango']
nums = [45, 30, 6]
sorted_nums = sorted(nums)
print(sorted_nums)
#[6, 30, 45]
#WE CANT SORTED A MIXED LIST (strings, nums)
mixed_values = ['mango', 14, 'grape', 4]
sorted_mixed_values = sorted(mixed_values)
print(sorted_mixed_values) #ERROR
--
#CALCULATE SUM OF NUMS 
prices = [4, 14, 18, 20]
sum_of_prices = sum(prices)
print(sum_of_prices) #56 !!
--
# CREATE CHAR LIST
my_list = [char for char in 'hello']
print(my_list) #['h','e','l','l','o']
--
# NUM LIST
my_list2 = [num for num in range(0,101)]
print(my_list2) #[0,1,...,99,100]
my_list2_2 = [num*2 for num in range(0,100)]
#[0,2,4,...,196,198,200]
my_list2_3 = [num**2 for num in range(0,100)]
#[0,1,4,9,16,...,9409,9604,9801,10000]
my_list2_4 = [num**2 for num in range(0,100) if num % 2 == 0]
#
--
# INIFINITE LOOP LIST
def make_lisat(num):
	result = []
	for i in range(num):
		result.append(i*2)
	return result

my_list = make_list(100)
print(list(range(1000000)))
----
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicates:
			duplicates.append(value)
print(duplicates) #['b','n']
--
some_list = ['a','b','c','b','d','m','n','n']
duplicates = [x for x in some_list if some_list.count(x) > 1]
print(duplicates) #['b','b','n','n']
-
some_list = ['a','b','c','b','d','m','n','n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates) #{'b','n'}
-
some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates) #['b','n']
--
#ACCESSING !!!
religions = ['Judaisme',['Christianisme',['Catholicisme','Protestantisme','Orthodoxie'], 'Islam',['Sunnisme','Chiisme']]]
print(religions) #['Judaisme', ['Christianisme', ['Protestantisme', 'Catholicisme', 'Orthodoxisme'], 'Islam', ['Sunnisme', 'Chiisme']]]
print(religions[0]) #Judaisme
print(religions[1]) #['Christianisme', ['Protestantisme', 'Catholicisme', 'Orthodoxisme'], 'Islam', ['Sunnisme', 'Chiisme']]
print(religions[1][0]) #Christianisme
print(religions[1][1]) #['Protestantisme', 'Catholicisme', 'Orthodoxisme']
print(religions[1][1][0]) #Catholicisme
print(religions[1][1][1]) #Protestantisme
print(religions[1][1][2]) #Orthdoxie
print(religions[1][2]) #Islam
print(religions[1][3]) #['Sunnisme', 'Chiisme']
print(religions[1][3][0]) #Sunnisme
print(religions[1][3][1]) #Chiisme
---
#List UNPACKING
a,b,c, *other = [1,2,3,4,5,6,7,8,9] #star=all the rest (unpacking)
#other is a random name i can rename it.
print(a) #1
print(b) #2
print(c) #3
print(other) #[,5,6,7,8,9]
#if we add d ?
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(other) #[4,5,6,7,8]
print (d) #9
--
basket = ['a','x', 'b','c','d','e', 'd']
basket.sort() #ordonner
basket.reverse() #inverser
print(basket[::-1]) #['a','b','c','d','d','e','x']
print(basket) #['x','e','d','d','c','b','a']
print(basket[:]) #make a copy of the list
--
print(range(1,100)) #1,100
print(list(range(1,100))) #[1,2,3,4,5,...,97,98,99]
#range 101 to get list 1-100.
--
sentence = ' ' #espace/element entre les elements
show_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOHN'])
print(show_sentence) #hi my name is JOHN 
----
#ENUMARATE
for i, char in enumerate('Hello'):
	print(i, char)
#0 H
#1 e
#2 l
#3 l
#4 o
--
for i, char in enumerate(list(range(100))):
	print(i, char)
	if char == 50:
		print(f'index of 50 is: {i}')
----------------------------
#DICTIONNARY is a DATA STRUCTURE
mydict = {"a": "AAA", "b": "BBB"}
dict()
---
dictionary = {
	'a': [1,2,3],
	'b': 'hello',
	'x': True
}
#DICT Inside LIST:
my_list = [
	{
	'a': [1,2,3],
	'b': 'hello',
	'x': True
	},
	{
	'a': [4,5,6],
	'b': 'hello',
	'x': True
	}
]
#Display Select
#print(name[whichInList][KeyName][WhereElementInValue])
print(my_list[0]['a'][2]) #result 3
print(dictionary['a'][1]) #resul 2
--#OBJECTS
user = {
	'name': 'Golem',
	'age': 5006,
	'can_swim': False
}
for item in user:
	print(item)
#results: name age can_swim
for item in user.items():
	print(item) 
#results: ('name': 'Golem')
         #('age': 5006)
         #('can_swim': False)
for item in user.values():
	print(item)  
#results: Golem, 5006, False
for item in user.keys():
	print(item)
#results: name age can_swim
for key, value in user.items():
	print(key, value)
#results: name Golem
         #age 5006
         #can_swim False
---
#Display Select
mydict["a"] #'AAA'

mydict = [{},{}]
mydict = {}

#define keys, str as key, num as key and tuple as key
mydict = {
	"a" : "AAA",
	1 : "BBB",
	("a","b"): "CCC"
}
print(mydict)
---
#create dictionary {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
mydict = {i:i**2 for i in range(10)}
mydict[5] #25
---
# CREATE CHAR DICT
my_list = [char for char in 'hello']
print(my_list) #['h','e','l','l','o']
--
# NUM DICT
my_list2 = [num for num in range(0,101)]
print(my_list2) #[0,1,...,99,100]
my_list2_2 = [num*2 for num in range(0,100)]
#[0,2,4,...,196,198,200]
my_list2_3 = [num**2 for num in range(0,100)]
#[0,1,4,9,16,...,9409,9604,9801,10000]
my_list2_4 = [num**2 for num in range(0,100) if num % 2 == 0]
#
---
#videogame characher by DICTIONARY
dictionary = {
#	'key': value,
	'life_points': 100,
	'shield': 50,
	'skills': None,
	'head_oneshot': True,
	'fly': False
}
#EACH KEY has a DIFFERENT Place in Memory
#on Lists each index is next to the other li[1] li[2]
#in Dictionary 'key_one' is stocked at #54678
#and 'key_two' at #76543
--
dictionary = {
	123: [1,2,3],
	True: 'Hello',
	[100]: True
}
print(dictionary[123]) #[1,2,3] OK
print(dictionary[True]) #Hello OK
print(dictionary[100]) #ERROR cause
#a Key has to be IMMUTABLE !
#string, Boolean, Number are IMMUTABLE
#but a List is NOT so we cant rename dictionary key
#as list [100]!
#So you can use TUPLE but 99% of the time,
#Keys are STRINGS
--
dictionary = {
	123: [1,2,3],
	123: 'Hello'
}
print(dictionary[123]) #Hello =O
#KEY HAS TO BE UNIQUE WE CANT USE THE SAME KEY
#FOR ANOTHER VALUE, IN THIS CASE THE FIRST VALUE 
#IS DEAD ! IT NO LONGER EXIST !
---
user = {
	'basket': [1,2,3],
	'greet': 'hello'
}
print(user['age']) #ERROR age doesnt Exist!!
#SO USE GET (usable in DICTIONARY and OBJECTS)
print(user.get('age')) #None (YES IT IS WORK)
#None is because we didnt add value to 'age'
#So ADD VALUE !
print(user.get('age', 55)) #Nice! BUT 
#if 'age': 20, is ALREADY in the dictionary
print(user.get('age', 55)) #will display 20, not 55!
--
#SECOND UNUSUAL WAY TO CREATE DICTIONARY
#dictionary_name = dict(key=value)
user2 = dict('name'='JohnRice')
print(user2) #dont Work, 
#[pyflakes] = error and give description of
#KEYWORD CAN'T BE AN EXPRESSION so
user2 = dict(name='JohnRice')
print(user2) #{'name': 'JohnRice'}
---------------------------
#IN CLASS 18nov (WTF)
tuple(d.values())[]
hash
d = dictionary
dir(d) (list of all values)
d.keys()
d.items()

[something] * number 
[item] * 5 #[item, item, item, item, item]

(1+1,)*2 #(2, 2)
(1+1)*2 #4
(1+1,)*10 #(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
(1,2,3)*10 #(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
l=[[item]*3[item]*3[item]*3] #[[item, item, item], [item, item, item], [item, item, item]]

min
help(min)
min(1,2,3,-5) #-5
help(max)
max(1,2,3) #3
max(l) #4
len(l) #4
list(d)
len(d) #4
list(d.keys()) #= list(d)

list(d.values())

d.items()
len(list(d)) #4
abs()
any()
l.sort()

reversed(l)
for i in reverded(l):
	print(i)
#d
#z
#c
#a

help(sum)
help(ord)
ord('5')
ord('5') - ord('0')
type(ord('5') - ord('0')) #<class 'int'>
ord('1') - ord('0') #1
(ord('5') - ord('0')) * 10 #10
(ord('0') - ord('0')) * 1 #0

s = input("Please enter a number: ")
num = 0
div = 10 ** (len(s) - 1)

for digit in s:
	print(digit)

for digit in s:
	num += (ord(digit) - ord('0')) * div

print(num)

--------------------------
# SETS (unordered Sequence Type)
#doesnt support indexing and duplicate too
#use it to make list with no duplicates in it
set()
set.add(element)

my_set = set()
my_set.add("Nameone")
my_set.add("Nametwo")
my_set.add("Nameone") #work but useless, already added

print(my_set) #{"Nameone", "Nametwo"}
--
my_set = {1,2,3,4,5,5,5,5}
print(my_set) #result> {1,2,3,4,5}
#DISPLAY-SELECT ELEMENT 
print(1 in my_set) #True
#LENGTH
print(len(my_set))
#COPY != EQUAL
new_set = my_set #Now new_set has a different place in memory but he is referring to THE SAME ID REF MEMORY of my_set
#so
new_set.add("d") #my_set will ALSO get "d" !!!!

#now if COPY
new_set = my_set.copy()
new_set.add("e") #list1 will NOT get "e" !!! because you have only COPIED the value, not the ID REF in Memory.
#REMOVE ALL ELEMENTS 
my_set.clear()
---
#Johnathan
myset = {"a","b","c"}
mylist = ["a","b","C"]

myset.update("a")
mylist.append("a")

set(mylist)
list(myset)
-------
#SEQUENCES (Ordered Set)
#Sequences can be indexable
#each element can be retrieved with his index:
sequence_name[index_num]
#Sequence is not a data type, it’s a category of data types
#Negative indexes, meaning beginning from the end 
sequence_name[-index_num]
#Range indexes, returns a list from an index to the other
sequence_name[start:end]
#When using ranges, the end index is not included
------------------------
#TUPLE (IMMUTABLE List)
#Why not using LIST... We cant modify TUPLE so it makes
#our code more protectable/safe !
#but it's less flexible
my_tuple = (1,2,3,4,5)
or
mytup = ("a","b","c","a","a")
my_tuple[1] = 'z' #ERROR Tuple doesnt support item assignment
#(a basic LIST is Mutable so we can modify by this method)
print(my_tuple[1]) #Like a list WE CAN ACCESS to any item
print(5 in my_tuple) #true (yes we can verify)

#(good thing about tuples is that they can be unpacked, 
#meaning each value will go to one variable)a, b, c = my_tuple
my_tuple = (5,6,7)
a, b, c = my_tuple
print(a) #5
print(b) #6
print(c) #7

#Tuple can only allow adding tuple to it
mytuple =(u'2',)
mytuple +=(new.id,)
#or
mytuple = (u'2',)
mytuple += ('example text',)
--
histuple = (14)
ourtuple = mytuple + histuple
#Dictionary
user = {
	'basket': [1,2,3],
	'greet': 'hello',
	'age': 20
}
print(user.items())
#a Dictionary has KEYS !
#a Tuples is also a VALID KEY ! ci dessous:
user = {
	(1.2): [1,2,3],
	'greet': 'hello',
	'age': 20
}
print(user[(1,2)])

--------------------
#ITERABLE
list, dictionary, tuple, set, string #are iterable
#cause they can be iterated
#ITERATE -> one by one check each item in the collection
-------------------------------
#CONDITIONS (IF)
a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
#The elif keyword is pythons way of saying 
#if the previous conditions were not true,
#then try this condition".
--
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#The else keyword catches anything which isn't caught 
#by the preceding conditions.
if a > b: print("a is greater than b")
--
a = 2
b = 330
print("A") if a > b else print("B")
--
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
--
#The and keyword is a logical operator,
#and is used to combine conditional statements:
Test if a is greater than b, 
AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

---
#ERRORS (if you are an error int str by use input)
#make :
if int(user_height) < int(height_min): #convert in int
#OR 
var = int(input("..."))

----------------
#TERNARY OPERATORS
condition_if_true if condition else condition_if_false
#if condition (it is verified is the condition is true or false)
#if true so > condition_if_true
#if false > else condition_if_false
#example : like Facebook, is user can message you?
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message) #change True by False to change result
----
#SHORT CIRCUIT
is_Friend = True
is_User = True

print(is_Friend and is_User) #result = True

if is_Friend or/and is_User:
	print('best friends foreever')
----------------------
#LOOPS 
for(i=0; i <= 10; i++) #js, c...
for i in range(0,10) #py

for(i=0; i <= 10, i+=5)
for i in range()

#dictionary 
mydict = {i:i**2 for i in range(10)}
mydict[5] #25
---
["*" * i for i in range(10)] 
#result is:
['','*','**','***','****','*****','******','*******','********','*********']
print("\n".join(['*' * i for i in range(10)]))
#will display:
*
**
***
****
*****
******
*******
********
*********

---
if x > 10 and y > 20: #and, or...
	something
	something2
	something3
	return "a"
return "b"

#If the condition is true so RETURN A if not so RETURN B.

--
list["John", "Alexandra Jane", "Rina"]

if "John" in mylist #py
if "John" is not string: #py

if (mylist.indexOf("John") != -1) #JS
--

for i in range(10):
	here
not here

range(start [, stop[, step]])

--
age = input("Enter your age: ")

if age >= 18:
	print("Beer")
else:
	print("Soda")
--
word = ""
while word != "zzz":
	word = input("Enter a word ")
---
password = ''
while password != 'hello-world-123':
  password = input('What is the top secret password? ')

print('You guessed the right password!')

secret_number = 4

while True:
  user_number = input('Guess the secret number: ')
  if int(user_number) == secret_number:
    print('Congrats! You win!')
    break
  else:
    print('Wrong guess...')
--
i = 0
while i < 50
	print(i)
	break / i+=1 #or break to display only ONE TIME i.
	             #or i+=1 to display 50 times i.
# i = i + 1 } i+=1
--- 
#ELSE with WHILE
while i < 50:
	print(i)
	#break (if you put break the ELSE will never happen)
else:
	print('done')
 ----
for item in (1,2,3,4):
	for x in ['a', 'b', 'c', 'd']:
		print(item, x)
#results:
# 1 a
# 1 b
# 1 c
# 1 d
# 2 a
# 2 b
#etc until 5 d
----
#BREAK CONTINUE PASS
break #stop/exit the loop
continue #go back to the loop 
pass #pass to the next line...
     #useless but we can like that for comment:

examplist = [4,14,16,18,20]
for item in examplist:
	#thinking about it
	pass

i = 0
while i < len(examplist):
	print(examplist[i])
	i += 1
	pass

------------------------
#FUNCTIONS !!! #def = define
def say_hello();
	print('helloooo')

#to USE function we have to CALL it
say_hello() #if you forget parentheses it will not display anything
--
#TO KNOW THE MEMORY LOCATION OF OUR FUNCTION
def func():
	...

print(func) #<function func at 0x7ff987d46e2>

----
#PARAMETERS & ARGUMENTS
def chalom(name, emoji):
	print(f"Hachalom Aaleykhem {name}{emoji}")
#name & emoji are Parameters

chalom('John', '😀') #arguments

#PARAMETERS are when we DEFINE the Function
#ARGUMENTS are when we CALL the function
chalom('Dan', '😀') 
chalom('Yitshaq', '😀') #result Hachalom Aaleykhem Yitshaq 😀
--
#POSITIONAL parameters
#Positional Arguments
chalom('😀', 'John') #result Hachalom Aaleykhem 😀 John
chalom('Yitshaq', '😀')
#positional argument says that the arguments
#have to be displayed in the SAME ORDER we have 
#declared them. 
--
#KEYWORD arguments
chalom(emoji='😀', name='David') #result Hachalom Aaleykhem David 😀
#be carefull that arguments IN THE SAME ORDER of parameters
chalom(name='David', emoji='😀')
--
#DEFAULT PARAMETERS
def chalom(name='Yeshua', emoji='✋'):
	print(f"Hachalom Aaleykhem {name}{emoji}")

chalom('Dan', '😀')
chalom(name='David', emoji='😀')
#THE DEFAULTS PARAMETERS DIDNT CHANGE RESULTS
#if we call more one time this function
#but we forget to put parameters, it will display
#with the DEFAULT Parameters:
chalom() #Hachalom Aaleykhem Yeshua ✋
#Even if we didnt give all arguments
chalom('Rah\'el') #Hachalom Aaleykhem Rah'el ✋

----
#RETURN 
def sum(num1, num2):
	num1 + num2

sum(4,5) #DOESNT WORK DIDNT DISPLAY ANYTHING
print(sum(4,5)) #HAS DIPLAYED None ! WTF xD
#we have to RETURN SOMETHING !
def sum(num1, num2):
	return num1 + num2

print(sum(4,5)) #9 
print(sum(10,5)) #15

#a function can MAKE something A and return something B
def sum(num1, num2):
	print("Rien à voir mais j'aime les pâtes")
	return num1 + num2

print(sum(4,14)) #Rien à.... 18

/!/ a Function Should do one thing really well /!/
/!/ Should return something /!/
#but it is not necesseraly bad that func makes many things
#but the name of the func is SUM so WHY my program says something OFF TOPIC
--
#assign the func result to a variable
total = sum(4,14)
print(sum(10,total)) #print sum of 10 + total xD
--
#Func in Func
def sum(num1, num2):
	def another_func(num1, num2):
		return num1 + num2

total = sum(10, 20)
print(total) #Result will be None (WHY ?!)
#because the return is for another_func, not for sum
#so 1) we didnt return anything in sum func. 
#2) we didnt call another_func !

def sum(num1, num2):
	def another_func(num1, num2):
		return num1 + num2
	return another_func

total = sum(10, 20)
print(total) #result is the place in memory =O -_-
#we have different way to execute properly

print(total(10,20)) #30. ok bof bof
#or
def sum(num1, num2):
	def another_func(num1, num2):
		return num1 + num2
	return another_func(num1, num2)#add parameters name

print(total) #30

#but this function is Unusual, not CLEAR
/!/ A Function has to be CLEAR, EASY to understand /!/

def sum(num1, num2):
	def another_func(n1, n2):
		return n1 + n2
	return another_func(num1, num2)

---
#ONLY ONE RETURN FOR EACH FUNCTION
def another_func(n1, n2):
	return n1 + n2 #return answer and EXIT the function
	return 5 #USELESS (the program won't even read that)
	print('weae') #USELESS (the program won't even read that)

---
#CLEAN CODE
def is_odd_or_even(num):
	if num % 2 == 0: #even number in this case
		return True
	else num % 2 != 0 #odd num
		return False

print(is_odd_or_even(50)) #True
print(is_odd_or_even(51)) #False
#How can we CLEAN this code :

def is_even(num):
	if num % 2 == 0: #even number in this case
		return True

	return False

#We can CLEAN MORE :
def is_even(num):
	return num % 2 == 0: #even number in this case

-----
#SCOPE 
#(what variables do I have to access to?)
total = 100 #Global variable, also global scope

def some_func():
	total = 100 #Local scope. 
--
a = 1 #global scope

def confusion():
	a = 5 #local scope
	return a

print(a) #1
print(confusion()) #5
--
a = 1

def parent():
	a = 10 #local
	def confusion():
		return a #will search the global
    return confusion()

print(parent()) #10
print(a) #1
--
a = 1
 
def parent():
	def confusion():
		return sum
    return confusion()

print(parent()) #<built-in function sum>
                #search sum in the local, parent and global and python
                #sum has been founded in Python so it dont give error
print(a) #1

#so 4 RULES OF SCOPE (Where it is searching variables)
#1 - start with local
#2 - parent local ?
#3 - global
#4 - built in python functions
--
#WHY DO WE NEED SCOPE ?
def outer():
	x = "local"
	def inner():
		x = "nonlocal"
		print("inner:", x) #inner: nonlocal

inner()
print("outer:", x) #outer: local

outer()
--
#NONLOCAL 
nonlocal #the PARENT Variable.
#it like saying :
#"I want to use a variable NOT Global but Outside the function"
def outer():
	x = "local"
	def inner():
		nonlocal x
		x = "nonlocal"
		print("inner:", x) #inner: nonlocal

inner()
print("outer:", x) #outer: nonlocal

outer()
-----
#PARAMETERS (are locals variables)
total = 0
def count():
	total += 1
	return total
print(count()) #ERROR total NOT DEFINED
--
total = 0
def count():
	total = 0
	total += 1
	return total
print(count()) #1
#mais si on veut appeler la function plusieurs fois
#pour obtenir 3.
count()
count()
print(count()) #1 (pas 3 parce que à chaque qu'on relance
#la fonction on redefinit total à 0. donc USELESS
#Alors COMMENT ? use GLOBAL variable :
total = 0
def count():
	global total #var declaration
	total += 1
	return total
count()
count()
print(count()) #3
#BUT THIS WAY IS NOT GOOD!! (to use extern variable)
#WE HAVE TO USE FUNCTION PARAMETERS !!
total = 0
def count(total):
	total += 1
	return total
print(count(count(count(total)))) #3 
#WTF ?! look:
print(count(count(count(0))))
#the first count will add one so result 1:
print(count(count(1)))
#the second count will add one so result 2:
print(count(2))
#the last count called will add one so result and print 3
print(3) 
-----
#METHODS vs FUNCTIONS
list()
print()
max()
min()
input()

def some_random_stuff():
	pass

some_random_stuff()

'hello'.capitalize() 
#a Method cant be alone like called function.
#a method after something (using . to separate)

---
#DOCSTRINGS
def test(a):
	'''
	Info: This function tests and prints param a
	'''
	print(a)

test('!!!!')
test() #the info msg will be in a bulle when we 
#mousein to test().
--
print(test.__doc__) #Info : this func....

----
#ARGS & KWARGS (Arguments & )
#*args **kwargs
def super_func(args):
	return sum(args)

super_func(1,2,3,4,5) #not Working cause we have only ONE argument

def super_func(*args):
	print(*args)
	return sum(args)

super_func(1,2,3,4,5) #1 2 3 4 5
---
def super_func(*args):
	print(args)
	return sum(args)

super_func(1,2,3,4,5) #(1, 2, 3, 4, 5) #tuple
---
def super_func(*args):
	print(args)
	return sum(args)

print(super_func(1,2,3,4,5)) #15

#args is the (*) and allows us to use (1,2,3,4,5) as argument
#but not keywords. and we can rename as we want:
def func(*weshhhh) #it is ok
---
#KWARGS is (**) allows us to use keywords as argument
def super_func(*args, **kwargs):
	print(kwargs)
	return sum(args)

print(super_func(1,2,3,4,5, num1=5, num2=10))
#result: {'num1': 5, 'num2': 10} #we get dictionary
#resultsuite: 15
--
def super_func(*args, **kwargs):
	total = 0
	for items in kwargs.values():
		total += items
	return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))
#30
#ordre priorité pour placer dans les param
/!/Rule: params, *args, default parameters, **kwargs

def super_func(*args, i='hi', **kwargs):
	total = 0
	for items in kwargs.values():
		total += items
	return sum(args) + total

print(super_func('John', 1,2,3,4,5, num1=5, num2=10))
#30 #it is work

-----------------------------
#LIBRARIES 

sys, random...

Other Libraries are naturally part of pyhon. 
but are not included by default, you have to install them
django...

---------------------------------
#JSON (Javascript Object Notation)
#2) is a syntax for storing ans exchanging data
#is text written with JavaScript object notation

#2 > used to send data between machines.

JSON.parse()
var obj = JSON.parse('{"name":"John", "age":"20", "city":"Ashdod"}')

JSON.stringify()
var myJSON = JSON.stringify(obj)
--------------
#XML 
#the same task, just XML use html syntax.
----
#We will use more JSON cause of it is more clear

--------------------------
#GUI (Graphical User Interface)
picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
]
for image in picture:
	for pixel in image:
		if (pixel):
			print('*', end="")
		else:
			print(' ', end ="")
	print('')

for image in picture:
	for pixel in image:
		if (pixel):
			print('*', end="")
		else:
			print(' ', end ="")
	print('')

   *
  ***
 *****
*******
   *
   *
#WE ARE REPEATING OURSELF SO MAKE FUNCTION
def show_tree():
	for image in picture:
	for pixel in image:
		if (pixel):
			print('*', end="")
		else:
			print(' ', end ="")
	print('')

show_tree()
show_tree()
show_tree() #if we call the function BEFORE the function
#it will not work cause the program doenst know that
#the functin exist. it reads line by line !
--------------------
#IMMUTABILITY (CANNOT BE CHANGED)
Key, Tuple, String, Number.
----------------------
#MATRIX (is an array or list)
matrix = [
	[1,2,3],
	[2,4,6],
	[7,8,9]
]
matrix = [
	[[1,0],2,3],
	[2,4,6],
	[7,8,9]
]
matrix = [
	[1,0,1],
	[0,1,0],
	[1,0,1]
]
#When you want to acces to a multidiensional list
matrix = [
	[1,4,1], #index 0 (and 4 is on index 1) so [0][1]
	[0,1,0],
	[1,0,1]
]
print(matrix[0][1]) #4

-------------------------------------------
#FORMATING CODE ACCORDING TO PEP 8

#BEFORE FORMAT
def multiply_by_two(num):
	return num*2
def sum(num1, num2):
	return num1+num2
print(sum(20,3))

#AFTER FORMATING PEP 8 (>Format Document)
def multiply_by_two(num):
	return num*2


def sum(num1, num2):
	return num1+num2


print(sum(20, 3))
#code > preferences > Format > Format on Save
#pour bien arranger le code à chaque CTRL S 

----------------------------------------
#OOP (Object-Oriented Programming)

print(type(None)) #<class 'NoneType'>
print(type(True)) #<class 'bool'>
print(type(5)) #<class 'int'>
print(type(5.5)) #<class 'float'>
print(type('hi')) #<class 'str'>
print(type([])) #<class 'list'>
print(type(())) #<class 'tuple'>
print(type({})) #<class 'dict'>

#We can create our OWN DataType
#with differents Attributes and Methods
------------------------------