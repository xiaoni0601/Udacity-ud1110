#Lesson6
# scripting脚本编写
# To write and run own scripts该lesson6即将学习在自己电脑上编写与运行脚本

how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)



# Quiz: Generate Messages


names = input("Entetr names separated by commas:").title().split(",")
assignments = input("Enter assignment counts separated by commas:").split(",")
grades = input("Enter grades separated by commas:").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
   print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

#Handling Input Errors
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
       num_each = cookies // people
       leftovers = cookies % people
    except ZeroDivisionError:
       print("Oops, you entered 0 people will be attending.")
       print("Please enter a good number of people for a party.")
    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")


############################################################
##卸载anaconda-->重装-->ok