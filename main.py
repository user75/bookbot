import sys
from stats import get_num_words, get_count_characters, report_sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    text = get_book_text(path)
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

