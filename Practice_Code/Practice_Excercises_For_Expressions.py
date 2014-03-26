######################################
# Practice exercises for expressions #
######################################

import math

#1) There are 5280 feet in a mile. Write a Python statement that calculates and prints the number of feet in 13 miles.

feet_in_mile = 5280

num_of_miles = 13

total_feet = feet_in_mile*num_of_miles

print total_feet

#2) Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds.

hours = 7
minutes = 21
seconds = 37

hours_to_seconds = hours*60*60
minutes_to_seconds = minutes*60

total_seconds = hours_to_seconds+minutes_to_seconds+seconds

print total_seconds

#3) The perimeter of a rectangle is 2w+2h, where w and h are the lengths of its sides. Write a Python statement that calculates and prints the length in inches of the perimeter of a rectangle with sides of length 4 and 7 inches.

#Equation for perimeter of rectangle = 2w + 2h

w = 7
l = 4

rect_perim = 2*w + 2*l

print rect_perim

#4) The area of a rectangle is wh, where w and h are the lengths of its sides. Note that the multiplication operation is not
#   shown explicitly in this formula. This is standard practice in mathematics, but not in programming. Write a Python statement that calculates
#   and prints the area in square inches of a rectangle with sides of length 4 and 7 inches.

w = 4
l = 7

rect_area = w * l

print rect_area

#5) The circumference of a circle is 2pir where r is the radius of the circle. 
#   Write a Python statement that calculates and prints the circumference in inches of a circle whose radius is 8 inches. Assume that the constant pi=3.14.

circle_radius = 8
pi_constant = 3.14

circle_circum = pi_constant * circle_radius * 2

print circle_circum

#6) The area of a circle is pir2 where r is the radius of the circle. (The raised 2 in the formula is an exponent.)
#   Write a Python statement that calculates and prints the area in square inches of a circle whose radius is 8 inches. Assume that the constant pi=3.14.

circle_radius = 8 
pi_constant = 3.14

circle_area = pi_constant * (circle_radius**2)

print circle_area

#7) Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is p(1+0.01r)y.
#   Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10 years.

# p = dollars
# r = % interest
# y = years

p = 1000
r = 7
y = 10

value = p*(1+.01 * r) ** y

print value

#8) Write a single Python statement that combines the three strings "My name is", "Joe" and "Warren" 
#  (plus a couple of other small strings) into one larger string "My name is Joe Warren." and prints the result.

welcome = "My name is"
first_name = "Joe"
last_name = "Warren"

print welcome + " " + first_name + " " + last_name + "."

#9) Write a Python expression that combines the string "Joe Warren is 52 years old." 
#   from the string "Joe Warren" and the number 52 and then prints the result (Hint: Use the function str to convert the number into a string.)

name = "Joe Warren"
age = 52

print name + " is " + str(age) + " years old."

#10) The distance between two points (2,2) & (5,6)

x1 = 2
x2 = 5
y1 = 2
y2 = 6

equation = ((x1-x2)**2) + ((y1-y2)**2)
final_eq = math.sqrt(equation)
final_eq = int(final_eq)
print str(final_eq) + " is the distance between the two points!"