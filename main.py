def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_characters = get_count_characters(text)
    liste_report = report_sort(count_characters) 
    # print(f"{num_words} words found in the document")
    #print(count_characters)
    print(liste_report)
def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    characters_dict = {}
    for i in text:
        i = i.lower()
        if i in characters_dict:
            characters_dict[i] += 1
        else: 
            characters_dict[i] = 1
    return characters_dict
        
def report_sort(characters_dict):
    liste =[]
    for k,v in characters_dict.items():
        if k.isalpha():
            liste.append({"character": k , "value" : v})
            print(f"The character {k} was found {v} times")
    liste = sorted(liste, key = lambda x : x["value"], reverse=True )
    

main()

