def main():
    global book_path
    book_path = "/home/heinz/workspace/github.com/SirSidge/bookbot/books/frankenstein.txt"
    text = get_text(book_path)
    global num_words
    num_words = get_num_words(text)
    global my_alphabet
    my_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict_letters = get_num_letters(text)
    get_report(dict_letters)

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

def sort_on(dict):
    return dict["num"]

def get_report(dict_letters):
    li_dicts = []
    for letter in dict_letters:
        if letter in my_alphabet:
            li_dicts.append({"letter": f"{letter}", "num": dict_letters[letter]})
    li_dicts.sort(reverse=True, key=sort_on)
    
    report_output = f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n"
    for dict in li_dicts:
        temp_letter = dict["letter"]
        temp_num = dict["num"]
        report_output += f"The '{temp_letter}' character was found {temp_num} times\n"
    report_output += "--- End report ---"
    print(report_output)

main()