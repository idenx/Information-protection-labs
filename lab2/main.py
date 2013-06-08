import enigma
import rotor
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: `" + sys.argv[0] + " key'")
        exit(1)
    enigma_machine = enigma.Enigma(sys.argv[1])
    result = [enigma_machine.encipher(char) for char in sys.stdin.read()]
    sys.stdout.write(''.join(result))

main()
