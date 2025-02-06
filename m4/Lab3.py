# Lab 3 Module 4
import math

result = 0
iterations = 0
total_sum = 0

while True:
    print(f'Current result: {result}\n\nCalculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n')
    selection = int(input('Enter Menu Selection: '))
    if selection in range(0,7):
        if selection == 0:
            print('Thanks for using this calculator. Goodbye!')
            break
        op1 = input('Enter first operand: ')
        op2 = input('Enter second operand: ')
        if selection == 1: # addition logic
            if op1 == 'RESULT':
                result = result + float(op2)
            elif op2 == 'RESULT':
                result = result + float(op1)
            else: result = float(op1) + float(op2)
        elif selection == 2: # subtraction logic
            if op1 == 'RESULT':
                result = result - float(op2)
            elif op2 == 'RESULT':
                result = result - float(op1)
            else: result = float(op1) - float(op2)
        elif selection == 3: # multiplication logic
            if op1 == 'RESULT':
                result = result * float(op2)
            elif op2 == 'RESULT':
                result = result * float(op1)
            else: result = float(op1) * float(op2)
        elif selection == 4: # division logic
            if float(op2) == 0:
                print('Error: invalid input!')
                break
            elif op1 == 'RESULT':
                result = result / float(op2)
            elif op2 == 'RESULT':
                result = result / float(op1)
            else: result = float(op1) / float(op2)
        elif selection == 5: # exponentiation logic
            if op1 == 'RESULT':
                result = result ** float(op2)
            elif op2 == 'RESULT':
                result = result ** float(op1)
            else: result = float(op1) ** float(op2)
        elif selection == 6: # logarithm logic
            if op1 == 'RESULT':
                result = math.log(float(op2), result)
            elif op2 == 'RESULT':
                result = math.log(float(op1), result)
            else: result = math.log(float(op2), float(op1))
    elif selection == 7: # averages logic
        if iterations >= 1:
            average = total_sum / iterations
            print(f'Sum of calculations: {result}\nNumber of calculations: {iterations}\nAverage of calculations: {average:.2f}')
            iterations -= 1
    else:
        print('Invalid selection.')
        break
    total_sum += result
    iterations += 1
