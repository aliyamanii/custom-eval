operators = {"&": lambda a, b: a and b,
             "|": lambda a, b: a or b,
             ">": lambda a, b: (not a) or b,
             "#": lambda a, b: a == b}


def evaluate(expression):
    expression = expression.replace(' ', '')
    print(expression)
    feed = None
    operate = False
    operator = None
    index = 0
    count = 0
    for i, char in enumerate(expression):
        if char == '(':
            if not operate:
                operate = True
                index = i
            count += 1

        if char == ')':
            count -= 1

        if count != 0:
            continue

        if operate:
            operate = False
            exp = evaluate(expression[index + 1:i])
            feed = exp if feed is None else operator(feed, exp)

        if char in operators.keys():
            print(f'Operating "{char}" with the feed of "{feed}"')
            operator = operators[char]

        if char in 'FT':
            exp = char == 'T'
            feed = exp if feed is None else operator(feed, exp)

    return feed


userInput = input("Please enter your logical expression: \n").upper()
print("The value of the expression is:", evaluate(userInput))
