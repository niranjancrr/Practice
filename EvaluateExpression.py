from Stack import Stack

def EvaluateExpression(expression):

    stack = Stack()

    bracketDict = {']':'[','}':'{',')':'('}

    expression = expression.split()
    for char in expression:
        if char != ' ':
            if char in [']',')','}']:
                numbers = []
                while stack.top != bracketDict[char]:
                    if stack.top in ['/','*','+','-']:
                        expr = stack.pop()
                        value = expr.join(numbers)
                        stack.pop()
                        stack.push(str(eval(value)))
                        break
                    else:
                        numbers.append(stack.pop())
            else:
                stack.push(char)
    return stack.pop()

if __name__ == '__main__':

    print(EvaluateExpression("56"))
    print(EvaluateExpression("( + 1 2 3 )"))
    print(EvaluateExpression("( * 1 2 3 4 )"))
    print(EvaluateExpression("( * ( + 1 2 ) 3 4 )"))
    print(EvaluateExpression("( * ( + ( * 3 4 ) 3 ) ( + 1 2 ) )"))
