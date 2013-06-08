import reflector
import rotors_connection
import rotor

class Enigma:
    def __init__(self, key):
        self.rotors_connection = rotors_connection.RotorsConnection(key)
        self.ROTORS_COUNT = 3
        for i in range(self.ROTORS_COUNT):
            self.rotors_connection.add_rotor(rotor.Rotor())
        self.reflector = reflector.Reflector()
    def encipher(self, char):
        result = self.rotors_connection.map(char)
        result = self.reflector.map(result)
        result = self.rotors_connection.unmap(result)
        self.rotors_connection.rotate()
        return result
    def reset_key(self, key):
        self.rotors_connection.set_rotor_states(key)
