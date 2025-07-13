import sys

from stats import word_count, letter_count, get_rankings
from sys import argv

def get_book_text(file):
    with open(file) as f:
        return f.read()

def disp_letters(raw_ranks):
    out = ""

    for char in raw_ranks:
        if char["char"].isalpha():
            out += f"{char["char"]}: {char["num"]}\n"

    return out

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    raw_book = get_book_text(argv[1])

    book_letters = letter_count(raw_book)

    letter_rank = get_rankings(book_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count(raw_book)} total words.")

    print("--------- Character Count -------")
    print(disp_letters(letter_rank))

    print("============= END ===============")



main()