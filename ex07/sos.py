import sys

def is_alphanumeric_with_spaces(argument):
    return all(argument.isalnum() or argument.isspace() for charachter in argument)

def main():
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        ' ': '/'
    }
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return
    if not is_alphanumeric_with_spaces(sys.argv[1]):
        print("AssertionError: the arguments are bad")
        return
    message = sys.argv[1].upper()
    morse_message = ''.join(morse_code[char] for char in message)
    print(morse_message)

if __name__ == "__main__":
    main()

