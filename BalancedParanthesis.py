from Stack import Stack

def BalancedParanthesis(stringofBrackets):

    bracketDict = {']':'[','}':'{',')':'('}
    stack = Stack()

    flag = True

    for char in stringofBrackets:
        if char in ['[','{','(']:
            stack.push(char)
        elif char in [']','}',')']:
            bracket = stack.pop()
            if bracketDict[char] != bracket:
                flag = False
                return flag

    return flag


if __name__ == '__main__':
    print(BalancedParanthesis('[]{()}'))
    print(BalancedParanthesis('[{()}]'))
    print(BalancedParanthesis('[{]}]'))