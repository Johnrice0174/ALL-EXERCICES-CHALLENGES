# DECORATORS (function that calls function)
# @staticmethod

# @decorate
# def add(x, y):
#    return x + y

# add = decorate(add)
# when you call add function you call decorator function with add argument

# def decorator(func):
#     def wrapper():
#         print('Hey!')
#         func()
#         print('Bye!')
#
#     return wrapper


# add = decorator(add)

# @staticmethod
# def my_method():

# my_method = staticmethod(my_method)

""" Write a decorator called play prints 'playing' before and pausing after"""

# def play(music):
#     def wrapper():
#         print('playing')
#         music()
#         print('pausing')
#
#     return wrapper
#
#
# @play  # decorator name is play
# def sing_soprano():
#     print('Envoie l\'mic à Marseille, on l\'fait à la bien!...')


# if __name__ == "__main__":
#     sing_soprano()

""" Write a decorator that prints the execution time of the function
    Use the decorator on a function that computes 2*10000
"""


# from datetime import datetime
#
#
# def timing(calc):
#     def wrapper(*args, **kwargs):  # make the master function accept all arguments
#         before = datetime.now()
#         output = calc(*args, **kwargs)
#         after = datetime.now()
#         secs = (after - before).seconds
#         micro = (after - before).microseconds
#         print(f'Execution time: {secs:.3f} seconds, {micro:.3f} microseconds')
#         return output
#
#     return wrapper
#
#
# @timing
# def compute():
#     return 2 ** 100
#
#
# def power_2(power):
#     return 2 ** power
#
#
# if __name__ == "__main__":
#     sing_soprano()
#     compute()
#     print(compute())  # None
#     print(power_2(9))  # add argument in wrap scope


# class
#     @staticmethod
#     def my_static():
#
# my_instance.my_static()
# my_static(my_instance)
#
# def method(self)


# ------------------------------
# SUPER()
class Book:
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')


class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):  # if you put author before title, the title will be Asimov
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        # self.title = title (look at super() )
        self.author = author
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print("Wow this is an awesome book!")
        else:
            self.bored = True
            print("I am very bored")


if __name__ == '__main__':
    foundation = Fiction('Foundation', 'Assimov', '1966', '5$', True)
    foundation.present()
    print(foundation.price)
    print(foundation.is_awesome)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '4000$', False)
    print(boring_book.bored)
