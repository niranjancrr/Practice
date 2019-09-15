from Stack import Stack

def BalancedParanthesis(stringofBrackets):

    bracketDict = {']':'[','}':'{',')':'('}
    stack = Stack()

    unbalanced = True

    for char in stringofBrackets:
        if char in ['[','{','(']:
            stack.push(char)
        elif char in [']','}',')']:
            bracket = stack.pop()
            if bracketDict[char] != bracket:
                unbalanced = False
                return unbalanced

    return unbalanced


if __name__ == '__main__':
    print(BalancedParanthesis('[]{()}'))
    print(BalancedParanthesis('[{()}]'))
    print(BalancedParanthesis('[{]}]'))