from stats import get_book_text, word_count, character_count, character_sort
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
file = sys.argv[1]
book = get_book_text(file)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {file}...")
print("----------- Word Count ----------")
print(f"Found {word_count(book)} total words")
print("--------- Character Count -------")
count = character_count(book)
sorted_count = character_sort(count)

for i in sorted_count:
    print(f"{i["char"]}: {i["num"]}")

