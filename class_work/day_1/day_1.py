import os

os.system("python --version")

op1 = 3
op2 = 4

def add(op1, op2):
    return op1 + op2

def subtract(op1, op2):
    return op1 - op2

def multiplication(op1, op2):
    return op1 * op2

def modulus(op1, op2):
    return op1 % op2

def division(op1, op2):
    return op1 / op2

def exponential(op1, op2):
    return op1 ** op2

def floor_division(op1, op2):
    return op1 // op2

your_name = 'jared'
last_name = 'cooper'
country = 'united states'
enjoying = 'i am enjoying 30 days of python'

print(
    type(10),
    type(9.8),
    type(3.14),
    type(4-4j),
    type(['Asabeneh', 'Python', 'Finland']),
    type(your_name),
    type(last_name),
    type(country),
    type(enjoying)
)

#examples

integer = 5
float = 3.14

#COMPLEX NUMBER
# Initializing real numbers
x = 5
y = 3
# converting x and y into complex number
z = complex(x,y)

string = 'string'
boolean = False
list = ['list','list1','list2']

#TUPLE
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

#SET
# Creating a Set with
# the use of a List
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)

my_dictionary = {
    'name':'jared',
    'age':'29',
    'sound':'ouch'
}

# Given points
x1, y1 = 2, 3
x2, y2 = 10, 8

# Calculate differences
difference_x = x2 - x1
difference_y = y2 - y1

# Calculate Euclidean distance
distance = (difference_x**2 + difference_y**2)**0.5

print(f"The Euclidean distance between the points is approximately {distance:.2f} units.")