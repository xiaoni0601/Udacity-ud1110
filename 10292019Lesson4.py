# Break, Continue
# Below, you'll find two methods to solve the cargo loading program from the video. 
# The first one is simply the one found in the video, which breaks from the loop when the weight reaches the limit. 
# However, we found several problems with this. 
# The second method addresses these issues by modifying the conditional statement and adding continue. 
# Run the code below to see the results and feel free to experiment!
# 逻辑缜密很重要

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))


# Quiz: Break the String

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        print("current headline: {}".format(headline))
    
print(news_ticker)
print('final result:{}.'.format(news_ticker))


# Coding Quiz: Check for Prime Numbers
# If the numbers are prime, the code should print "[number] is a prime number."
# If the number is NOT a prime number, 
# it should print "[number] is not a prime number", 
# and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num - 1:
            print("{} is a prime number.".format(num))

######## Logic for this solution:
#1. loop through each number in the check_prime list.
#2. Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
#3. Use a conditional statement with themodulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
#4. If we ever find one factor, we can declare that the number is not prime, and state the factor we found. Then we can break out of the loop for that number.
#5. If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime.