
def shift_char(char, shift):
    char_code = ord(char)
    char_code = (char_code + shift) % 256
    return chr(char_code)

def unshift_char(char, shift):
    char_code = ord(char)
    char_code = (char_code + 256 - shift) % 256
    return chr(char_code)

class RotorsConnection:
    def __init__(self, key):
        self.rotors = []
        self.rotor_positions = []
        self.key = key
    def add_rotor(self, rotor):
        self.rotor_positions.append(ord(self.key[len(self.rotors)]))
        self.rotors.append(rotor)
    def map(self, char):
        result = char
        for i in range(len(self.rotors)):
            result = self.rotors[i].map(shift_char(result, self.rotor_positions[i]))
        return result
    def unmap(self, char):
        result = char
        for i in reversed(range(len(self.rotors))):
            result = unshift_char(self.rotors[i].unmap(result), self.rotor_positions[i]);
        return result
    def rotate(self):
        rotors_count = len(self.rotors)
        rotate_current_rotor = True
        for i in range(rotors_count):
            if rotate_current_rotor == False:
                break
            self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 256
            rotate_current_rotor = self.rotor_positions[i] == 0
    def set_rotor_states(self, key):
        self.key = key
        self.rotor_positions = [ord(key[i]) for i in range(len(self.rotor_positions))];

