def count_words(data):
        words=data.split()
        return len(words)

def count_letters_and_group(data):
	letters = {}
	for i in data:
		lc = i.lower()
		if lc in letters:
			tmp = letters[lc] + 1
			letters[lc] = tmp
		else:
			letters[lc] = 1
	return letters 
