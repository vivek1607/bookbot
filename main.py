def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    count_words(text)
    num_chars = count_character(text)
    print(num_chars)
    freq_arr = char_freq(num_chars)
    for item in freq_arr:
        if not item["char"].isalpha():
            continue
        else:
            print(f"The '{item['char']}' character was found {item['num']} times")

# count words
def count_words(text):
    return len(text.split())
# get book text
def get_book_text(path):
    book_path = 'books/frankenstein.txt'
    with open(path) as f:
        return f.read()
# get number of character
def count_character(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars
def char_freq(arr):
    sorted_arr = []
    for ch in arr:
        sorted_arr.append({'char': ch, 'num': arr[ch]})
    sorted_arr.sort(reverse=True, key=sort_on)
    return sorted_arr
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]
main()
