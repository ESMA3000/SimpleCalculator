import re
import math

def add(operand_A, operand_B):
    return float(operand_A) + float(operand_B)

def subtract(operand_A, operand_B):
    return float(operand_A) - float(operand_B)

def multiply(operand_A, operand_B):
    return float(operand_A) * float(operand_B)

def divide(operand_A, operand_B):
    return float(operand_A) / float(operand_B)

def Calcutor(user_string):

    try:
        if not re.match("[0-9\-*+.@!l%\&]", user_string):
            return None

        operator_list = re.findall("[/\-*+%\&@!l]", user_string)
        operator = operator_list[0]

        operands_array = user_string.split(operator)

        if operands_array[0] is "":
            operands_array.pop(0)

        if len(operands_array) is 2 and re.match("[/\-*+%\&]", operator) != None:

            if operator is "*":
                return multiply(operands_array[0], operands_array[1])

            if operator is "+":
                return add(operands_array[0], operands_array[1])

            if operator is "-":
                return subtract(operands_array[0], operands_array[1])
            
            if operator is "%":
                return math.fmod(float(operands_array[0]), float(operands_array[1]))

            if operator is "&":
                return math.gcd(int(operands_array[0]), int(operands_array[1]))

            if operator is "/" and float(operands_array[1]) != 0:
                return divide(operands_array[0], operands_array[1])
            
            else: 
                return print("Cannot divide by 0")
        
        elif len(operands_array) is 1 and re.match("[@!*+\-/l]", operator) != None:

            if operator is "l":
                return math.log(float(operands_array[0]), 2)

            if operator is "@":
                return math.sqrt(float(operands_array[0]))

            if operator is "!":
                return math.factorial(float(operands_array[0]))
                
            if operator is "*":
                return multiply(operands_array[0], operands_array[0])

            if operator is "+":
                return add(operands_array[0], operands_array[0])

            if operator is "-":
                return subtract(operands_array[0], operands_array[0])

            if operator is "/" and float(operands_array[0]) != 0:
                return divide(operands_array[0], operands_array[0])

            else:
                return print("Cannot divide by 0")

        else:
            return None

    except:
        return None

def interface():

    print("[ESMA©]****************Calculator****************[ESMA©]\nYou can do two operands and one operator (2+2) or one operator and one operand (@16).\nAvalible operators: + - * /\n% = modulus\n@ = squareroot\n! = factorial\nl = log_2\n& = greatest common divisor\nPress q to exit the program :)")
    
    loop_con = True
    while (loop_con):

        user_input = input("\nYour input: ")

        if user_input is "q":
            loop_con = False
            break

        result = Calcutor(user_input)

        if result != None:
            print("\n" + user_input + " =", Calcutor(user_input))
        else:
            print("\nIncorret input. Try again!")

interface()

