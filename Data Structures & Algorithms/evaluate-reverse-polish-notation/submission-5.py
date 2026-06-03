'''
input: a list of strings that are some comb of numbers and arithmetic ops
want: a way to evaluate hte expression presented in a int output


edge case(s): empty token list, other chars besides tokens that cna be correclty evaluated

time, space - 

exp:
- init stack which we will push all numbers to and this will store the result for us too
- iterate through hte input adding nums and when we hit an operand we pull the last 2 eleemtns form the stack to do hte op
- track hte order of ops when we pop from the stack we also need ot append hte result to hte top of hte stack after each computation
- finally we return stack[-1] which is the final result if all prev steps are done correclty

'''









class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                a, b = stack.pop(), stack.pop()
                res = int(a) + int(b)
                stack.append(res)
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                res = int(b) - int(a)
                stack.append(res)
            elif t == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(a) * int(b))
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                res = int(int(b) / int(a))
                stack.append(res)
            else:
                # must be a number so push it
                stack.append(int(t))
        return stack[-1] if stack else 0
