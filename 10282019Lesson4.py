# for_loop
# 1. 从list列表中提取信息:
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title()) 

# 2. 创建新的list列表
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []   #从空list列表[]开始
for city in cities:
    capitalized_cities.append(city.title())  #结合append()添加新item项
print(capitalized_cities) 


#3. 修改list列表：内置函数range(start,stop,step)；start 默认为0； step默认为1；
print(range(4))

for number in range(4):
    print(number)

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)  # 课程中这里的print与上一行加tab键平齐，是错的；tab结果是将结果重复range里面的次数



# Practice: Quick Brown Fox
# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)


# Practice: Multiples of 5
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for i in range(5, 31, 5):
    print(i)

# Quiz: Create Usernames
# HINT: Use the .replace() method to replace the spaces with underscores. 
# Check out how to use this method in this Stack Overflow answer.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)  # output 依然是原names

# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to modify the list.
# 大写换小写；空格换下滑键。

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)


# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
# XML is a data language similar to HTML. 
# You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
# Keep track of the number of tags using the variable count.
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in tokens:
    if '<' in i and '>' in i: # or if i[0] == '<' and i[-1] == '>':
        count += 1

print(count)


# Quiz: Create an HTML List

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)



# Iterating Through Dictionaries with For Loops
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)


# cast = {
#           "Jerry Seinfeld": "Jerry Seinfeld",
#           "Julia Louis-Dreyfus": "Elaine Benes",
#          "Jason Alexander": "George Costanza",
#            "Michael Richards": "Cosmo Kramer"
# for key, value in cast.items():
#   print("Actor: {}  Role: {}".format(key, value))



# Quiz: Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

    
###更简单的代码，自己想的：
#Iterate through the dictionary
for key, value in basket_items.items():
#if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
       result += value

print(result)

# Quiz: Fruit Basket - Task 2

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value 
print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value 
print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value 
print(result)




## Quiz: Fruit Basket - Task 3
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    
#if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count += value
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count +=value

print(fruit_count, not_fruit_count)


# Practice: Factorials with While Loops

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)


# Practice: Factorials with For Loops

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for number in range(2, number + 1):
    product = product * number

# print the factorial of number
print(product)


# Quiz: Count By
start_num = 123 #provide some start number
end_num = 1001 #provide some end number that you stop when you hit
count_by = 39 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by 

print(break_num)


# Quiz: Count By Check

start_num = 123 #provide some start number
end_num = 1002 #provide some end number that you stop when you hit
count_by = 29 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
    
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by 
result = break_num
print(result)


#Quiz: Nearest Square

limit = 40

num = 0
while (num+1) ** 2 < limit:
    num += 1
nearest_square = num**2  # 此处即为result

print(nearest_square)



### For Loops Vs. While Loops
# for loops are ideal when the number of iterations is known or finite.
# while loops are ideal when the iterations need to continue until a condition is met.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))