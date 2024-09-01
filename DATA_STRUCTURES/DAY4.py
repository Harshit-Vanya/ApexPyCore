# # reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
from collections import deque

# stack = deque()
# def reverse_string(phrase: str):
#     count =0 
#     for i in phrase:
#         stack.append(i)
#         count +=1
#     phrase = ""
#     for i in range(count):
#         phrase += stack.pop()
#     return phrase

# print(reverse_string("I am Unstoppable"))

# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    # print(is_balanced("({a+b})"))
    # print(is_balanced("))((a+b}{"))
    # print(is_balanced("((a+b))"))
    # print(is_balanced("((a+g))"))
    # print(is_balanced("))"))
    # print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    print(is_match('}','{'))
            
