
'''Lambda Functions in Python
------------------------------
# A **lambda function** is a small, anonymous function used for simple operations.

Syntax
lambda Arguments : expressions

'''
#EX:
square = lambda x: x*x
print(square(5))

''' 1. Lambda with Multiple Arguments'''

add = lambda a, b: a + b
print(add(10, 20))

''' 2. Lambda with Condition'''

check_condition = lambda x: "Even" if x % 2 == 0 else "Odd" 
print(check_condition(10))

''' 3. Lambda with `map()`
#map() applies a function to every item.
'''

Numbers = [1,2,3,4]

squares = list(
    map(lambda x: x*x , Numbers)
    )
print(squares)

'''Real-world example: Add tax'''

prices = [100, 200, 500]

final_prices = list(
    map(lambda price: price * 1.18, prices)
)

print(final_prices)

'''
## 4. Lambda with `filter()`

`filter()` selects items based on a condition.

'''
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

'''
### Real-world example: Passing students

'''
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 35},
    {"name": "Charlie", "marks": 70}
]

passed = list(
    filter(
        lambda student: student["marks"] >= 40,
        students
    )
)

'''
## 5. Lambda with `sorted()`

`lambda` is commonly used to define the sorting rule.

### Sort words by length

'''
words = ["apple", "kiwi", "banana", "fig"]

result = sorted(
    words,
    key=lambda word: len(word)
)
'''
### Sort students by marks
'''
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 70},
    {"name": "Charlie", "marks": 95}
]

result = sorted(
    students,
    key=lambda student: student["marks"]
)
'''
 Sort from highest to lowest
'''
result = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)
'''
## 6. Lambda with `reduce()`
`reduce()` combines all items into one result.
from functools import reduce

'''
numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)
print(total)
# 15
