# Iterators and Generators
# 学习使用生成器创建迭代器（迭代器表示数据流的对象）
def my_range(x):#my_range()这里不是普通的函数，而是一个生成器函数，能够生成0到x-1的数字流
    i = 0
    while i < x:
        yield i ##yield使得函数一次返回一个值；每次被调用时，从停下的位置继续
        i += 1
print(my_range(4))
for n in my_range(4):
    print(n)


##Quiz: Implement my_enumerate
"""Write your own generator function that works like the built-in function enumerate.
OUTPUT:
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
"""

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1 
    # Implement your generator function here


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

"""
If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), 
being able to take and use chunks of it at a time can be very valuable.
Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.
OUTPUT:
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
"""


#Quiz: Chunker

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))


# Generator Expressions
"""
Here's a cool concept that combines generators and list comprehensions! 
You can actually create a generator in the same way you'd normally write a list comprehension, except with parentheses instead of square brackets.
"""
sq_list = [x**2 for x in range(10)]  # this produces a list of squares，这里是方括号，得到list列表。
print(sq_list[2])####OUTPUT:4
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares，这里是圆括号，得到生成器。
print(sq_iterator) ###OUTPUT:<generator object <genexpr> at 0x106999e50>