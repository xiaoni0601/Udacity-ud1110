#Quiz: Practice Debugging
# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = int(input("Enter any 2-digit number: "))
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = userInput
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))



#Import Local Scripts:
#1.如果要导入的python 脚本与当前脚本位于同一个目录：import 脚本名(other_script),无需.py文件后缀；该导入语句放在顶部

#################The Python Standard Library¶:
# https://docs.python.org/3/library/index.html
#################Python 3 Module of the Week¶:
#https://pymotw.com/3/


# Quiz: Compute an Exponent

#It's your turn to import and use the math module. 
# Use the math module to calculate e to the power of 3. print the answer.
"""It's your turn to import and use the math module. 
Use the math module to calculate e to the power of 3. print the answer.
"""

# print e to the power of 3 using the math module
import math
e = 3
print(math.exp(3))


#Quiz: Password Generator
"""
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
Your function should not accept any arguments and should reference the global variable word_list to build the password
"""

# Use an import statement at the top
import string
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
def generate_password():
    return ''.join(random.sample(word_list, 3))


#####################################################
# solution from udacity:
# def generate_password():
#    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


# It should return a string consisting of three random words 
# concatenated together without spaces



# test your function
print(generate_password())



####适合其他情形的导入方式：
from collections import defaultdict, namedtuple###只访问 collections模块中的defaultdict, namedtuple等等
##from module_name import object_name##
##from module_name import first_object, second_object##
##import module_name as new_name##
# from multiprocessing as mp ##更简洁；也可以防止命名重复；有专门的缩写
# print(mp.cpu_count())

#from random import * ##请勿使用该语句，不见得更加方便，别人不太容易知道导入对象的定义，会引起困惑；
                     ##若的确全部导入，只需要标准写法：import random

##Modules, Packages, and Names
####import package_name.submodule_name.for exampel: import os.path


###如果没有包含在python中，如何获取这些软件包？Third-Party Libraries
#pip是标准的软件包管理器
#Anaconda也是热门的软件包管理器，专门针对data science

#######Useful Third-Party Packages: 
#Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
#IPython - A better interactive Python interpreter
#requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
#Flask - a lightweight framework for making web applications and APIs.
#Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
#Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
#pytest - extends Python's builtin assertions and unittest module.
#PyYAML - For reading and writing YAML files.
#NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
#pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
#matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
#ggplot - Another 2D plotting library, based on R's ggplot2 library.
#Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
#pyglet - A cross-platform application framework intended for game development.
#Pygame - A set of Python modules designed for writing games.
#pytz - World Timezone Definitions for Python


##### Getting the information you need to know: finding information quickly! more ! import!
##### Hierarchy of Online Resources:
# No1. The Python Tutorial 
# No2. The Python Language and Library References
# No3. Third-Party Library Documentation 
# No4. The websites and blogs of prominent experts
# No5. StackOverflow 
# No6. Bug Trackers
# No7. Random Web Forums


#Practice Question
""" 
Question: Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. 
The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. 
It should then use it to print the flower name with the same first letter (from dictionary created in the first function).
"""

# function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# Main function that prompts for user input, parses out the first letter
# includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
# print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()