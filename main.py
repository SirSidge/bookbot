def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    num_chars = char_counter(text)
    #print(num_words)
    print(num_chars)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_counter(text):
    word_li = text.split()
    return len(word_li)

def char_counter(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()