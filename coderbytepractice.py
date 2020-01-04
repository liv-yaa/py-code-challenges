# coderbyte practice

def LetterChanges(str):
	""" Have the function LetterChanges(str) take the str parameter being passed and modify it using 
	the following algorithm. Replace every letter in the string with the letter following it in the alphabet 
	(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and 
	finally return this modified string.Have the function LetterChanges(str) take the str parameter being 
	passed and modify it using the following algorithm. Replace every letter in the string with the letter 
	following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string
	 (a, e, i, o, u) and finally return this modified string. """
	out = ''
	for let in str:
		if ord(let) == 90:
			out += 'A'
		elif ord(let) == 122:
			out += 'a'
		elif (64 < ord(let) and ord(let) < 90) or (96 < ord(let) and ord(let) < 122) :
			out += chr(ord(let) + 1)
		else:
			out += let

	out = out.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')
	return out

def betterLetterChanges(st):
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW"
	changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWZ"
	mapping = { k:v for (k, v) in zip(st + letters, st + changes)}
	return ''.join([ mapping[c] for c in st ])


def SimpleAdding(num): 
	"""
	Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000.
	num <= 1000.
	"""
	return sum([n for n in range(1, num + 1)])

def twoSum(arr, S):
	""" find all pairs of two integers in unsorted array that add up to S 
	* Dont loop twce - O(n^ 2)
	* better - try to get O(n) time
		* Use Hash Tables / Dictionary with constant lookup time
	"""
	sums = []
	hAsh = {}

	for a in arr:
		# Check if x = S - a exists in the hash table
		if S - a in hAsh:
			sums.append((a, S - a))

		# Add a to the hash table
		hAsh[a] = a

	return sums 	



if __name__ == "__main__":
	""" if this were a module, use this format """
	print(twoSum([3, 5, 2, -4, 8, 11], 7))
























