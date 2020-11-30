# THE FOLLOWING CODE CONVERTS INFIX EXPRESSIONS TO POSTFIX AND EVALUATES FINAL POSTFIX EXPRESSION

#       Translation Scheme
#        E -> E+T | E-T | T
#        T -> T*F | T/F | F
#        F -> Digit | (E)
#        Digit -> "0-9"
#        precedence: "*,/" > "+,-"

#       left recursion elimination
#       E -> TE'
#       E' -> +TE' | -TE' | Σ
#       T -> FT'
#       T' -> *FT' | / FT' | Σ
#       F -> digit | (E)


#   Implementation

def match(newterm):                     # GOES TO THE NEXT INDEX AND STORES INTO LOOKAHEAD
    global indx, lookahead
    if newterm == lookahead:
        indx += 1
        lookahead = expression[indx]


#   CHECKS IF THE CHARACTER IS DIGIT
def termCharacter():
    if lookahead.isdigit():
        # print(lookahead)
        convertedExpression.append(lookahead)
        match(lookahead)


#   Looks for PRECEDING OPERATORS i.e "*" or "/"
def precedingOperators():

    if lookahead == "*":
        match("*")
        termCharacter()
        # print("*")
        convertedExpression.append("*")
        precedingOperators()

    elif lookahead == "/":
        match("/")
        termCharacter()
        convertedExpression.append("/")
        # print("/")
        precedingOperators()


# LOOKS FOR NORMAL OPERATORS i.e "+" or "-"
def normalOperators():

    if lookahead == "+":
        match("+")
        term()
        convertedExpression.append("+")
        # print("+")
        normalOperators()

    elif lookahead == "-":
        match("-")
        term()
        convertedExpression.append("-")
       # print("-")
        normalOperators()


def term():
    termCharacter()
    precedingOperators()


def postfixConverter():
    term()
    normalOperators()


# EVALUATION OF POSTFIX EXPRESSION
def evaluate(finalExpression):
    evalStack = []
    operator = ['*', '-', '+','/']      # DEFINE THE OPERATORS

    for i in finalExpression:           # ITERATE OVER THE ELEMENTS IN FINAL EXPRESSION

        if i not in operator:
            evalStack.append(i)     #appand the operands into Stack

        else:
            a = evalStack.pop()  # POP previous 2 digits from t he stack
            b = evalStack.pop()

            if i == '+':
                result = int(b) + int(a)  # old val <operator> recent value
            elif i == '-':
                result = int(b) - int(a)
            elif i == '*':
                result = int(b) * int(a)
            elif i == '/':
                result = int(b) / int(a)

            evalStack.append(result)
    return(result)


expression = input("Enter Arithmetic Expression: ") + " "   # TAKE EXTRA SPACE TO AVOID INDEX OVERFLOW ERROR
# expression = "1+2*3/4-5+6*7-8/9" + " "
indx = 0
lookahead = expression[indx]

convertedExpression = []        #  store the Sequence sequence in a list
finalExpression = ""

postfixConverter()              # Start

for item in convertedExpression:
    finalExpression += item         # JOIN THE ELEMENTS IN TO A STRING FOR PRINTING

print("Given Expression: ", expression)
print("postfix Expression: ", finalExpression)

print(evaluate(finalExpression))