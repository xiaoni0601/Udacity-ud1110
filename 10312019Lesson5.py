def cylinder_volume(height, radius):###Function Header--格式："def" + "具有描述性名字的function函数名" + “(” + "参数, 参数, ..." + ") + ":冒号" 结束；
    ###以下缩进模块是函数主体function body：
    pi = 3.14159 ###pi引入局部变量，只可以在该函数主体使用；   
    return height * pi * radius ** 2 ###return不是必有项
cylinder_volume(10, 3)  ####function call statement

#Print vs. Return in Functions
# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)
print('Calling show_plus_ten...')
return_value_1 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))


def cylinder_volume2(height, radius=5):###radius默认定义为5；但依然可以重新赋值改变。
   
    pi = 3.14159  
    return height * pi * radius ** 2 

print(cylinder_volume(10, 7))##不额外赋值，默认为5;赋值为7，覆盖默认值5;按位置接受参数：pass in arguments by position
print(cylinder_volume(height=10, radius=7))                     ##按名称接受参数；pass in arguments by name

#Quiz: Population Density Function

# write your function here
def population_density(population, land_area):
    return population / land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# Quiz: readable_timedelta

# write your function here
def readable_timedelta(n):   
    return '{} week(s) and {} day(s)'.format(n//7, n%7)

# test your function
print(readable_timedelta(10))

##udacity solution:
def readable_timedelta2(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta2(10))


# Variable Scope


word = "hello"

def some_function():
    print(word)
some_function()

##QUIZ QUESTION


def buy_eggs(n):
    egg_count = 0
    egg_count += 12 # purchase a dozen eggs

print(buy_eggs(10))

#QUESTION 1 OF 5
str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

##QUESTION 2 OF 5
str1 = 'Functions are important programming concepts.'

def print_fn2():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn2()

##QUESTION 3 OF 5
def print_fn3():
    str1 = 'Variable scope is an important concept.'
    print(str1)

#print_fn3(str1)   #### As long as the function definition did not include any arguments, 
                  #### the function call written as print_fn(str1) will give an error as it was not seeking an argument.


##QUESTION 4 OF 5
str1 = 'Functions are important programming concepts.'

def print_fn4():
    print(str1)

#print_fn4(str1)   #### As long as the function definition did not include any arguments, 
                  #### the function call written as print_fn(str1) will give an error as it was not seeking an argument.


#Quiz: Write a Docstring
# Docstring:以  “““  开头
def readable_timedelt(n):
    # insert your docstring here
    """ Define readable_timedelt function
    INPUT:
    Args:
        days (int): number of days to convert
    OUTPUT:
    () week(s) and () day(s)
    """
    weeks = n // 7
    remainder = n % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


#lambda Expressions:精简
def double(x):
    return x * 2
"""以下为对等的lambda表达式"""
doubel = lambda x: x * 2

#Quiz: Lambda with Map
"""map() is a higher-order built-in function that takes a function and iterable as inputs, 
and returns an iterator that applies the function to each element of the iterable. 
The code below uses map() to find the mean of each list in numbers to create the list averages. 
Give it a test run to see what happens.

Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map()."""

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

#def mean(num_list):
#    return sum(num_list) / len(num_list)

#averages = list(map(mean, numbers))
averages = list(map(lambda num: sum(num) / len(num), numbers))
print(averages)




# Quiz: Lambda with Filter
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
#    return len(name) < 10

#short_cities = list(filter(is_short, cities))
"""Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().
OUTPUT:
['Chicago', 'Denver', 'Boston']
"""
short_cities = list(filter(lambda city: len(city) < 10, cities))
print(short_cities)


##