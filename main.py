from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    output = get_book_text(sys.argv[1])

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")

    num_words = count_words(output)
    print(f"\nFound {num_words} total words")

    print("\n--------- Character Count -------")
    count = count_characters(output)
    sorted = sort_dict(count)
    for item in sorted:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
