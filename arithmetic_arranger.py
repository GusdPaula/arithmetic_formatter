def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    arranged_problems = []

    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    a = 0
    b = 0
    r = 0
    
    for index, value in enumerate(problems):
        
        # ['32', '+', '8']
        operation = value.split(' ')
        if operation[1] not in '+-':
            return "Error: Operator must be '+' or '-'."

        try:
            value_1 = int(operation[0])
            value_2 = int(operation[2])

        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        if len(operation[0]) > 4 or len(operation[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'


        # calculate the lenght of each line
        longest_val = max(len(operation[0]), len(operation[2]))

        width = longest_val + 2

        # ['32', '+', '8']
        L1 = f"{operation[0]:>{width}}"
        L2 = operation[1] + f"{operation[2]:>{width - 1}}"
        d = '-'*width
        a = f"{int(operation[0]) + int(operation[2]):>{width}}"
        b = f"{int(operation[0]) - int(operation[2]):>{width}}"

        if args:
            if operation[1] == '+':
                r = a
            else:
                r = b

        line_1.append(L1)
        line_2.append(L2)
        line_3.append(d)
        line_4.append(r)

        
        # generate the corret number od dashes below the problem statment
        # append the answer if necessary
    if len(line_1) == 1:
        r_line_1 = f'{line_1[0]}'
        r_line_2 = f'{line_2[0]}'
        r_line_3 = f'{line_3[0]}'
        if args:
            r_line_4 = f'{line_4[0]}'
    
    elif len(line_1) == 2:
        r_line_1 = f'{line_1[0]}    {line_1[1]}'
        r_line_2 = f'{line_2[0]}    {line_2[1]}'
        r_line_3 = f'{line_3[0]}    {line_3[1]}'
        if args:
            r_line_4 = f'{line_4[0]}    {line_4[1]}'
    
    elif len(line_1) == 3:
        r_line_1 = f'{line_1[0]}    {line_1[1]}    {line_1[2]}'
        r_line_2 = f'{line_2[0]}    {line_2[1]}    {line_2[2]}'
        r_line_3 = f'{line_3[0]}    {line_3[1]}    {line_3[2]}'
        if args:
            r_line_4 = f'{line_4[0]}    {line_4[1]}    {line_4[2]}'
    
    elif len(line_1) == 4:
        r_line_1 = f'{line_1[0]}    {line_1[1]}    {line_1[2]}    {line_1[3]}'
        r_line_2 = f'{line_2[0]}    {line_2[1]}    {line_2[2]}    {line_2[3]}'
        r_line_3 = f'{line_3[0]}    {line_3[1]}    {line_3[2]}    {line_3[3]}'
        if args:
            r_line_4 = f'{line_4[0]}    {line_4[1]}    {line_4[2]}    {line_4[3]}'

    elif len(line_1) == 5:
        r_line_1 = f'{line_1[0]}    {line_1[1]}    {line_1[2]}    {line_1[3]}    {line_1[4]}'
        r_line_2 = f'{line_2[0]}    {line_2[1]}    {line_2[2]}    {line_2[3]}    {line_2[4]}'
        r_line_3 = f'{line_3[0]}    {line_3[1]}    {line_3[2]}    {line_3[3]}    {line_3[4]}'
        if args:
            r_line_4 = f'{line_4[0]}    {line_4[1]}    {line_4[2]}    {line_4[3]}    {line_4[4]}'
    
    arranged_problems.append(r_line_1)
    arranged_problems.append(r_line_2)
    arranged_problems.append(r_line_3)
    if args:
        arranged_problems.append(r_line_4)

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}\n{arranged_problems[3]}" if args else output

    return output
