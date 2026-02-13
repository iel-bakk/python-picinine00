import sys
from ft_filter import ft_filter

def main():
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    input_string = sys.argv[1]
    word_lenght = 0
    try :
        word_lenght = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    words = input_string.split()
    result = ft_filter(lambda x: len(x) > word_lenght, words)
    print(list(result))


if __name__ == "__main__":
    main()