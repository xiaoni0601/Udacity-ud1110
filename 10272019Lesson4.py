# Quiz: Using Truth Values of Objects
# You will use a new variable prize to store a prize name if one was won, 
# and then use the truth value of this variable to compose the result message. 
# This will involve two if statements.

points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = 'wooden rabbit'
elif points >= 151 and points <= 180:
    prize = 'wafer-thin mint'
elif points >= 181 and points <= 200:
    prize = 'penguin'
     

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)