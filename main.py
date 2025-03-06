from stats import get_num_words, get_book_text, num_chars, sort_character_count
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filepath>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read the file '{filepath}'.")
        sys.exit(1)
    word_count = get_num_words(book_text)
    char_counts = num_chars(book_text)
    sorted_chars = sort_character_count(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    sorted_chars = sorted(sorted_chars, key=lambda x: x["char"])
if __name__ == "__main__":
    main()