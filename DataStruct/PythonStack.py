class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def parchecker(symbolstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isempty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isempty():
        return True
    else:
        return False


def matches(opener, closer):
    opens = "([{"
    closers = ")]}"
    return opens.index(opener) == closers.index(closer)


def baseconverter(decnumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decnumber > 0:
        rem = decnumber % base
        remstack.push(rem)
        decnumber = decnumber // base
    newstring = ""
    while not remstack.isempty():
        newstring = newstring + digits[remstack.pop()]
    return newstring


def infixtopostfix(infixexpr):
    prec = dict()
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split()
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isempty()
                   ) and prec[opstack.peek()] >= prec[token]:
                postfixlist.append(opstack.pop())
            opstack.push(token)
    while not opstack.isempty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)


def postfixeval(postfixexpr):
    operandstack = Stack()
    tokenlist = postfixexpr.split()
    for token in tokenlist:
        if token in "0123456789":
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = domath(token, operand1, operand2)
            operandstack.push(result)
    return operandstack.pop()


def domath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2


print(postfixeval('7 8 + 3 2 + /'))
