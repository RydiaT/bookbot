def word_count(book):
    return len(book.split())

def letter_count(book):
    book = book.lower()

    out = {}

    for letter in book:
        if letter in out:
            out[letter] += 1
        else:
            out[letter] = 1

    return out

def sort_on(items):
    return items["num"]

def get_rankings(letter_count):
    out = []

    for letter in letter_count:
        count = letter_count[letter]

        out.append({"char": letter, "num": count})

    out.sort(reverse=True, key=sort_on)

    return out