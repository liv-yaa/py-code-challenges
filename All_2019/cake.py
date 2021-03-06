"""
Interview Cake - probs

"""

import os
import hashlib # Used in dup files prob
import random

def binary_search(target, nums):
    """See if target appears in nums, Recursively

    Runtime is 

    https://www.interviewcake.com/question/python3/two-egg-problem

    >>> binary_search(10, [1, 2, 3, 4, 10, 5, 6, 7, 8, 9])
    True
    >>> binary_search(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    False



    """
    # Choose "walls" around the position of target
    
    floor_ix = -1 # -1 is to the left of the 0th index
    ceil_ix = len(nums) # Last index

    # If there is nothing between floor and ceil, the number must not be present
    while floor_ix + 1 < ceil_ix:

        # Find the index ~ halfway between flor and ceil
        distance = ceil_ix - floor_ix
        half_dist = distance // 2
        guess_ix = floor_ix + half_dist

        guess = nums[guess_ix]

        if guess == target:
            return True

        if guess > target:
            # Target is to the left, so move ceil to left
            ceil_ix = guess_ix

        else:
            # Target is to the right, so move floor to right
            floor_ix = guess_ix


    return False


def merge_sort(list_to_sort):
    """
    https://www.interviewcake.com/article/python/logarithms?course=fc1&section=algorithmic-thinking
    """
    # Base case: lists with fewer than 2 elements are sorted
    if len(list_to_sort) < 2:
        return list_to_sort

    # Step 1: divide the list in half
    # We use integer division, so we'll never get a "half index"
    mid_index = len(list_to_sort) / 2
    left  = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    # Step 2: sort each half
    sorted_left  = merge_sort(left)
    sorted_right = merge_sort(right)

    # Step 3: merge the sorted halves
    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    # sortedLeft's first element comes next
    # if it's less than sortedRight's first
    # element or if sortedRight is exhausted
    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and
                (current_index_right == len(right) or
                 sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1
    return sorted_list


def merge_ranges(meetings):
    """
    A feature to see the times in a day when everyone is available.
    In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
    These integers represent the number of 30-minute blocks past 9:00am.
    https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation    
    
    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    """

    # Merge meeting ranges
    # Want to do O(n) - What if we sorted our list of meetings by start time?

    sort_meetings = sorted(meetings)
    
    # Create a list with the first tuple
    merged_meetings = [sort_meetings[0]]
    
    # For the rest of the tuples,
    for curr_start, curr_end in sort_meetings[1:]:
        last_merged_start, last_merged_end = merged_meetings[-1]
        
        # Either replace that item with the max end time, or
        if (curr_start <= last_merged_end):
            merged_meetings[-1] = (last_merged_start, max(last_merged_end, curr_end))
            
        # Add tuple to list
        else:
            merged_meetings.append((curr_start, curr_end))
    
    return merged_meetings


def reverse_list(lst):
    """
    Write a function that takes a list of characters and reverses the letters in place. ↴

    (note lists are mutable but strings are not)

    >>> reverse_list(['a', 'b', 'c'])
    ['c', 'b', 'a']
    >>> reverse_list(['a', 'b'])
    ['b', 'a']
    >>> reverse_list([])
    []
    >>> reverse_list(['c'])
    ['c']

    """

    left = 0
    right = len(lst) - 1

    while left < right:

        # Swap, move toward middle:

        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    

    return lst



def reverse_words(message):
    """
    Takes a message as a list of characters and reverses the order of the words in place
    * Space separated

    # Need to debug!!
    
    # >>> reverse_words(['a', ' ', 'c', 'a', 't'])
    # ['c', 'a', 't', ' ', 'a']

    # >>> reverse_words(['c', 'a', 't'])
    # ['c', 'a', 't']

    # >>> reverse_words([])
    # []

    """
    # Use above fxn
    reverse_characters(message, 0, len(message)-1)

    # Un-scramble each word
    # current word start index
    index = 0

    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_characters(message, index, i - 1)

            index += 1


def merge_lists(l1, l2):
    """
    Not done!
    We have our lists of orders sorted numerically already, in lists. 
    Write a function to merge our lists of orders into one sorted list.

    # >>> merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
    # [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

    """

    out = [None] * (len(l1) + len(l2))

    print(l1, len(l1))
    print(l2, len(l2))
    print(out, len(out))


    i = 0
    idx1 = 0
    idx2 = 0

    while i < len(out):
        print(i)
        curr1 = l1[idx1]
        curr2 = l2[idx2]
        print(curr1, curr2)

        if i < len(out):

            if curr1 < curr2:

                out[i] = curr1
                print("Out", out)
                i += 1
                idx1 += 1

            else:

                out[i] = curr2
                print("Out", out)
                i += 1
                idx2 += 1       

    print(out)
    return out


def is_riffle(half1, half2, deck):
    """
    Write a RECURSIVE function that takes a deck and checks if it has been shuffled in a "riffle" way

    ## If deck is a "riffle" of half1 and half2, the first card from deck
    ## should be either the same as the first card from half1 or the same as the 
    ## first card from half 2.

    ## Go through the deck, matching and throwing out as you match
    ## If we get to the end, return True

    Note this version is bad! Better version keeps track of indexes...


    """
    if len(deck) == 0:
        return True # Base case

    # If it exists, is the top of deck the same as the the top of half1?
    if len(half1) and half1[0] == deck[0]:
        # Take the tops off both and recurse
        return is_riffle(half[1:], half2[1:], deck[1:])

    # If it doesn't match, we know it's not:
    else:
        return False


def is_riffle_iter(half1, half2, deck, deck_ix=0, half1_ix=0, half2_ix=0):
    """
    Write a Better iterative RECURSIVE function that takes a deck and 
    checks if it has been shuffled in a "riffle" way

    Note this has better time complexity than the previous recursive version! 
    Instead of slicing the list, it just keeps track of indexes.

    """
    # base case is still the same, we have hit the end
    if deck_ix == len(deck):
        return True

    # If we still have cards in half1 and the top card is the same
    # as the top card in deck,
    if half1_ix < len(half1) and half1[half1_ix] == deck[deck_ix]:
        half1_ix += 1


    # If we still have cards in half2 and the top card is the same
    # as the top card in deck,
    elif half2_ix < len(half2) and half2[half2_ix] == deck[deck_ix]:
        half2_ix += 1

    # If either half is depleted OR there are not matches,
    else:
        return False

    #Move on to the next card:
    deck_ix += 1

    return is_riffle_iter(half1, half2, deck, deck_ix, half1_ix, half2_ix)


def is_riffle_best(half1, half2, deck):
    half1_ix = 0
    half2_ix = 0
    half1_max_ix = len(half1) - 1
    half2_max_ix = len(half2) - 1

    for card in deck:
        # If we still have cards in half1 and the "top" card in half1 is the same,
        if half1_ix <= half1_max_ix and card == half1[half1_ix]:
            half1_ix += 1

        # If we still have cards in half1 and the "top" card in half1 is the same,
        elif half2_ix <= half2_max_ix and card == half2[half2_ix]:
            half2_ix += 1

        else:
            return False

    # If all cards in shuffled deck have been accounted for, this is a riffle!
    return True


def time_equal(flight_length, movie_lengths):
    """Write a function that takes an integer flight_length (in minutes) and a
    list of integers movie_lengths (in minutes) and returns a
    boolean indicating whether there are two numbers in movie_lengths whose
    sum equals flight_length.

    >>> time_equal(0, [3, 3, 4])
    False
    >>> time_equal(10, [3, 7, 4])
    True
    >>> time_equal(100, [30, 70])
    True
    >>> time_equal(100, [])
    False

    Time is O(n) 

    Are you sure your function won’t give a false positive if the 
    list has one element that is half flight_length? 
    >> Solution : Pop the item once you get it

    """

    while len(movie_lengths) > 1:

        # Get the first item of movie_lengths:
        m1 = movie_lengths[0]

        # Create a set with the remaining elements:
        others = set(movie_lengths[1:]) # Oo this slice is bad, takes O(n)?

        # Get the value we are looking for:
        delta = flight_length - m1
        
        return delta in others # This takes O(n)

    return False


def perm_palin(string):
    """
    Write an efficient function that checks whether 
    any permutation ↴ of an input string is a palindrome. ↴

    >>> perm_palin("civic")
    True
    >>> perm_palin("ivicc")
    True
    >>> perm_palin("civil")
    False
    >>> perm_palin("livci")
    False

    HINT:
    - Check that each character left of the middle has a corresponding 
    copy right of the middle
    - Then check each character appears an even number of times
    - ONE char appears an odd number of times!
    - Data structure to use: DICTIONARY (with the char : boolean )

    # Overall time is O(n) + O(n) so still linear

    """

    # Create dict for characts:bools
    dic = {}

    # Iterate and add to dict: O(n)
    for char in string:
        parity = True # Stand in for Even Parity

        if string.count(char) % 2 == 1:
            parity = False # Stand in for Odd Parity

        dic[char] = parity


    # see if count of odd parity != 1 or 0 ... O(m)
    odd_count = [v for v in dic.values()].count(False)
    return odd_count == 1 or odd_count == 0


def has_pal_perm(string):
    # Their implementation. Faster?
    unpaired = {} # All unpaired characters

    for char in string:

        if char in unpaired:
            unpaired.remove(char)

        else:
            unpaired.add(char)

    return len(unpaired) <= 1


def word_cloud(string):
    """
    Build a word cloud, an infographic where the size of a word corresponds 
    to how often it appears in the body of text.
    Return a word count dictionary.
    
    >>> word_cloud("cloudy cloudy day")
    {'cloudy': 2, 'day': 1}

    >>> word_cloud("cloudy cloudy day day day")
    {'cloudy': 2, 'day': 3}

    >>> word_cloud("Cloudy cloudy Day day day")
    {'cloudy': 2, 'day': 3}

    >>> word_cloud("")
    {}

    """ 
    counts = {}
    listo = [s.lower() for s in string.split(" ")]

    # Create word counter for lowercase list:

    if len(listo) > 1:

        for item in listo:

            counts[item] = counts.get(item, 0) + 1


    return counts


def sort_scores(scores, highest):
    """
    Write a function that takes:
    - scores; a list of unsorted scores
    - highest: the highest_possible_score in the game
    and returns a sorted list of scores in less than O(nlgn) time.
    (where n = len(scores))

    # >>> sort_scores([37, 89, 41, 65, 91, 53], 100)
    # [91, 89, 65, 53, 41, 37]

    """

    dic = {}

    if len(scores) > 1:

        for s in scores:

            dic[s] = dic.get(s, 0) + 1

            # add the score to a new list sorted_scores as many times as count of appearances.
    sort = []

    sorted_keys = sorted(dic.keys) 
    for key in range(len(sorted_keys), -1, -1):

        for n in dic[key]: 
            sort[0] = key * dic[key]

    # print("sorted_scores", sorted_scores)

    return sort


def rem_duplicate_files(directory):
    """
    Not hte final solution
    Write a function that returns a list of all the duplicate files. 
    We'll check them by hand before actually deleting them, since 
    programmatically deleting files is really scary. To help us confirm that 
    two files are actually duplicates, return a list of tuples ↴ where:

        the first item is the duplicate file
        the second item is the original file

    3 data struectures:
    - a dictionary to hold the files we've already seen
    - a stack ↴ (we'll implement ours with a list) to hold directories and files as we go through them
    - a list to hold our output tuples
      
    """
    seen_already = {}
    stack = [directory] # starting directory, as list
    dups = [] # duplicates - tuples of (dup file, orig file)

    while len(stack) > 0:
        current_path = stack.pop()

        # If it's a directory, put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path, path):
                full_path = os.path.join(current_path, path)

        # If it's a file,
        else:

            # Get contents of file
            with open(current_path) as file:
                file_contents = file.read()

            # Get the time it was edited
            edit_time = os.path.getmtime(current_path)

            # If we've seen it before
            if file_contents in seen_already:
                existing_time = seen_already[file_contents]
                existing_path = seen_already[file_contents]

                if edit_time > existing_time:

                    # Current file is the dup!
                    duplicates.append((current_path, existing_path))

                else:

                    # Delete the old file cuz it's the dup
                    duplicates.append((existing_path, current_path))

                    seen_already[file_contents] = ((edit_time, current_path))


            else:

                # If it's a new file, throw it in seen_already & record the path
                seen_already[file_contents] = ((edit_time, current_path))



    return duplicates


    # Heruistic: the more recently added file will be the duplicate


""" Final Solution! to dup file finder """  

def find_dups(starting_dir):
    """ https://www.interviewcake.com/question/python3/find-duplicate-files?course=fc1&section=hashing-and-hash-tables """
    files_seen_already = {}
    stack = [starting_dir]

    duplicates = [] # List of tuples (dup file, orig )

    while len(stack):
        current_path = stack.pop()

        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        else:
            # Get it's hash & time if its a file
            file_hash = sample_hash_file(current_path)
            last_edit = os.path.getmtime(current_path)

            if file_hash in files_seen_already:

                prev_edit, prev_path = files_seen_already[file_hash]

                # If the current time is greater, it is dup!
                if last_edit > prev_edit:
                    duplicates.append((current_path, prev_path))

                else:
                    duplicates.append((prev_path, current_path))

                    # Update files_seen_already w/ new info
                    files_seen_already[file_hash] = (last_edit, current_path)

            else:
                # If it's a new file, throw it in files_seen
                files_seen_already[file_hash] = (last_edit, current_path)

    return duplicates


def sample_hash_file(path):
    # Helper function
    byte_size = 4000
    total_bytes = os.path.getsize(path)
    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        if total_bytes < byte_size * 3:
            hasher.update(file.read())

        else:
            bytes_btw_each = (total_bytes - byte_size * 3) / 2

            # Read first, middle, and last blocks:
            for x in range(3):
                start = x * (bytes_btw_each + byte_size)
                file.seek(start)
                sample = file.read(byte_size)
                hasher.update(sample)

    return hasher.hexdigest() 


""" Greedy algo for the max profit finder """  
def get_max_profit(stock_prices):
    """ stock_prices is a list of stocks from that day
    note: you can only sell AFTER you buy, and profit could be negative
    """  

    if len(stock_prices) < 2:
        raise ValueError('Err, profits require at least 2 prices')

    # Initialize
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):
        price = stock_prices[i]

        profit = price - min_price # Potential profit

        max_profit = max(max_profit, profit) # Update if we did better

        min_price = min(min_price, price) # Update if we found lower

    return max_profit


""" Greedy algo for the max profit finder """  
def max_prod_of_3(ints):

    if len(ints) < 3:
        raise ValueError('Error, less than 3')

    # Initialize
    hi = max(ints[0], ints[1])
    lo = min(ints[0], ints[1])
    hi_of_2 = ints[0] * ints[1] # highest product of 2
    lo_of_2 = ints[0] * ints[1] # lowest 
    hi_of_3 = ints[0] * ints[1] * ints[2] # highest product of 3

    # Iter through, updating any of the variables:
    for i in range(2, len(ints)):
        curr = ints[i]

        hi_of_3 = max(hi_of_3,
                        curr * hi_of_2,
                        curr * lo_of_2)
        hi_of_2 = max(hi_of_2,
                        curr * hi,
                        curr * lo)
        lo_of_2 = min(lo_of_2,
                        curr * hi,
                        curr * lo)
        hi = max(hi, curr)
        lo = min(lo, curr)

    return hi_of_3

""" Greedy algo for TWO passes through a list of ints """  
def prod_finder(ints):
    """ You have a list of integers, and for each index you want to find 
    the product of every integer except the integer at that index.
    * No division allowed! *

    Strategy:  
    The product of all the integers except the integer at each index can be broken down into two pieces:
        1- the product of all the integers before each index, and
        2- the product of all the integers after each index.

    >>> prod_finder([1, 2, 3, 4])
    [24, 12, 8, 6]

    >>> prod_finder([0, 2, 3, 4])
    [24, 0, 0, 0]

    >>> prod_finder([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> prod_finder([3, 1, 2, 5, 6, 4])
    [240, 720, 360, 144, 120, 180]



    """
    if len(ints) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')


    products = [None] * len(ints)    

    # Forward traversal:
    p = 1 # Product so far, before index
    for i in range(len(ints)):

        products[i] = p
        p *= ints[i] 

    # Reverse traversal:
    p = 1 # Re-initialize product so far, for after index
    for i in range(len(ints) - 1, -1, -1):

        products[i] *= p
        p *= ints[i]


    return products


""" Greedy algo for an inplace random shuffle """  
def inplace_shuffle(deck):
    """
    Write a function for doing an in-place ↴ shuffle (random ordering) of a list.

    The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

    Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.

    # >>> inplace_shuffle([1, 2, 3, 4, 5, 6])
    # []

    Strategy:
    - We choose a random item to move to the first index, then we choose a 
    random other item to move to the second index, etc. We "place" an item 
    in an index by swapping it with the item currently at that index.

    O(n) time and O(1) space

    """

    print(random.randint(1, 111))

    if len(deck) <= 1:
        return deck 

    last_index = len(deck) - 1

    # Iterate through deck, chosing two random items and swapping them.
    # Must be AFTER current item
    for i in range(0, len(deck) - 1):

        random_i = random.randint(i, last_index)

        if random_i != i:

            deck[i], deck[random_i] = deck[random_i], deck[i] # Swap!


    return out


""" Given: Binary search, iterative - works on a SORTED list """  
def binary_search_iter(target, nums):
    """ 
    A binary search algorithm finds an item in a sorted list in O(log(n)) time.

    https://www.interviewcake.com/concept/python3/binary-search?course=fc1&section=sorting-searching-logarithms

    I got a time out on these?    
    # >>> binary_search_iter(6, [1, 6, 18, 22, 99])
    # True

    # >>> binary_search_iter(99, [1, 99])
    # True

    # >>> binary_search_iter(66, [1, 9])
    # False

    # >>> binary_search_iter(6, [])
    # False

    """ 
    # Define the "walls" around the current position. 
    # Starting with the 0th index, we need floor -1 and ceiling at length: 
    f = -1 
    c = len(nums)


    while f + 1 <= c:

        # Find the 'half index' - whole number
        half_ix = (c - f) // 2

        guess_ix = f + half_ix

        guess_value = nums[guess_ix]

        if guess_value == target:
            return True

        elif guess_value > target:
            # It is to the left, so re-assign ceiling index:
            c = guess_ix

        else:
            # It is to the right, so re-assign floor index:
            f = guess_ix



    return False 


""" Ordered List target finder O log(n) """  
def rotation_point(words):
    """
    Write a O(lgn) time function for finding the index of the "rotation point," 
    which is where the letters start from the beginning of alphabet. 
    At each iteration, we go right if the item we're looking at is greater 
    than the first item and we go left if the item we're looking at is less 
    than the first item.
    
    >>> rotation_point(['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i'])
    9

    >>> rotation_point(['a', 'b', 'c', 'd', 'e', 'g', 'i'])
    1
    
    >>> rotation_point(['a', 'a', 'a', 'a', 'a'])
    5

    Strategy: Do a binary search, using alphanumeric ordering 
    ** The rotation point is to our left if the current item is less than the 
    first item. Else it's to our right.


    """
    first_word = words[0]
    f = -1 #floor index
    c = len(words) #ceiling index

    while f < c:
        # Guess a point halfway btw floor anc ceil
        guess_ix = f + ((c - f) // 2)
        guess = words[guess_ix]

        # If guess comes after first word or is the first word, go right:
        if guess <= first_word:

            # Go right, setting the floor to the guess index
            f = guess_ix

        else:

            # Go left, setting the ceil to the guess index
            c = guess_ix

        # If Floor and Ceil have converged,
        if f + 1 == c:
            return c



""" duplicate finder O log(n) """  
def dup_finder(ints):
    """
    We have a list of integers, where:
    - the integers are in the range 1...n, and the list has a length of n+1
    - our list has at least one integer which appears at least twice. 
    - but it may have several duplicates, and each duplicate may appear more than twice.


    Write a function which finds an integer that appears more than once in our 
    list. (If there are multiple duplicates, you only need to find one of them.)
    
    ** Optimize for space **

    # >>> dup_finder([1, 1, 2, 3])
    # 1
    # >>> dup_finder([1, 2, 3])
    # None   
    # >>> dup_finder([1, 1, 2, 2, 3])
    # 1

    Strategy: 
    """
    floor = 1
    ceil = len(ints) - 1

    while floor < ceil:

        # Divide our range into upper and lower nonoverlapping range
        mid = floor + ((ceil - floor) // 2)
        low_floor, low_ceil = floor, mid
        upp_floor, upp_ceil = mid + 1, ceil 

        # Count the number of items in lower range
        low_items = 0
        for item in ints:
            if item >= low_floor and item <= low_ceil:
                low_items += 1

        # What is the distict possible number of integers in lower range?
        low_max = low_ceil - low_floor + 1
    
        if low_items > low_max:
            # There must be duplicate in the lower range by pigeonhole principle
            # So, iteratively use that range now
            floor, ceil = low_floor, low_ceil

        else:
            # There must be duplicate in the hi range by pigeonhole principle
            # So, iteratively use that range now
            floor, ceil = upp_floor, upp_ceil

    # When floor and ceil have converged, we found our repeating number!
    return floor


""" Given: Binary Tree demo """  
class BinaryTreeNode(object):
    """ https://www.interviewcake.com/concept/python3/binary-tree?course=fc1&section=trees-graphs"""  

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert_right(self, data):
        self.right = BinaryTreeNode(data)
        return self.right 


    def insert_left(self, data):
        self.left = BinaryTreeNode(data)
        return self.left  


""" BFS: write a 'superbalanced' binary tree """
def superbalanced(root):
    """ https://www.interviewcake.com/question/python3/balanced-binary-tree 
    Write a BinaryTree where the difference between the depths of any two
    leaf nodes is no greater than one. 

    # >>> superbalanced - how do you test?
    
    """
    # A tree w/o nodes is superbalanced
    if root is None:
        return True 

    # This will short-circuit if it reaches more than 2
    depths = []

    # Create a stack that will store tuples (node, depth)
    nodes = []
    nodes.append((root, 0))



    while len(nodes):
        # Pop tuple from top of stack
        node, depth = nodes.pop()

        # If we found a leaf
        if (not node.left) and (not node.right):

            if depth not in depths:
                depths.append(depth)

                # Check if it is unbalanced
                if ((len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False

        # If this is not a leaf, keep stepping down
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True

""" is it a Binary Search Tree (BST)? """
def is_bst(root):
    """ https://www.interviewcake.com/question/python3/bst-checker?course=fc1&section=trees-graphs 
    Write a function that checks if a tree is a Binary Search Tree (BST)? 

    """

    # Start at root, initializing Nodes, low & hi bounds
    stack = [(root, -float('inf'), float('inf'))]

    # Depth-first traversal
    while len(stack):

        # Get the first item from top of stack
        node, lo_bound, hi_bound = stack.pop()

        # If node is invalid, return False right away
        if (node.data <= lo_bound) or (node.data >= hi_bound):
            return False

        if node.left:
            # This node must be less than the current node
            stack.append((node.left, lo_bound, node.data))


        if node.right:
            # This node must be greater than the current node
            stack.append((node.right, node.data. hi_bound))

    # If we have checked all nodes
    return True


""" Recursive formula for finding the 'rightmost' element in a BST"""
def find_largest(root_node):

    if root_node.right:

        return find_largest(root_node.right)

    else:
        return root_node.data 

""" Recursive formula for finding the 'rightmost' element in a BST"""
def find_2nd_largest(root_node):

    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    # This saves space, making it O(1) instead of O(h)
    current = root_node
    while current:
        # If current is largest and has a left subtree,
        # 2nd largest is thus the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.right)

        # Else if current is parent of largest, and largest has no children,
        # Current is 2nd largest
        if (current.right and 
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right



""" Graph coloring - NOT done! """
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set() # All neighbors are GraphNode objects
        self.color = None # This will be set as we traverse the graph





""" Bitwise Functions """
def find_unique_int_slow(dups):
    """ 
    Given the list of IDs, which contains many duplicate integers 
    and one unique integer, find the unique integer.
    Not ordered or sequential
    https://www.interviewcake.com/question/python3/find-unique-int-among-duplicates?course=fc1&section=bit-manipulation
    
    >>> find_unique_int_slow([1, 2, 2, 3, 3, 4, 4])
    1
    >>> find_unique_int_slow([1, 1, 2, 2, 3, 3, 4, 4])
    'None'
    >>> find_unique_int_slow([1, 2, 3, 4, 1, 2, 3, 4, 5])
    5


    """
    # Create occurance dictionary
    counts = {} 

    for i in dups:
        counts[i] = counts.get(i, 0) + 1

    # Create a set of values with count of 1
    s = {k for k in counts.keys() if counts[k] == 1}

    if len(s) != 1:
        return 'None'

    return s.pop() # Assuming there is only one value


def find_unique_int(delivery_ids):

    """ 
    Faster version using XOR operation!    
    >>> find_unique_int([1, 2, 2, 3, 3, 4, 4])
    1
    >>> find_unique_int([1, 1, 2, 2, 3, 3, 4, 4])
    0
    >>> find_unique_int([1, 2, 3, 4, 1, 2, 3, 4, 5])
    5


    """

    unique_id = 0 # Flag

    for idd in delivery_ids:
        unique_id ^= idd

    return unique_id



""" Given """

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        """Return and remove the last item"""

        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None

        else:
            return self.items[-1]


""" Write a MaxStack class """
class MaxStack(Stack):

    def get_max(self):
        """Return the LARGEST item without removing it"""

        if not self.items:
            return None

        else:
            # Search for max
            maxx = self.items[0]
            for i in self.items:
                if i > maxx:
                    maxx == i 
            return maxx















# Doctest Section:
if __name__ == '__main__':
    import doctest

    # print(prod_finder([1, 2, 3]))
    # print(prod_finder([-3, -5, -7]))

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')

