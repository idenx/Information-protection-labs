import random

class Rotor:
    def __init__(self):
        self.mappings = [i for i in range(256)]
#        random.shuffle(self.mappings)
    def map(self, char):
        return chr(self.mappings[ord(char)])
    def unmap(self, char):
        return chr(self.mappings.index(ord(char)))

