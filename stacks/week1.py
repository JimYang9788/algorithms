# Stack Week 1 

# 8.1  Implement a stack with MAX API 

# Design a stack that includes a max operation, in addition to 
# push and pop. The max returns the maximum value on the stack 

class Stack:

    content = []
    max_val = [] 

    def __init__(self):
        self.content = []

    def push (self, x):
        
        self.content.append (x)
        
        if self.max_val == [] or x > self.max_val[-1]:
            self.max_val.append(x) 
        else:
            self.max_val.append (self.max_val[-1])
        
    def pop (self, x):

        self.max_val.pop()
        return self.content.pop()

    def get_max(self, x):
        if self.max_val == []:
            return None 
        else: 
            return self.max_val[-1]


