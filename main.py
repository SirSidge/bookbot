def main():
    global book_path
    book_path = "/home/heinz/workspace/github.com/SirSidge/bookbot/books/frankenstein.txt"
    text = get_text(book_path)
    global num_words
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    dict_letters = get_num_letters(text)
    #print(dict_letters)
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

#def sort_on(dict):
#    return dict["num"]


#============================================================================
#NEED TO WORK ON 'get_report'. IT'S CLEAR THE PROBLEM LIES WITH THE SORT FUNCTION. IF YOU EXECUTE 'python3 main.py' you will get all the characters
#but they're not organised either.
#Figure out how to remove everything that isn't an alphnumeric character, remove them, then organise the rest according to "num" in the dictionary.
#We might need to change the structure of li_dicts as this is should be written according to the List on boot.dev example.
#============================================================================

def get_report(dict_letters):
    li_dicts = []
    for letter in dict_letters:
        li_dicts.append({f"{letter}": dict_letters[letter]})
    #li_dicts.sort(reverse=True, key=sort_on)
    report_output = f"--- Begin report of {book_path} ---\n{num_words} words found in the document\n\n"
    for dict in li_dicts:
        for i in dict:
            report_output += f"The '{i}' character was found {dict[i]} times\n"
    report_output += "--- End report ---"
    print(report_output)



main()