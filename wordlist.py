import sys

input_letters = sys.argv[1]

f = open('wordlist.txt', 'r')

matching_words = []
for word in f:
	
	input_contains_word = True
	input_copy = list(input_letters)
	
	for char in word.strip():
		
		if char in input_copy:
			input_copy.remove(char)
		else:
			input_contains_word = False
			break
	
	if input_contains_word:
		matching_words.append(word.strip())
	
char_score = {'a': 1, 'b': 4, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 2, 'h': 3, 'i': 1, 'j': 8, 'k': 3, 'l': 1, 'm': 3, 'n': 1, 'o': 2, 'p': 3, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 1, 'y': 1, 'z': 1}

best_score = 0
best_word = ''
for word in matching_words:
	word_score = 0
	for char in word:
		word_score += char_score[char]
		
	if word_score > best_score:
		best_word = word
		best_score = word_score
		
print best_word
