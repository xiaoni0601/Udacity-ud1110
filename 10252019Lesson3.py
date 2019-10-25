# Quiz: len, max, min, and Lists
# QUESTION 1 OF 4
# What would the output of the following code be? 
# (Treat the comma in the multiple choice answers as newlines.)
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))



# Quiz: sorted, join, and Lists
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# Quiz: append and Lists
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))


# Check for Understanding
# Quiz: Tuples

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])
print(tuple_b[1])

# Quiz: Define a Dictionary
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
population = { 'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5 }
    
print(population)

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5




elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': False},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', 'is_noble_gas': True}}
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't



# Quiz: Count Unique Words
# plit verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
# Convert the list into a data structure that would keep only the unique elements from the list.
# Print the length of the container.
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split(' ')
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set) - 1
print(num_unique, '\n')

# Quiz: Verse Dictionary
# In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys and the number of times they appear in verse stored as values. Use this dictionary to answer the following questions. Submit these answers in the quiz below the code editor.

# Try to answer these using code, rather than inspecting the dictionary manually!

# 1. How many unique words are in verse_dict?
# 2. Is the key "breathe" in verse_dict?
# 3. What is the first element in the list created when verse_dict is sorted by keys?
# Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
# 4. Which key (word) has the highest value in verse_dict?
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
a = list(verse_dict.keys())
a.sort()
sorted_keys = a

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(verse_dict.keys()))    #or print(sorted_keys[-1]) 

#数据结构特征:
# 数据结构    ordered  Mutable      Constructor	        Example
# List	    Yes 	Yes   	  [ ] or list()	    [5.7, 4, 'yes', 5.7]
# Tuple	    Yes	    No	      ( ) or tuple()	    (5.7, 4, 'yes', 5.7)
#  Set	    No  	Yes	      {}* or set()	    {5.7, 4, 'yes'}
#  Dict	    No	    No**	  { } or dict()    	{'Jun': 75, 'Jul': 89}