
class Philosopher:
    def __init__(self, name):
        self.name = name

    def ponder(self):
        with open('solution1.py', 'r') as f:
            for line in f.readlines():
                print(line, end='')

        print("Oh,", self.name)
        print("If I annotated this world that I am in, then what am I? The maker of the world?")


aristotle = Philosopher("Aristotle")
aristotle.ponder()

