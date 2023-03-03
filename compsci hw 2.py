#Rosemary Hoffman Hw 2
#problem 1
def print_name(name):
    print("the name is", name)
print_name("Rosemary")
#problem 2
def ninety(a,b,c,):
    d=90*4 a-b-c
    return d
print(ninety(2,3,4))

#problem 3
def miles_per_hour(miles, hours, minutes, seconds):
    a=miles
    b=hours
    c=minutes/60
    d=seconds/3600
    speed=a/(b+c+d)
    return speed
print(miles_per_hour(20,2,21,16))
#problem 4
def greeting(name):
    if name=="Chris":
        print("Hello Chris")
    else:
        print("Goodbye", name)
greeting("Chris")
greeting("Rosemary")
#problem 5
def convert_temperature(temp, units):
    if units=="celsius":
        value=temp*(9/5 +32)
        return value
    elif units=="fahrenheit":
        value=(5/9)*(temp-32)
        return value
print(convert_temperature(1, "celsius"))
print(convert_temperature(1, "fahrenheit"))
#problem 6
def calculate_grade(score):
    if 90<=score:
        return "A"
    if 80<=score<90:
        return "B"
    if 70<=score<80:
        return "C"
    if 60<=score<70:
        return "D"
    if score<60:
        return "F"
print(calculate_grade(85))
print(calculate_grade(95))
print(calculate_grade(75))
print(calculate_grade(65))
print(calculate_grade(55))
