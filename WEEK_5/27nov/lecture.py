# class Parent:
#     def scold(self):
#         print('Go to your room you\'re are punished!!')
#
# class Child:
#     def cry(self):
#         print(scold)
#         print("I'm cryiiiiing!")

# ------------------------
@staticmethod
def instance_check(func):
    def wrapper(self, obj):
        if isinstance(obj, self.__class__):
            output = func(self,obj)
            return output
        else:
            raise TypeError(f'Operation not supported between Philosophy and {type(other)}')

    return wrapper

class Philosophy:

    def __init__(self,general_name,idea_list=[]):
        self.name = general_name
        if isinstance(idea_list,list):
            self.ideas = idea_list
        else:
            raise TypeError('idea_list should be a list')

    def __repr__(self):
        return f'<Philosophy Object: {self.name}>'

    def __str__(self):
        paragraph = ''
        for idea in self.ideas:
            paragraph += f'{self.name} states: {idea}\n'
        return paragraph

    def __len__(self):
        return len(self.ideas)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        else:
            res = self.ideas[self.index]
            self.index += 1
            return res

    @instance_check
    def __add__(self, other):g
            add_name = ' + '.join([self.name, other.name])
            return self.__class__(add_name,self.ideas + other.ideas) #self.__class__ = Philosophy

@instance_check
    def __sub__(self, other):
        sub_name = ' - '.join([self.name, other.name])
        return self.__class__(sub_name,[idea for idea in self.ideas if idea not in other.ideas])

    # def __long__(self):
    #     return len(self.ideas)


if __name__ == '__main__':
    general_name = 'Existentialism'
    idea_list = ['Life sucks','Existence preceeds essence','Jean Paul Startre is awesome']
    s_name = 'Structuralism'
    s_list = ['Everything is kindof network stuff', 'Life sucks']
    structuralism = Philosophy(s_list)
    existe = Philosophy(general_name,idea_list)
    print(existe.__repr__())
    print(existe)
    print(len(existe))

    for item in existe:
        print(item)

    print(existe + structuralism)
    print (existe - structuralism)
    #print (existe + 10) #it will crash like we want