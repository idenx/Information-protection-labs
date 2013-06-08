import random

class Reflector:
    def __init__(self):
        self.mappings = [i for i in range(256)]
        help_array = [i for i in reversed(range(256))]
#        random.shuffle(help_array)
        for i in range(int(256 / 2)):
            to_char = help_array[2 * i]
            from_char = help_array[2 * i + 1]
            self.mappings[to_char] = from_char
            self.mappings[from_char] = to_char

    def map(self, char):
        return chr(self.mappings[ord(char)])

