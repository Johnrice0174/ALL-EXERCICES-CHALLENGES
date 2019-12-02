# class Dog:
#     def __init__(self, name_dog, height_dog):
#         self.name_dog = name_dog
#         self.height_dog = height_dog
#
#     def talk(self):
#         print('Wouaf')
#
#     def jump(self):
#         self.height_dog = self.height_dog * 2
#         return f'<The dog height while jumping is {self.height_dog}'
#
#
# if __name__ == "__main__":
#     dog = Dog('Brave', 20)
#     print(dog.jump())
#
# Davids_dog = {
#     'name': 'Rex',
#     'height': 50
# }
#
# print(f'Davids Dog details are {Davids_dog}')
#
# Sarahs_dog = {
#     'name': 'Teacup',
#     'height': 20
# }
# print(f'Sarahs Dog details are {Sarahs_dog}')

# def winner(self):

# EXERCICE 2

class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if len(self.animals) == 0:  # verifier si list vide (car la loop se lance pas quand cest vide)
            self.animals.append(new_animal)
        else:
            for i in self.animals:
                if new_animal in self.animals:
                    print('This animal was already added to the zoo')
                else:
                    self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self):


French_zoo = Zoo('Zavatar')

French_zoo.add_animal('Tiger')

French_zoo.add_animal('Lion')

French_zoo.get_animals()