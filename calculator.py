# Imports time module

import time

# Program that executes basic math operations based on user input

print('Addition: +')
print('Subtraction: -')
print('Multiplication: *')
print('Division: /')
print('Type "Quit" to exit the program')
# The code above shows the operations and its respective symbols



selectOption = 'None'

while selectOption.lower() != 'quit':
    
    selectOption = input('Type the operation symbol to select an option: ')
    print()
    if selectOption.lower() == 'quit':
        break
    
    number1 = float(input('Insert a number: '))
    number2 = float(input('Insert another number: '))
    print()
    if selectOption == '+':
        add = number1 + number2
        print('{} + {} is equal to {:.2f}'.format(number1, number2, add))
    elif selectOption == '-':
        sub = number1 - number2
        print('{} - {} is equal to {:.2f}'.format(number1, number2, sub))
    elif selectOption == '*':
        mult = number1 * number2
        print('{} * {} is equal to {:.2f}'.format(number1, number2, mult))
    elif selectOption == '/':
        div = number1 / number2
        print('{} / {} is equal to {:.2f}'.format(number1, number2, div))
    else:
        print('Unavailable option')
    print()
# This part of the code creates a loop and checks which option was selected and performs the calculation, therefore, showing the results

print('End of the program')

time.sleep(1)
