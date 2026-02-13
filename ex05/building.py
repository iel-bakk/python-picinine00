import sys

def count_characters(string_to_count: str) -> None:
    text_stats = {
        "characters": len(string_to_count),
        "spaces": 0,
        "lowerCases": 0,
        "upperCases": 0,
        "digits": 0,
        "punctuation": 0
    }
    for char in string_to_count:
        if char.isspace():
            text_stats["spaces"] += 1
        elif char.islower():
            text_stats["lowerCases"] += 1
        elif char.isupper():
            text_stats["upperCases"] += 1
        elif char.isdigit():
            text_stats["digits"] += 1
        elif char in ".,;:!?\"'()[]{}":
            text_stats["punctuation"] += 1

    print(f"The text contains {text_stats['characters']} characters:")
    print(f"{text_stats['upperCases']} upper letters")
    print(f"{text_stats['lowerCases']} lower letters")
    print(f"{text_stats['punctuation']} punctuation marks")
    print(f"{text_stats['spaces']} spaces")
    print(f"{text_stats['digits']} digits")

def main():

    assert len(sys.argv) <= 2, "You can only provide one argument!"
    string_to_count = ""
    if len(sys.argv) == 2:
        string_to_count = sys.argv[1]
    elif len(sys.argv) == 1:
        lines = []
    try:
        print("What is the text to count?")
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    string_to_count = '\n'.join(lines)
    count_characters(string_to_count)

if __name__ == "__main__":
    main()