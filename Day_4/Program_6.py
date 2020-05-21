def character(word): 
	dict = {} 
	for i in word: 
		dict[i] = dict.get(i, 0) + 1
	return dict


def possible_words(lwords, charSet): 
	for word in lwords: 
		p = 1
		chars = character(word) 
		for key in chars: 
			if key not in charSet: 
				p = 0
			else: 
				if charSet.count(key) != chars[key]: 
					p = 0
		if p == 1: 
			print(word) 

if __name__ == "__main__": 
	input = ['how', 'cat', 'he', 'eat', 'row', 'cow', 'run'] 
	charSet = ['e', 'o', 'c', 'a', 'h', 'r', 'w'] 
	possible_words(input, charSet) 