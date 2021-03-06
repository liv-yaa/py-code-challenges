# Following this! https://codechalleng.es/bites/paths
# ===================================================
# ===================================================

#  [Collections] Bite 108. Loop over a dict of `collections.namedtuples`, calculating a total score - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import namedtuple
class NinjaBelts:
	BeltStats = namedtuple('BeltStats', 'score ninjas') # typename, field_names

	ninja_belts = {'yellow': BeltStats(50, 11),
	               'orange': BeltStats(100, 7),
	               'green': BeltStats(175, 1),
	               'blue': BeltStats(250, 5)} # Can have more belts


	def get_total_points(self, belts=ninja_belts):
		"""

		** What is a `namedtuple`? - a dict-like container from the Collections module
		** More powerful than a dictionary because:
		- it is iterable ** (also unordered tho)
		- you can access by key
		- You can specify `typename` for the item

		Calculate the amount of points rewarded on PyBites given the
		ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
		(of course there are more points but let's keep it simple)

		Make your code generic so if we update ninja_belts to include
		more belts (which we do in the tests) it will still work.

		Ah and you can get score and ninjas from the namedtuple with nice
		attribute access: belt.score / belt.ninjas (reason why we get
		you familiar with namedtuple here, because we love them and use
		them all over the place!)

		Return the total number of points int from the function.
		"""
		total = 0
		for k, v in belts.items():
			total += v.score * v.ninjas
		return total
if __name__ == '__main__':
	nb = NinjaBelts()
	# print(nb.get_total_points())

#  [Collections] Bite 45. Keep a Queue of last n items using `collections.deque` - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import deque
def my_queue(n=5):
	return deque(maxlen=n) # 'append', 'appendleft', 'clear', 'count', 'extend', 'extendleft', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate'

if __name__ == '__main__':
	mq = my_queue()
	# for i in range(10):
	# 	# print(dir(mq))
	# 	mq.append(i)
	# 	print((i, list(mq)))

	"""Queue size does not go beyond n int, this outputs:
	(0, [0])
	(1, [0, 1])
	(2, [0, 1, 2])
	(3, [0, 1, 2, 3])
	(4, [0, 1, 2, 3, 4])
	(5, [1, 2, 3, 4, 5])
	(6, [2, 3, 4, 5, 6])
	(7, [3, 4, 5, 6, 7])
	(8, [4, 5, 6, 7, 8])
	(9, [5, 6, 7, 8, 9])
	"""

#  [Collections] Bite 180.Group names by country using `collections.defaultdict`  - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import defaultdict
class DefaultDict:
	"""`defaultdict` - "dict subclass that calls a factory function to supply missing values "
	
	Powerful! You can directly append to existing values with the defaultdict.append method,
	and it even initializes values with a zero:

		d = defaultdict(list)
		for k, v in s:
			d[k].append(v)
		
		>>> d.items()
		[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

	"""
	data = """last_name,first_name,country_code
		Watsham,Husain,ID
		Harrold,Alphonso,BR
		Apdell,Margo,CN
		Tomblings,Deerdre,RU
		Wasielewski,Sula,ID
		Jeffry,Rudolph,TD
		Brenston,Luke,SE
		Parrett,Ines,CN
		Braunle,Kermit,PL
		Halbard,Davie,CN"""

	def group_names_by_country(self, data=data):
		""" Take string and returns a defaultdict """
		countries = defaultdict(list) # Provide an initial value for the dict object
		
		d = self.data.strip().split()[1:]
		for l in d:
			l = l.split(',')
			countries[l[2]].append(l[1] + ' ' + l[0])

		return countries
if __name__ == '__main__':
	dd = DefaultDict()
	# print(dd.group_names_by_country())

#  [Collections] Bite 4. Top tags using `collections.Counter`  - NOT DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# [Data Analysis] Bite 188. Get statistics from PyBites test code - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import statistics
from urllib.request import urlretrieve
class Stats:

	TMP = os.getenv("TMP", "/tmp")
	S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
	DATA = 'testfiles_number_loc.txt'
	STATS = os.path.join(TMP, DATA)
	if not os.path.isfile(STATS):
	    urlretrieve(os.path.join(S3, DATA), STATS)

	STATS_OUTPUT = """
		Basic statistics:
		- count     : {count:7d}
		- min       : {min_:7d}
		- max       : {max_:7d}
		- mean      : {mean:7.2f}

		Population variance:
		- pstdev    : {pstdev:7.2f}
		- pvariance : {pvariance:7.2f}

		Estimated variance for sample:
		- count     : {sample_count:7.2f}
		- stdev     : {sample_stdev:7.2f}
		- variance  : {sample_variance:7.2f}
		"""

	def get_all_line_counts(self, data: str = STATS) -> list:
		"""Get all 186 line counts from the STATS file,
		returning a list of ints"""
		# TODO 1: get the 186 ints from downloaded STATS file
		# sd = statistics.mean([1, 2, 3])
		c = []
		with open(data, 'r') as fh:
			for line in fh:
				n = None
				try:
					n = int(line.strip().split()[0])
				except:
					print('error')
				c.append(n)
		return c

	def create_stats_report(self, data=None):
		if data is None:
			# converting to a list in case a generator was returned
			data = list(self.get_all_line_counts())

		# taking a sample for the last section
		sample = list(data)[::2]

		# TODO 2: complete this dict, use data list and for the last 3 sample_ variables, use sample list
		stats = dict(count=None,
			min_=None,
			max_=None,
			mean=None,
			pstdev=None,
			pvariance=None,
			sample_count=None,
			sample_stdev=None,
			sample_variance=None,
			)

		stats['count'] = len(data)
		stats['min_'] = min(data)
		stats['max_'] = max(data)
		stats['mean'] = statistics.mean(data)
		stats['pstdev'] = statistics.pstdev(data)
		stats['pvariance'] = statistics.pvariance(data)
		stats['sample_count'] = len(sample)
		stats['sample_stdev'] = statistics.stdev(sample)
		stats['sample_variance'] = statistics.variance(sample)

		return self.STATS_OUTPUT.format(**stats)
if __name__ == '__main__':
	s = Stats()
	# print(s.create_stats_report())

# [Data Formats] Bite 38. Using ElementTree to parse XML: DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import xml.etree.ElementTree as ET
class XMLParser:
	"""
	Parses XML using `ElementTree`:
	The Element type is a flexible container object, designed to store hierarchical data structures in memory. 
	The type can be described as a cross between a list and a dictionary.
	https://docs.python.org/2/library/xml.etree.elementtree.html

	"""
	# from OMDB
	xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
		<root response="True">
		<movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
		<movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
		<movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
		<movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
		<movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
		</root>'''  # noqa E501

	def get_tree(self):
		""" Use ET.fromstring - this reads data from the string 

		print(root, root.tag, root.attrib) # <Element 'root' at 0x107a3f910>, 'root', {'response': 'True'}
		Children are nested, and we can access specific child nodes by index:
		"""
		# print('get_tree root')
		root = ET.fromstring(self.xmlstring)
		return root
	
	def get_movies(self):
		"""Call get_tree and retrieve all movie titles, return a list or generator"""
		# print('get_movies')
		root = self.get_tree()
		# print(root)

		r = []
		for c in root.iter(tag='movie'):
			yield movie.attrib['title']


	def _get_runtime(self, movie):
		""" Helper fxn to extract minutes from runtime attribute """
		return int(movie.attrib['runtime'].rstrip(' min'))

	def get_movie_longest_runtime(self):
		""" Call get_tree again and return the movie title for the movie with the longest
		runtime in minutes, for latter consider adding a _get_runtime helper """
		tree = self.get_tree()
		movies = [(movie.attrib['title'], self._get_runtime(movie)) for movie in tree.iter(tag='movie')]
		max_movie, max_runtime = max(movies, key=lambda m: m[1])
		return max_movie
if __name__ == "__main__":
	# STUCK - need to look up answers
	x = XMLParser()
	# print(x.get_tree())
	# print(x.get_movies())
	# print(x.get_movie_longest_runtime())

# [Data Formats] Bite 130. Analyzing basic JSON Car Data: - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import Counter
import requests
class JSONParser:
	""" Data analysis with basic car data """

	CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'
	with requests.Session() as s:
		data = s.get(CAR_DATA).json() # A list of dicts
		c = Counter()
		# for d in self.data:
		# 	if d['year'] == year:
		# 		c.update([d['automaker']])
		# return [str(k) for k, v in sorted(c.items(), key=lambda item:item[1])[::-1]][0]

	def get_models(self, automaker, year):
	    """Filter cars 'data' by 'automaker' and 'year',
	       return a set of models (a 'set' to avoid duplicate models)"""
	    s = set()
	    for m in self.data:
	    	if m['automaker'] == automaker and m['year'] == year:
	    		s.add(str(m['model']))
	    return s 
if __name__ == "__main__":
	# See testCars.py for full test suite
	j = JSONParser()
	# models = j.get_models('Volkswagen', 2008)

# [Data Formats] Bite 13. Convert dict to namedtuple/json - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import namedtuple
from datetime import datetime
import json
class dictToJSON:
	blog = dict(name='PyBites',
		founders=('Julian', 'Bob'),
		started=datetime(year=2016, month=12, day=19),
		tags=['Python', 'Code Challenges', 'Learn by Doing'],
		location='Spain/Australia',
		site='https://pybit.es')

	# define namedtuple here
	MyTuple = namedtuple('MyTuple', sorted(blog)) # Create a subclass of namedtuple by passing the keys of the dict:

	def dict2nt(self, dict_):
		"""
		From docs: " To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):"
			>>> d = {'x': 11, 'y': 22}
			>>> Point(**d)
		assert nt.name == 'PyBites'
		assert nt.founders[1] == 'Bob'
		assert nt.tags[2] == 'Learn by Doing'
		assert nt.started.year == 2016

		assert nt.__class__.__base__ == tuple
		assert hasattr(nt, '_asdict')
		"""
		# Create instances from this dict, or other dicts with matching keys
		return self.MyTuple(**dict_)


	def nt2json(self, nt):
		"""
		assert type(output) == str
	    data = json.loads(output)
	    assert data['name'] == 'PyBites'
	    assert data['founders'][0] == 'Julian'
	    assert data['tags'][0] == 'Python'
	    assert data['started'][:4] == '2016'
		"""
		j = {}
		for data in nt._asdict().items():
			v = data[1]
			if isinstance(v, datetime):
				v = str(v)
			j[data[0]] = v
		return json.dumps(j)
if __name__ == "__main__":
	dj = dictToJSON()
	# print(dj.MyTuple, dj.MyTuple._fields, dj.MyTuple._fields[1]) # Prints location
	# natu = dj.dict2nt(dict_=dj.blog)
	# print(natu)
	# jsn = dj.nt2json(nt=natu)
	# print(jsn)
	# print(jsn["name"])
	# print(jsn['founders'][0])
	# print(jsn['tags'][0])
	# print(jsn['started'][:4])

# [String Manip] Bite 105. Slice and dice - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from string import ascii_lowercase
class SliceDice:

	text = """
		One really nice feature of Python is polymorphism: using the same operation
		on different types of objects.
		Let's talk about an elegant feature: slicing.
		You can use this on a string as well as a list for example
		'pybites'[0:2] gives 'py'.
		 The first value is inclusive and the last one is exclusive so
		here we grab indexes 0 and 1, the letter p and y.
		  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
		but here is the kicker: you can use this on a list too!
		['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
		and now you know about slicing from the end as well :)
		keep enjoying our bites!
		"""


	def slice_and_dice(self, text):
		"""Get a list of words from the passed in text.
		Instructions:
		1. Take the block of text provided and strip off the whitespace at both ends. 
		2. Split the text by newline (\n).
		3. Loop through lines, for each line:
		strip off any leading spaces,
		check if the first character is lowercase,
		if so, split the line into words and get the last word,
		strip the trailing dot (.) and exclamation mark (!) from this last word,
		and finally add it to the results list.
		Return the results list.

		"""
		results = []
		for line in self.text.strip().splitlines():
			line = line.lstrip()

			if line[0] not in ascii_lowercase:
				continue

			words = line.split()
			last_word_stripped = words[-1].rstrip('!.')
			results.append(last_word_stripped)

		return results

# [String Manip] Bite 106. Strip out vowels and count the number of replacements - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from typing import Tuple
class ZenReplace:
	text = """
		The Zen of Python, by Tim Peters

		Beautiful is better than ugly.
		Explicit is better than implicit.
		Simple is better than complex.
		Complex is better than complicated.
		Flat is better than nested.
		Sparse is better than dense.
		Readability counts.
		Special cases aren't special enough to break the rules.
		Although practicality beats purity.
		Errors should never pass silently.
		Unless explicitly silenced.
		In the face of ambiguity, refuse the temptation to guess.
		There should be one-- and preferably only one --obvious way to do it.
		Although that way may not be obvious at first unless you're Dutch.
		Now is better than never.
		Although never is often better than *right* now.
		If the implementation is hard to explain, it's a bad idea.
		If the implementation is easy to explain, it may be a good idea.
		Namespaces are one honking great idea -- let's do more of those!
		"""
	vowels = 'aeiouAEIOU'

	def strip_vowels(self, text: str = text) -> Tuple[str, int]:
		"""Replace all vowels in the input text string by a star
		character (*).
		Return a tuple of (replaced_text, number_of_vowels_found)

		So if this function is called like:
		strip_vowels('hello world')

		... it would return:
		('h*ll* w*rld', 3)

		The str/int types in the function defintion above are part
		of Python's new type hinting:
		https://docs.python.org/3/library/typing.html"""
		new_str = []
		chars = list(text)
		vows = 0

		for c in chars:
			if c.lower() in self.vowels:
				c = '*'
				vows += 1
			new_str.append(c)
		return ''.join(new_str), vows
if __name__ == '__main__':
	z = ZenReplace()
	# print(z.strip_vowels())

# [Datetime Module] Bite 16. PyBites date generator - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from datetime import datetime, timedelta 
from itertools import islice
class DateGenerator:

	PYBITES_BORN = datetime(year=2016, month=12, day=19) # bday

	def gen_special_pybites_dates(self):
		""" * A Generator: the state of the function is remembered. Every time you call next, it increments the state

			* From docs: class `datetime.datetime` https://docs.python.org/3/library/datetime.html
				A combination of a date and a time. 
				Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
		 """
		# Every year mark from bday			
		# Every 100 days mark from bday
		days = 0
		while True:			
			days += 1
			if days % 100 == 0 or days % 365 == 0:
				yield self.PYBITES_BORN + timedelta(days = days)
if __name__ == '__main__':
	dg = DateGenerator()
	# gen = dg.gen_special_pybites_dates()
	# dates = list(islice(gen, 10))
	# print(dates)

#  Bite 109. Workout dict lookups and raising an exception - NOT DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workout:
	WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
	                    'Monday': 'Chest+biceps',
	                    'Saturday': 'Rest',
	                    'Sunday': 'Rest',
	                    'Thursday': 'Legs',
	                    'Tuesday': 'Back+triceps',
	                    'Wednesday': 'Core'}
	REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
	INVALID_DAY = 'Not a valid day'


	def get_workout_motd(self, day):
		"""First title case the passed in day argument
		(so monday or MONDAY both result in Monday).

		If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

		If day is in WORKOUT_SCHEDULE retrieve the value (workout)
		and return the following:
		- weekday, return TRAIN with the workout value interpolated
		- weekend day (value 'Rest'), return CHILL_OUT

		Examples:
		- if day is Monday -> function returns 'Go train Chest+biceps'
		- if day is Thursday -> function returns 'Go train Legs'
		- if day is Saturday -> function returns 'Chill out!'
		- if day is nonsense -> function returns 'Not a valid day'

		Trivia: /etc/motd is a file on Unix-like systems that contains
		a 'message of the day'
		"""
		# print(self.WORKOUT_SCHEDULE)
		if len(day) > 0:
			d = day[0].upper()
			for i in range(1, len(day)):
				d += day[i].lower()

			# Check that d is valid
			if d in self.WORKOUT_SCHEDULE.keys():
				# print('OK')
				return self.WORKOUT_SCHEDULE.get(d)			
		else:

			return self.INVALID_DAY
if __name__ == '__main__':
	w = Workout()
	# print(w.get_workout_motd('Monday'))
	# print(w.get_workout_motd('monday'))
	# print(w.get_workout_motd('Tuesday'))
	# print(w.get_workout_motd('TuEsday'))
	# print(w.get_workout_motd('Wednesday'))
	# print(w.get_workout_motd('wednesday'))
	# print(w.get_workout_motd('Thursday'))
	# print(w.get_workout_motd('Friday'))
	# print(w.get_workout_motd('Saturday')) # CHILL_OUT
	# print(w.get_workout_motd('Sunday')) # CHILL_OUT
	# print(w.get_workout_motd('')) # INVALID_DAY
	# print(w.get_workout_motd('monday3')) # INVALID_DAY

# [Web Scraping] Bite 55. Get the latest game releases from Steam's RSS feed - DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from collections import namedtuple
from pprint import pprint
import feedparser # PyPi "parse RSS feeds in Python" - had to install with pip3
class GameScraper:
	FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"
	# Create a subclass of namedtuple by passing the keys of the dict
	# Now we have the ability to create custom Game objects, with fields `title` and `link`
	Game = namedtuple('Game', 'title link')

	def get_games(self):
		""" Parses Steam's RSS feed and returns a list of Game namedtuples, pull out the names of the games in the feed as well as their URLs. 
			Use the Game namedtuple provided. Return a list of `Game` namedtuples
		"""
		out = [] 
		for e in feedparser.parse(self.FEED_URL)['entries']:
			# Create a Game namedtuple instance and add it to the dictionary
			out.append(self.Game(e['title'], e['link']))
		
		return out
if __name__ == '__main__':
	gs = GameScraper()
	# pprint(gs.get_games())
""" 
	Decorator : 
	===========
		A Py object that is used to modify a function, method, or class definition
		The decorator is passed to the original object being defined and returns a 
		modified object, which is then bound to the name in the definition.

		Syntax:

			@mydecorator
			def my_function(args):
				...

		is the same as:

			def my_function(args):
				...
			>>> my_function = mydecorator(my_function)


		Decorators can:
		- Be stacked to run inside out

		Common uses:
		- Caching
		- Access checks in web frameworks (like Flask!)
"""
# [Decorators] Bite 218. Create a sandwich decorator - SUPER CLOSE NOT DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from functools import wraps # @wraps is to preserve the original func's docstring
UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="
ingredients = ['bacon', 'lettuce', 'tomato']

def sandwich(func):
	""" A *decorator* that prints UPPER_SLICE and LOWER_SLICE before and after 
	calling the function (func) that is passed in
	"""
	@wraps(func)
	def wrapped(*args, **kwargs):
		res = func(*args, **kwargs)
		# print('res', res)

		# print(func, res, UPPER_SLICE, LOWER_SLICE)
		wrap = UPPER_SLICE + '\n' + res + '\n' + LOWER_SLICE
		return wrap

	return wrapped

@sandwich
def add_ingredients(ingredients):
	""" A function that is passed to the decorator, sandwich.
		Takes a list of ingredients. All it does is return ingredients as a string.
	"""
	# print(' / '.join(ingredients))

	return ' / '.join(ingredients)

if __name__ == '__main__':
	# print(add_ingredients(ingredients))
	pass

# [Decorators] Bite 22. Write a decorator with argument - NOT DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# <p><strong>I code ...</strong></p>

# from functools import wraps


def make_html(element, func):
	""" Decorator that wraps html in tags 
		- is a callable
		- takes a callable (element - takes get_text)
		- returns a callable (wrapped)

	"""
	# @wraps(func)
	def wrapper(*args, **kwargs):
	# 	# Element is a callable
	# 	# print('args', *args, **kwargs)
		# print(type(element))
		# return func
		print('test', func)

	return wrapper
	# return 


# make_html(make_html(get_text(text)))

# Not changing
# @make_html(element='p')
# @make_html(element='strong')
# def get_text(text='I code with PyBites'):
# 	return text

# Demo
def trace(func):
	def wrapper(*args, **kwargs):
		print('test', *args, **kwargs)
		return func(*args, kwargs)
	return wrapper

@trace
def get_text(text='I code with PyBites'):
	return type(text)









if __name__ == '__main__':

	print(get_text())
	# assert get_text() == '<p><strong>I code with PyBites</strong></p>'























































