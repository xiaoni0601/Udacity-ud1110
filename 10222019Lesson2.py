# Quiz: Average Electricity Bill
# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23 + 32 + 64) / 3)


# Quiz: Calculate
# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
# Fill this in with an expression that calculates how many tiles are needed.
print(9 * 7 + 5 * 7)

# Fill this in with an expression that calculates how many tiles will be left over.
print(17 * 6 - 9 * 7 - 5 * 7)

# 变量与运算符
# x += 2 等同于 x = x + 2;  x -= 2 等同于 x = x - 2

# Quiz: Assign and Modify Variables
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
# add the rainfall variable to the reservoir_volume variable
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
# decrease reservoir_volume by 5% to account for evaporation
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
# print the new value of the reservoir_volume variable
rainfall = rainfall * 0.9  # 等同于 rainfall *= .9
reservoir_volume = rainfall + reservoir_volume # 等同于 reservoir_volume += rainfall
reservoir_volume = reservoir_volume * 1.05  #等同于 reservoir_volume *= 1.05
reservoir_volume = reservoir_volume * 0.95   #等同于 reservoir_volume *= 0.95
reservoir_volume = reservoir_volume - 2.5e5   #等同于 reservoir_volume -= 2.5e5
print(reservoir_volume)



# Quiz: Changing Variable Values
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
# If we now add this new 5th line of code to the above, what will the output be?
print(crs_per_rab)


# Quiz: Which is denser, Rio or San Francisco?
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# Quiz: Fix the Quote
# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

# Quiz: Write a Server Log Message
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

message = username + ' ' + 'accessed the site' + ' ' + url + ' ' + 'at' + ' ' + timestamp
print(message)

# Quiz: len()
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
name = given_name + ' ' + middle_names + ' ' + family_name
name_length = len(name)
print(name)
# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)



# Quiz: What Type Do These Objects Have?
print(type("12"))
print(type(12.3))
print(type(len("my_string")))
print(type("hippo" *12))


# Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print(total_sales)
total_sales = 'This week\'s total sales: ' + str(total_sales)
print(total_sales)

# Write two lines of code below, each assigning a value to a variable

# format() Practice:
# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
animal = 'dog'
action = 'bite'
print(('does your {} {} ?') .format(animal, action))

# Another important string method: split()
new_str = 'The crow jumped over the moon.'
new_str.split()
new_str.split(' ', 3)
new_str.split('.')
new_str.split(None, 3)


# Quiz: String Methods Coding Practice
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print(len(verse))
print((verse. find('and')))
print((verse.rfind('you')))
print((verse.count('you')))


# Debugging Code:
# Here are some tips on successful debugging that we'll discuss in more detail below:

#----1. Understand common error messages you might receive and what to do about them.
#----2. Search for your error message, using the Web community.
#----3. Use print statements.