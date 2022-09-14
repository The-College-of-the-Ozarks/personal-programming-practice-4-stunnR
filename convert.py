# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")

# ensures user enters numeric value
try:
    mph = float(mph)
except:
    print("Invalid input. Only numeric input is accepted.")
    exit()

# prints menu of function choices
print("1: Convert to kph")
print("2: Convert to m/s")
print("3: Convert to ft/s")
choice = input("Please enter the number of the function you would like to use: ")

# outputs appropriate converted value, or exits if invalid input was given
if choice == '1':
    print("Speed in kph is", mph_to_kph(mph))
elif choice == '2':
    print("Speed in m/s is", mph_to_ms(mph))
elif choice == '3':
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print("Input given was not a menu choice.")
