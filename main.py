def arithmetic_arranger(problems, show_answers=False):

    #5 problems or less
    if len(problems) > 5:
        return ('Error: Too many problems.')

    #check for + or - by splitting the list
    #search array for index 0
    #check if theres no addition or subtracion
    for problem in problems:
        operator = problem.split()
        if operator[1] not in ['+', '-']:
            return ("Error: Operator must be '+' or '-'.")

    #DIGITS ONLY
    for problem in problems:
        operand_digit_only = problem.split()
        if not (operand_digit_only[0].isdigit() and operand_digit_only[2].isdigit()):
            return ('Error: Numbers must only contain digits.')
    for problem in problems:
        operand = problem.split()        
        if len(operand[0]) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        if len(operand[2]) > 4:
            return ("Error: Numbers cannot be more than four digits.")

    #seperate each line into lists
    top_line = []
    middle_line = []
    dash_line = []
    answer_line = []

    #give each list a value
    for problem in problems:
        parts = problem.split()
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]
    
        #EVALUATE ANSWERS
        if operator == "+":
            answer = int(first_operand) + int(second_operand)
        elif operator == "-":
            answer = int(first_operand) - int(second_operand)
        
        #SET WIDTH
        width = max(len(first_operand), len(second_operand)) + 2

        top_line.append(first_operand.rjust(width))
        middle_line.append(operator + (" " + second_operand).rjust(width - 1)) 
        dash_line.append("-" * width)
        answer_line.append(str(answer).rjust(width))

    arranged_problems = "    ".join(top_line) + "\n" + "    ".join(middle_line) + "\n" + "    ".join(dash_line)

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
