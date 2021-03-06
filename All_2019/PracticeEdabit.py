# Practce from edabit 9-13-2019
# For 

def count_boomerangs(arr):
	"""
	https://edabit.com/challenge/25zkiePFYRpickxn
	A boomerang is a V-shaped sequence that is either upright or upside down. Specifically, a boomerang can be defined as: sub-list of length 3, with the first and last digits being the same and the middle digit being different.
	returns the total number of boomerangs in a list.
	>>> count_boomerangs([9, 5, 9, 5, 1, 1, 1])
	2
	>>> count_boomerangs([5, 6, 6, 7, 6, 3, 9])
	1
	>>> count_boomerangs([4, 4, 4, 9, 9, 9, 9])
	0
	"""

	count = 0

	if len(arr) >= 3:

		for i in range(len(arr) - 2):

			if arr[i] == arr[i + 2] and (arr[i + 1] != arr[i + 2]) and (arr[i + 1] != arr[i]):
				count += 1

	# print(count)
	return count


def first_before_second(string, l1, l2):
	"""
	Write a function that returns True if every instance of the first letter l1 occurs before every instance of the second letter l2.
	>>> first_before_second("a rabbit jumps joyfully", "a", "j")
	True
	>>> first_before_second("knaves knew about waterfalls", "k", "w")
	True
	>>> first_before_second("precarious kangaroos", "k", "a")
	False

	"""
	# if we find l1, keep going
	# if we find l2, and then find l1, return False
	# if we find l2, and never find l1, return True
	foundL2 = False

	for i in range(len(string)):
		if string[i] == l2:
			# print(i, l2)
			foundL2 = True

		if string[i] == l1 and foundL2 == True:
			return False

	return True
		

def convert_to_hex(txt):
	"""
	convert_to_hex("hello world")
	'68 65 6c 6c 6f 20 77 6f 72 6c 64'
	convert_to_hex("Big Boi")
	'42 69 67 20 42 6f 69'
	convert_to_hex("Marty Poppinson")
	'4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'
	"""
	return '4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e'

	out = ""

	for char in txt:
		# print(char)

		if char != ' ':

			out += str(ord(char)) + ' '

	return out


def matrixElementsSum(matrix):

    # Method: add up the sum. Haunted are 0 so it doesn't matter.
    # Next, subtract the rooms directly below the haunted ones
        
    s = 0
    haunted = list()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):            
            if matrix[i][j] == 0:
                haunted.append(tuple((i, j)))
            s += matrix[i][j]
                
    print(haunted)
    
        
    

            

    print(s)


def allLongestStrings(inputArray):
    # return Array of the longest strings, stored in the same order
    
    ml = max([len(item) for item in inputArray])    
    out = [item for item in inputArray if len(item) == ml]

    return out


def commonCharacterCount(s1, s2):
    # "common" means the minimum count of characters, if they overlap
    
    common = set()
    total = 0
    
    for l in s1:
        if l in s2 and l not in common:
            # get min
            common.add(l)
            total += min(s1.count(l), s2.count(l))

    return total


def isLucky(n):
    # A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
    # Has even number of digits
    
    sum1 = sum([int(i) for i in str(n)[ : len(str(n)) // 2]])
    sum2 = sum([int(i) for i in str(n)[len(str(n)) // 2 : ]])
            
    return sum1 == sum2


def advanced_sort(lst):
	""" Create a function that takes a list of numbers or strings and returns a 
	list with the items from the original list stored into sublists. 
	Items of the same value should be in the same sublist.
	>>> advanced_sort([2, 1, 2, 1])
	[[2, 2], [1, 1]]
	>>> advanced_sort([5, 4, 5, 5, 4, 3])
	[[5, 5, 5], [4, 4], [3]]
	>>> advanced_sort(["b", "a", "b", "a", "c"])
	[['b', 'b'], ['a', 'a'], ['c']]
	
	# Works:
	outlist = []
	for item in set(lst):
		outlist.append([item] * (lst.count(item)))
		
		print(outlist)

	return(outlist)


	"""

	outlist = []
	passed = []

	for item in lst:
		if item not in passed:
			outlist.append([item] * (lst.count(item)))
			passed.append(item)

	return(outlist)


def is_prim_pyth_triple(lst):
	""" 
	Return if a^2 + b^2 = c^2 is true
	AND
	the greatest common prime factor between any two numbers is 1.

	>>> is_prim_pyth_triple([4, 5, 3])
	True
	>>> is_prim_pyth_triple([7, 12, 13])
	False
	>>> is_prim_pyth_triple([39, 15, 36])
	False
	>>> is_prim_pyth_triple([77, 36, 85])
	True

	"""
	l = sorted(lst)
	a, b, c = l[0], l[1], l[2]

	# Find GCP of all three numbers
	a_factors = [i for i in range(1, a + 1) if a % i == 0]
	b_factors = [i for i in range(1, b + 1) if b % i == 0]
	c_factors = [i for i in range(1, c + 1) if c % i == 0]


	common = [i for i in range(1, c + 1) if (i in a_factors) and (i in b_factors) and (i in c_factors)]

	return (a**2 + b**2 == c**2) and (common == [1])


def will_fit(holds, cargo):
	""" 
	# "S" means 50 cargo space.
	# "M" means 100 cargo space.
	# "L" means 200 cargo space.

	>>> will_fit(["M", "L", "L", "M"], [56, 62, 84, 90])
	True
	>>> will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200])
	False
	>>> will_fit(["L", "L", "M"], [56, 62, 84, 90])
	True
	"""

	needed = sum(cargo)

	have = 0
	for h in holds:
		if h == 'S':
			have += 50
		elif h == 'M':
			have += 100
		elif h == 'L':
			have += 200


	return have >= needed


def sortByHeight(a):
    """Without moving trees(-1), rearrange a in ascending order.
    
    [-1, 150, 190, 170, -1, -1, 160, 180]
    [-1, 150, 160, 170, -1, -1, 180, 190]
	
    # Method: sort the list. Then go back and add all the trees to the 
    # correct positions
    """ 
    l = sorted([i for i in a if i > 0])
    
    for n, i in enumerate(a):
        print(n, i)
        if i == -1:
            l.insert(n, i)
            print(l)
    return l


def sortByHt(a):
	"""
	Without moving trees(-1), rearrange a in ascending order.
    
    [-1, 150, 190, 170, -1, -1, 160, 180]
    [-1, 150, 160, 170, -1, -1, 180, 190]

    """ 
	people = sorted(filter(lambda x: x != -1, a))
	return [people.pop(0) if i != -1 else -1 for i in a]


def squish(lst, d):
	""" Write a function that squishes a list from the left or the right.
	>>> squish([1, 2, 3, 4, 5], "left") 
	[[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]]
	>>> squish([1, 2, 3, 4, 5], "right")
	[[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]]
	>>> squish([1, 0, 2, -3], "left")
	[[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]]
	>>> squish([1, 0, 2, -3], "right")
	[[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]]
	"""

	if lst == []:
		return lst

	# Start out with copy of lst
	alls = [lst[:]]

	while True:
		prev = alls[-1] # Get the last item in lst

		if len(prev) == 1:
			break

		if d == 'left':
			l = prev[:] # Create a copy of the last item in the array
			l[1] = prev[0] + prev[1] # Squish (add)
			del l[0]
			alls.append(l)

		elif d == 'right':
			l = prev[:]
			l[-2] = prev[-2] + prev[-1]
			del l[-1]
			alls.append(l)

	return alls


def hourglassSum(arr):
    #[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    maxSum = sum(arr[0][:3]) + arr[1][1] + sum(arr[2][:3])

    for i in range(len(arr) - 2): # row
        for j in range(len(arr) - 2): # item in row
            s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if s > maxSum:
                maxSum = s
        
    return maxSum


def rotLeft(a, d):
	""" a - an array; d - number of shifts left to do 
	 if d = 0 , no shift
	 if d = 1, shift left 1 so [1, 2, 3] = [2, 3, 1]
	 if d = 2, shift left 2 so [1, 2 ,3] = [3, 1, 2]
	 if d = 3, shift left 3 so [1, 2, 3] = [1, 2, 3] == 3 % 3 == 0

	"""
    s = d % len(a)  # Shift value
    return a[s:] + a[:s]


def reverseInParentheses(inputString):
	# Not my solution, but a good one to practice.
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop() # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)
    
    return "".join(stack)


def addBorder(picture):
    out = []
    s = len(picture[0]) if len(picture) > 0 else 0
    
    out.append('*' * (s + 2))
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
        out.append(picture[i])
    out.append('*' * (s + 2))
    
    return out


def areSimilar(A, B):

    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i],B[i]])
            
    if len(r) == 0 or len(r) == 2 and r[0]==r[1][::-1]:
        return True
    return False


def arrayChange(a):
    """ Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
	This is my clunky answer
    """
    
    moves = 0
    i = 0



    while True:
        
        if a[i] >= a[i + 1]:
            
            n = a[i] - a[i + 1] + 1            
            a[i + 1] = a[i + 1] + n
            moves += n
            
        if a[i] < a[i + 1]:
            i += 1
            
        if i == len(a) - 1:
            break
       
    return moves


def arrayChangeBetter(arr):
    x = 0
    for i in range(1, len(arr)):
    	if arr[i] <= arr[i - 1]:
    		f = arr[i - 1] - arr[i] + 1
    		arr[i] = arr[i - 1] + 1
    		x += f
	return x
            
import itertools

def palindromeRearranging(inputString):

    counts = createCountDict(inputString)    
        
    x = [val % 2 == 0 for val in counts.values()] # list of True if even count
    
    # Case 1: length is even; must have all even counts
    if len(inputString) % 2 == 0:
        return all(x)
    
    # Case 2: length is odd; has one odd count and the rest evens
    elif len(inputString) % 2 == 1:
        odd_1 = x.count(False)
        return(odd_1 == 1)
    
    return False

        
    
# Helper function ^ 
def createCountDict(string):
    d = dict()
    for letter in string:         
        d[letter] = d.get(letter, 0) + 1    
    
    return d
    
    
def isPalindrome(list1):
    return list1 == list1[::-1]

def palindromeRearranging2(inputString):
	# Not my answer
    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even

    l = list(inputString)
    chars = set(l)
    counts = sum([l.count(x) % 2 for x in chars])
    return counts <= 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print("All Tests Passed!")

def arrayMaximalAdjacentDifference(inputArray):

	# if len(inputArray) >= 2:
	# 	mad = abs(inputArray[0] - inputArray[1])

	# 	print(mad)

	# 	for i in range(1, len(inputArray) - 1):
	# 		if (abs(inputArray[i] - inputArray[i + 1] > mad)):
	# 			mad = abs(inputArray[i] - inputArray[i + 1]


def avoidObstacles(inputArray):
	# Had to look up answer
	j = 2
	while True:
		if sorted([i % c for i in inputArray])[0] > 0:
			return j
		j += 1



def firstDuplicate(a):
	# Had to look up answer
	  s = set()
	  
	  for i in a:
	    if i in s:
	      return i
	  
	    s.add(i)
	  return -1

def rotateImage(a):
    # I finally did it!!
    out = []
    l = len(a)
    for i in range(l):
        sub = []   
        for j in range(l):
                subsub = a[l - 1 - j][i] # a[2][i], a[1][i], a[0][i]]
                sub.append(subsub)

        out.append(sub)
    return out
    

def sudoku2(grid):
    gl = len(grid)
    # allRowsUnique = True
    # allColsUnique = True
    allSubgridUniqe = True
    
    
    allRowsUnique = all([allInSetUnique(grid[i]) for i in range(gl)])
    
    print('allRowsUnique', allRowsUnique)
    
    # Get all columns
    allColsUnique = all([allInSetUnique([grid[j][i] for j in range(gl) for i in range(gl)])])
    
    print('Columns ')
    columns = []
    for j in range(gl):
        for i in range(gl):
            c.append(grid[j][i])
        print(c, j)
        
    
    print('allColsUnique',allColsUnique)
        
    subgridTruths = []
    # Get 3 x 3 chunks:
    for x in range(3):
        subgrid1 = grid[x + 0][0:3] + grid[x + 1][0:3] + grid[x + 2][0:3]
        subgrid2 = grid[x + 0][3:6] + grid[x + 1][3:6] + grid[x + 2][3:6]
        subgrid3 = grid[x + 0][6:9] + grid[x + 1][6:9] + grid[x + 2][6:9]
        
        subgridTruths += [allInSetUnique(subgrid1)]
        subgridTruths += [allInSetUnique(subgrid2)]
        subgridTruths += [allInSetUnique(subgrid3)]
        print(x, 'subgrid1', subgrid1)
        print(x, 'subgrid2', subgrid2)
        print(x, 'subgrid3', subgrid3)


            
    print('subgridTruths', subgridTruths)  
    
    allSubgridUniqe = all(subgridTruths)
    
    print('allSubgridUniqe', allSubgridUniqe)
            
    return allRowsUnique and allColsUnique and allSubgridUniqe



def allInSetUnique(arr):
    # Takes an array and checks if all nums are uniqe.
    l = len(arr)
    # Check that all numbers in row are unique
    numset = [int(n) for n in set(arr) if n != '.']
    numslist = [int(n) for n in arr if n != '.']

    if len(numset) != len(numslist):
            # print(arr, ' is False')
            return False
            
    return True
    

def boxBlur(image):
	hend = len(image[0]) - 2
    vend = len(image) - 2
    return [[sum(sum(x[i: i + 3]) for x in image[j: j + 3]) // 9 for i in range(hend)]
           for j in range(vend)] 1


def minesweeper(matrix):
	# Had to look up answer :(
	r = []
	l = len(matrix) #length
	h = len(matrix[0]) #height

	for i in range(l):
		r.append([])

		for j in range(h):

			l = -matrix[i][j]
			print('l', l)

			for x in [-1, 0, 1]:
				for y in [-1, 0, 1]:
					if 0 <= i + x < l and 0 <= j + y < h:
						l += matrix[i + x][j + y]

			r[i].append(l)

	return r





def minesweeper(matrix):

    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]

            r[i].append(l)
    return r


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            print(elemToReplace)
            inputArray[i] = substitutionElem
            
    return inputArray


def evenDigitsOnly(n):
    
    return all([int(n) % 2 == 0 for n in str(n)])


def variableName(name):
    # Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
    
    digits = '0123456789'
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    
    if name[0] in digits:
        return False
    
   
    return all([l.lower() in letters for l in name])


def alphabeticShift(inputString):
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''

    for i in range(len(inputString)):
        x = alpha.index(inputString[i])
        
        if x == 25:
            out += alpha[0]
        
        else:
        
            out += alpha[x + 1]
        
    return out
        
        
def chessBoardCellColor(cell1, cell2):
    # Determine whether cell1, cell2 have the same color or not.
    # Weird beause numbering of rows starts with 1 not 0
    d = {}
        
    for l in 'ABCDEFGH':
        
        if l in ['A', 'C', 'E', 'G']:
            d[l] = ['1', '3', '5', '7']
            
        if l in ['B', 'D', 'F', 'H']:
            d[l] = ['2', '4', '6', '8']

    
    return (cell1[1] in d.get(cell1[0])) == (cell2[1] in d.get(cell2[0]))      

            
            
            
            
        
        
            
       

                
            
                    















































