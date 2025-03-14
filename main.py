import sys

from stats import count_words
from stats import count_letters_and_group

def get_book_text(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents

def print_data(path, words, letters):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	for l in letters:
		if l.isalpha():
			print(f"{l}: {letters[l]}") 
	print("============= END ===============")
	return ""

def main():
#	location="./books/frankenstein.txt"
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)	

	book_data=get_book_text(sys.argv[1])
	num_words=count_words(book_data)
	letter_counts=count_letters_and_group(book_data)
	sorted_items = dict(sorted(letter_counts.items(), key=lambda kv: (-kv[1], kv[0])))
	print_data(sys.argv[1],num_words, sorted_items)

main()
