from stats import get_word_count 
from stats import get_character_count
from stats import get_sorted_character_coutn
from stats import get_book_contents
import sys


   
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    f_cont = get_book_contents(file_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(f_cont)} total words")
    print("----------- Character Count ----------")
    sorted_char = get_sorted_character_coutn(f_cont)
    for char_dic in sorted_char:
        print(f"{char_dic['char']}: {char_dic['num']}")
    print("============= END ===============")

    
if __name__ == "__main__":
    main()