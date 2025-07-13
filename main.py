from stats import word_count, letter_count, get_rankings

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
    frank = get_book_text("books/frankenstein.txt")

    frank_letters = letter_count(frank)

    frank_rank = get_rankings(frank_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {word_count(frank)} total words.")

    print("--------- Character Count -------")
    print(disp_letters(frank_rank))

    print("============= END ===============")



main()