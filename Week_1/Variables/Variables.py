#################################
# Working with Python variables #
#################################

#Letters, numbers and underscore
#Begins with letter or underscore
#Case-sensitive

#Variable = value (== is quality testing while = is assignment)

##############################
# Basic Variable Assignments #
##############################

my_name = "Ryan Schachte" #Declaring string variable
my_age = 19 #Declaring integer variable

print my_name
print my_age

my_age = my_age + 1
print my_age

my_age += 1
print my_age

###########################
# Temp Conversion Example #
###########################

##############################
#Converting from F to C
#c = 5/9 * (f-32)
##############################

temp_Fahr = 212
temp_Cels = 5.0/9.0 * (temp_Fahr-32)

print temp_Cels

##############################
#Converting from C to F
#c = 9/5 * C + 32
##############################

temp_Cels = 0
temp_Fahr = 9.0/5.0 * temp_Cels + 32

print temp_Fahr

