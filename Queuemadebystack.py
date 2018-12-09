class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack= self.stack + [x]
        
    def pop(self):
        if len(self.stack) >0 :
            output= self.stack[-1] 
        self.stack = self.stack[:-1]
        return output


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        if len(self.stack2) == 0 :
            if len(self.stack1) >0 : 
                while len(self.stack1)>0:
                    p =self.stack1.pop()
                    self.stack2.append(p)
                return self.stack2.pop()
            else:
                return "That's all"
        else:
            return self.stack2.pop()
        
    
    
q = Queue()
q.push(5)
q.push(4)
q.push(3)
q.push(2)
q.push(1)

print q.pop()
print q.pop()
print q.pop()
print q.pop()
print q.pop()
print q.pop()
