class Writer:
    num_writers = 0
    BEST_WRITER = 'Tolkien'

    def __init__(self, name, n_books):
        self.name = name
        self.n_books = n_books
        Writer.num_writers += 1

    def write(self):
        self.n_books += 1

    @staticmethod
    def be_honest():
        print(Writer.BEST_WRITER + ' is the best')


class Philosopher(Writer):
    # Philosopher is subclass, Writer is SuperClass (MasterClass)
    best = 'Nietz'

    def write_nonsense(self):
        print(f'This is complete nonsense, {self.name}')
        self.write()

    @staticmethod
    def be_honest():
        print(Philosopher.best + 'is an uberPhilosopher')


class French:

    def __init__(self,name,is_from_paris):
        self.name = name

    def talk_nonsense(self):
        print(f'I mean, you talk complete nonsense, {self.name}')


class FrenchThinker(Philosopher, French):

    def postmodern_nonsense(self):
        print(f'Yeah, whatever you say {self.name}')


if __name__ == '__main__':
    sun_tzu = Writer(name='Sun Tzu', n_books=1)
    print(sun_tzu.n_books)
    Kant = Philosopher(name='Emmanuel Kant', n_books=20)
    print(Kant.name, Kant.n_books)
    Kant.write()
    print(Kant.n_books)
    Kant.write_nonsense()
    print(Kant.n_books)
    Kant.be_honest()

    Jacques = French('Jacques',is_from_paris=True)
    Jacques.talk_nonsense()
    Derrida = FrenchThinker('Jacques Derrida',n_books=50)
    Derrida.talk_nonsense()
    Derrida.postmodern_nonsense()
    Derrida.write_nonsense()
    Derrida.write()
    print(f'{Derrida.name} wrote {Derrida.n_books} of complete nonsense')

    print(Writer.num_writers)

print(f'The best writer in the world is {Writer.BEST_WRITER}')
