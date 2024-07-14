def main():
    book_path = "/home/heinz/workspace/github.com/SirSidge/bookbot/books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    dict_letters = get_num_letters(text)
    print(dict_letters)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    dict_letters = {}
    for letter in text:
        lowered = letter.lower()
        if letter.lower() in dict_letters:
            dict_letters[lowered] += 1
        else:
            dict_letters[lowered] = 1
    return dict_letters

main()