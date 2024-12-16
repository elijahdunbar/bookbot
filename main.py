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
    print(f"{word_count} words found in the document\n")
    sorted_chars = sort_dict(char_dict)
    for char_dict in sorted_chars:
        if char_dict["name"].isalpha():
            print(f"The '{char_dict["name"]}' character was found {char_dict["num"]} times")
    print("--- End report ---")


def sort_dict(dictionary):
    dict_list = dict_to_list(dictionary)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dictionary):
    return dictionary["num"]


def dict_to_list(dictionary):
    dict_list = []
    for key in dictionary:
        dict_list.append({"name" : key, "num" : dictionary[key]})
    return dict_list


main()
