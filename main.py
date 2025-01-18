def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_counter(text)
    num_chars = char_counter(text)
    book_report = report(num_words, num_chars)
    #print(num_words)
    #print(num_chars)
    print(book_report)

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

def sort_on(d):
    return d["num"]

def report(num_words, num_chars):
    sorted_list = []
    for ch in num_chars:
        sorted_list.append({"char": ch, "num": num_chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    book_report = f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in document\n\n"
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        if item["char"].isalpha():
            book_report += (f"The key is: '{item["char"]}', and the value is: {item["num"]}\n")
    book_report += "--- End report ---"
    return book_report

main()