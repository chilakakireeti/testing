# main.py

from string_utils import StringOperations


def get_input():
    user_input = input("Enter a string: ")
    return user_input


def main():

    text = get_input()

    string_obj = StringOperations(text)

    reversed_text = string_obj.reverse_string()

    
    print("Reversed String:", reversed_text)


if __name__ == "__main__":
    main()