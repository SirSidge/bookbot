def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    print(num_words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_counter(text):
    word_li = text.split()
    return len(word_li)

main()