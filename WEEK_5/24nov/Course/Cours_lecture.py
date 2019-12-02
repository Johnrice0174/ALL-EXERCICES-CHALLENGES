# #There is a DIFFERENCE between CLASS and INSTANCE :

# class Book:
# 	title = "Harry Potter"
# 	n_pages = 800

# 	def change_title(self, title):
# 		title = title


# #from demo import Book
# Book #<class 'demo.Book'>

# my_book = Book()
# my_book #<demo.Book object at 0x7fd435esr4366>

# my_book.title #'Harry Potter'

# my_book.n_pages #800

# my_book.n_pages = 1000

# my_book.n_pages #1000

# second_book = Book()
# second_book.title #'Harry Potter'
# second_book.n_pages #800

# #------------
# Book().change_title #<bound method...>
# book = Book() #'Harry Potter'
# book.change_title('Harry')
# book.title #'Harry Potter' SO DIDNT CHANGE ANYTHING
# #CAUSE title in Func and in Class are DIFFERENT VARIABLES
# #One in LOCAL in the Class and the other is LOCAL in the fucntion

#--------------------
#Make like that :

# class Book:
# 	def __init__(self, title, n_pages):
# 		self.title = title
# 		if type(n_pages) == int:
# 			self.n_pages = n_pages
# 		else:
# 			raise Exception('number of pages should be an integer!')
# 		self.author = author


#    def is_nieztsche(self):
#    	return self.author == 'Friedrich Nieztsche'

#	@staticmethod #wrapper. wrap func Niez to even Func.
	#wrap = emballer / wrapper = enveloppe-emballage
#	def is_even(x):
#		return x % 2

#	@classmethod #refers to the general class, NOT to the instance
#	def is_read(cls):
#		cls.is_read = True
# u can  return cls('newtitle', 10, 'new_author')

# self method refers to the specific instance
# staticmethod doesnt depend of others attributes
# classmethod refers to the class and not the instance

# book = Book('Beyond God and Evil', 500)

# print(book) #<demo.Book object at 0x7awd3534634>
# print(book.title) #'Beyond God and Evil'
# print(book.n_pages) #500
# book.n_pages = 300
# print(book.n_pages) #300

# RAISE
# EXCEPTION

# from filename import classname

# book = Book('Beyond God and Evil', 500)
# book = Book('Beyond God and Evil', 40.5)

#   File "C:\Users\Administrateur\OneDrive\Bureau\DI_Python_Course\Week_5\Course\Cours_lecture.py", line 63, in <module>
#     book = Book('Beyond God and Evil', 40.5)
#   File "C:\Users\Administrateur\OneDrive\Bureau\DI_Python_Course\Week_5\Course\Cours_lecture.py", line 46, in __init__
#     raise Exception('number of pages')
# Exception: number of pages

# book = Book('Beyond God and Evil', 300)




# --------------------------
class Square:
	def __init__(self,x):
		self.side = x

	def __repr__(self):
		return f'<This is a square of side {self.side}'

	@classmethod
	def from_perimeter(cls, perimeter):
		return cls(x = perimeter/4)

	@staticmethod
	def perimeter(x):
		return x*4 

# from filename importe classname

print(Square) # <class 'demo.Square'>

a = Square(4)

print(a) # <filename.Square object at 0x7f32aedg35436>

print(a.side) # 4

print(Square.perimeter(20)) # 80

b = Square.from_perimeter(16)

print(b) # <filename.Square object at 0x7f0908qwe32453>

print(b.side) # 4.0

# ----
# from filename import classname

# ---------------
def add(x,y):
	return x + y

print(add(1,1))
