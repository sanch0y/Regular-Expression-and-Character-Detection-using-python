#Self Made Stack#
class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, val):
        self.items.append(val)
        self.length += 1
        # print(" ")
        # print(" stackval ",val)

    def pop(self):
        if self.empty():
            return None
        self.length -= 1
        return self.items.pop()

    def size(self):
        return self.length

    def peek(self):
        if self.empty():
            return None
        # print(" lastVal ", self.items[-1])
        return self.items[-1]

    def empty(self):
        return self.length == 0

    def __str__(self):
            return str(self.items)
#Stack Ends#




#Dictionary of Precidence#
precedence = {}
precedence['*'] = 3
precedence['/'] = 3
precedence['+'] = 2
precedence['-'] = 2
precedence['('] = 1




#After giving input code Executes from here#
def convert(expression):
    chek = True
    counterForIdentifier = 0
    CalcExpr = []
    CalcuOpstack = Stack()

    FinalExpr = __convert(expression.split())
    print(" *finalEXpression* ", FinalExpr)

    for i in onlyIdentifier:
        for j in FinalExpr:
            if(j.isidentifier() and  i != j):
                # print("i : ",i)
                # print("j : ",j)
                chek = False
            elif(j.isidentifier() and  i == j):
                # print("i else : ", i)
                # print("j else : ", j)
                chek = True
    if(chek==False):
        print("COMPILATION ERROR")
    else:
        # print("MATCHED")
        for i in FinalExpr:
            for index, j in enumerate(onlyIdentifier):
                if (i.isidentifier() and i == j):
                    CalcExpr.append(onlyVal[index])
                elif (i == '+' or i == '-' or i == '*' or i == '/'):
                    if(counterForIdentifier == 0):
                        CalcExpr.append(i)
                        counterForIdentifier = 1
            counterForIdentifier = 0
    print(" *calcuEXpression* ", CalcExpr)



    # Main Calculation Starts from Here#
    for i in CalcExpr:
        if (i.isdigit()):
            CalcuOpstack.push(i)
        elif(i == '+'):
            operand_1 = int(CalcuOpstack.pop())
            operand_2 = int(CalcuOpstack.pop())
            result = operand_2 + operand_1
            CalcuOpstack.push(result)
        elif(i == '-'):
            operand_1 = int(CalcuOpstack.pop())
            operand_2 = int(CalcuOpstack.pop())
            result = operand_2 - operand_1
            CalcuOpstack.push(result)
        elif (i == '*'):
            operand_1 = int(CalcuOpstack.pop())
            operand_2 = int(CalcuOpstack.pop())
            result = operand_2 * operand_1
            CalcuOpstack.push(result)
        elif (i == '/'):
            operand_1 = int(CalcuOpstack.pop())
            operand_2 = int(CalcuOpstack.pop())
            result = operand_2 / operand_1
            CalcuOpstack.push(result)
    #Final Result#
    print("FINAL RESULT : ",CalcuOpstack.pop())




#Main Algorithm Starts from Here#
def __convert(tokens):
    postfix = []
    opstack = Stack()

    for token in tokens:
        # print("--------------")
        # print("Token : ",token)
        # print("--------------")
        if token.isidentifier():
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            while True:
                temp = opstack.pop()
                if temp is None:
                    break
                elif temp == '(':
                    break
                elif not temp.isidentifier():
                    postfix.append(temp)
        else:  # must be operator
            if opstack.empty():
                opstack.push(token)
            elif opstack.peek() == '(':
                opstack.push(token)
            elif (precedence[token] > precedence[opstack.peek()]):
                opstack.push(token)
            elif (precedence[token] <= precedence[opstack.peek()]):
                # print("####################################### Checking Peek Inside The Condition: ", opstack.peek())
                p = opstack.pop()
                # print("*************************************** Checking Pop : ", p)
                postfix.append(p)
                opstack.push(token)
                # print("===================")
                # print("POSTFIX : ", postfix)
                # print("===================")
    #When There is No Input#
    while not opstack.empty():
        postfix.append(opstack.pop())

    return postfix
#Main Algorithm Ends Here#

# convert("a + b * c")
# convert("a * ( b + c ) + d")
# convert("( a + b - c ) * d - ( e + f )")
# convert("( a + b ) * c - ( d - e ) * ( f + g )")



##Code Starts From Here##
#taking input. Value of alphabets and giving Expressions#
countN = int(input('Give n: '))
identifiersWithVal = []
onlyIdentifier = []
onlyVal = []
expr = []
#code for n#
c1 = 0
while (c1 < countN):
    i = input()
    identifiersWithVal.append(i)
    c1 = c1 + 1

for i in identifiersWithVal:
    identifiersSplit = i.replace('=',' ').split()
    for j in identifiersSplit:
        if(j.isdigit()):
            onlyVal.append(j)
        if(j.isidentifier()):
            onlyIdentifier.append(j)

# print(" *input* ",identifiersWithVal)
# print(" *=* ",identifiersSplit)
# print(" *value* ",onlyVal)
# print(" *identifier* ",onlyIdentifier)

#code for m#
countM = int(input('Give m: '))
c2 = 0
while (c2 < countM):
    i = input()
    expr.append(i)
    convert(i)
    c2 = c2 + 1


