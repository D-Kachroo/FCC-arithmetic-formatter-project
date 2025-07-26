def arithmetic_arranger(problems, solve=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        first = parts[0]
        operator = parts[1]
        second = parts[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            answer = str(int(first) + int(second))
        else:
            answer = str(int(first) - int(second))

        length = max(len(first), len(second)) + 2
        top = first.rjust(length)
        bottom = operator + second.rjust(length - 1)
        dash = "-" * length
        ans = answer.rjust(length)

        if i > 0:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            answers += "    "

        first_line += top
        second_line += bottom
        dashes += dash
        answers += ans

    if solve:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes + "\n" + answers
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes

    return arranged_problems
