from stats import get_num_words, get_book_text, num_chars, sort_character_count
import sys
def main():
    filepath = 'books/frankenstein.txt'
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_counts = num_chars(book_text)
    sorted_chars = sort_character_count(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Only print alphabetical characters
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()