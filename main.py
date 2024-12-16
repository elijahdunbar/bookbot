def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    print_report(book_path, word_count, char_count)

    
def get_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    lowercase_text = text.lower()
    char_dict = {}
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def print_report(path, word_count, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for char in char_dict:
        if char == "\n":
            print(f"The '\\n' character was found {char_dict[char]} times")
        else:
            print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")


def sort_dict(dictionary):
    pass


def dict_to_list(dictionary):
    dict_list = []
    for key in dictionary:
        dict_list.append({"name" : key, "num" : dictionary[key]})
    return dict_list


main()
