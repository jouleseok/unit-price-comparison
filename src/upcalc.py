#upcalc.py

'''''''''''''''''''''''''''''''''''''''''''''''''''''
Developed by Juliana Seok (https://github.com/jouleseok)
Start date: July 31, 2025
Purpose: An app for comparing the unit price of grocery store items
    especially when unit conversion is required, e.g:
    $/lb vs $/kg
*** This version is for text/console interface.
'''''''''''''''''''''''''''''''''''''''''''''''''''''

def ConvertToPerGrams(unit, value):
    convFactor = 1.0
    if unit == "a": # $/kg
        convFactor = 1000
    elif unit == "c": # $/lb
        convFactor = 453.592
    elif unit == "d": # $/oz
        convFactor = 28.3495
    elif unit != "b":
        print("Error: not a valid unit")

    converted = value / convFactor
    return converted
    

def PerWeightFunc():
    name1 = input("Enter a one-word descriptor for the FIRST option:")
    print(f"Select the units of \'{name1}\':")
    print("a) $/kg")
    print("b) $/g")
    print("c) $/lb")
    print("d) $/oz")
    unit1 = input() #add while loop for input validity here
    value1_str = input(f"Now enter the value of the unit price for \'{name1}\':")
    value1_float = float(value1_str)
    
    name2 = input("Enter a one-word descriptor for the SECOND option:")
    print(f"Select the units of \'{name2}\':")
    print("a) $/kg")
    print("b) $/g")
    print("c) $/lb")
    print("d) $/oz")
    unit2 = input() #add while loop for input validity here
    value2_str = input(f"Now enter the value of the unit price for \'{name2}\':")
    value2_float = float(value2_str)

    converted1 = ConvertToPerGrams(unit1, value1_float)
    converted2 = ConvertToPerGrams(unit2, value2_float)

    if converted1 < converted2:
        print(f"RESULT: {name1} is the cheaper option (${converted1}/g vs ${converted2}/g).")
    elif converted > converted2:
        print(f"RESULT: {name2} is the cheaper option (${converted2}/g vs ${converted1}/g).")
    else:
        print(f"RESULT: Both options have the same effective unit price (${converted1}/g).")
    

print("Welcome to jouleseok's unit price comparison app!")
print("Is your comparison for price per a) weight/mass OR b) quantity?")
choice1 = input()
if choice1 == "a":
    print("We are in (a).")
    PerWeightFunc()
elif choice1 == "b":
    print("We are in (b).")
else:
    print("We are in uncharted territory.")


print("End of program")

