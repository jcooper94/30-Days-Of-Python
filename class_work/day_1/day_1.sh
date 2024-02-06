python3 --version

op1=3
op2=4

function add() {
    #arrithmetic expression double bracces
    echo $(($1 + $2))
}

function subract(){
    echo $(($1 - $2))
}

function multiplication(){
    echo $(($1 * $2))
}

function modulus(){
    echo $(($1 % $2))
}

function division(){
    echo $(($1 / $2))
}

function exponential(){
    echo $(($1 ** $2))
}

exponential $op1 $op2

your_name='jared'
last_name='cooper'
country='united states'
enjoying='i am enjoying 30 days of python in bash'
echo $your_name

# Integer and float variables
integer=5
float=3.14

# Complex number (not directly supported in bash)
# Initializing real numbers
x=5
y=3
# Converting x and y into complex number (not directly supported in bash)
# z=$(echo "$x + $y * i" | bc -l)

# String and boolean variables
string="string"
boolean=false

# List (array) in bash
list=("list" "list1" "list2")

# Tuple (not directly supported in bash)
# Creating a Tuple with the use of an array
tuple=("${list[@]}")

# Set (not directly supported in bash)
# Creating a Set with the use of an array
set1=("${list[@]}")

# Associative array (dictionary) in bash
declare -A my_dictionary
my_dictionary[name]="jared"
my_dictionary[age]="29"
my_dictionary[sound]="ouch"

# Given points
x1=2
y1=3
x2=10
y2=8

# Calculate differences
difference_x=$((x2 - x1))
difference_y=$((y2 - y1))

# Calculate Euclidean distance
distance=$(bc -l <<< "sqrt($difference_x^2 + $difference_y^2)")

echo "The Euclidean distance between the points is approximately $distance units."