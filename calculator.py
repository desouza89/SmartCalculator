K = {}

operands = {'+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 0,
            ')': 0}


def convert_infix(infix):
    infix = infix.replace('(', '( ').replace(')', ' )')
    if infix.count('(') != infix.count(')') or infix.count('*') > 2 or infix.count('//') > 1:
        return print('Invalid expression')
    Stack = []
    postfix = ''
    for i in infix.split():
        if i in operands.keys():
            # № 2,3
            if not Stack or Stack[-1] == '(' or operands[i] > operands[Stack[-1]]:
                Stack.append(i)
            # № 4
            while operands[i] < operands[Stack[-1]]:
                postfix += Stack.pop() + ' '
                if not Stack or Stack[-1] == ')':
                    Stack.append(i)
                    break
        # № 5, 6
        elif i == '(':
            Stack.append(i)
        elif i == ')':
            while Stack[-1] != '(':
                postfix += Stack.pop() + ' '
            Stack.remove('(')

        else:
            postfix += i + ' '

    while Stack:
        postfix += Stack.pop() + ' '

    return postfix


def calculate_post(postfix):
    postfix = str(postfix)
    Stack = []
    for i in postfix.split():
        if i.isdigit():
            Stack.append(i)
        elif i in K:
            Stack.append(K[i])
        elif i in operands.keys():
            sec, first = Stack.pop(), Stack.pop()
            result = eval(str(first) + i + str(sec))
            Stack.append(result)

    return round(Stack[-1]) if Stack else 0


def assignment(income):
    income = income.replace(' ', '')
    t = income.split('=')

    if not t[0].isalpha():
        return print('Invalid identifier')

    elif t[1] not in K and t[1].isalpha():
        return print('Unknown variable')

    elif not t[1].isalpha() and not t[1].isdigit() or len(t) > 2:
        return print('Invalid assignment')

    if t[1] in K:
        K[t[0]] = K[t[1]]
    else:
        K[t[0]] = t[1]


def printer(income):
    t = income.split()

    try:
        print(K[t[0]])
    except KeyError:
        print('Unknown variable')


def replace(income):
    for i in income:
        if i.isalpha():
            try:
                income = income.replace(i, K[i])
            except KeyError:
                return print("Unknown variable")

    return print(round(eval(income)))


while True:
    inp = input()
    operation = ["+", "-", "*", "/"]
    if not inp:
        continue
    elif '=' in inp:
        assignment(inp)
    elif '+' in inp or '-' in inp or '*' in inp or '/' in inp:
        if '/help' in inp:
            print('The program calculates the sum, subtraction, multiplication of numbers')
            continue
        elif '/exit' in inp:
            print("Bye!")
            break
        elif '/start' in inp:
            print("Unknown command")
            continue
        try:
            if inp.count('/') > 1:
                print('Invalid expression')
                continue
            print(eval(inp))
        except NameError:
            replace(inp)
        except SyntaxError:
            calculate_post(convert_infix(inp))
    else:

        printer(inp)
