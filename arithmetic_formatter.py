def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(width) + '    '
        second_line += operator + ' ' + num2.rjust(width - 2) + '    '
        dash_line += '-' * width + '    '

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            answer_line += result.rjust(width) + '    '

    arranged_problems += first_line.rstrip() + '\n'
    arranged_problems += second_line.rstrip() + '\n'
    arranged_problems += dash_line.rstrip() + '\n'

    if show_answers:
        arranged_problems += answer_line.rstrip() + '\n'

    return arranged_problems.rstrip()


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))