from stats import get_num_words, get_count_characters, report_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_characters = get_count_characters(text)
    print(f"Found {num_words} total words")
    liste_report = report_sort(count_characters)
    for k in liste_report:
        if k["character"].isalpha():
            print(f" {k["character"]}: {k["value"]} ")
    print("============= END ===============")
    #print(count_characters)
   
main()

