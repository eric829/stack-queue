
# coding: utf-8

# In[22]:

class Queue:
    
    def __init__(self):
        self.queue = []
        self.size = 4
        
    def push(self, x):
        if len(self.queue) >=0 and len(self.queue) < self.size:
            self.queue = self.queue + [x]
    
    def pop(self):
         
        if len(self.queue) >0 :
            output= self.queue[0] 
            self.queue=self.queue[1:]
            return output
        else:
            return 
        

q = Queue()
q.push(5)
q.push(4)
q.push(3)
q.push(2)
q.push(1)

print q.queue,q.pop()
print q.queue,q.pop()
print q.queue,q.pop()
print q.queue,q.pop()
print q.queue,q.pop()


 


# In[101]:

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
    
s=Stack()

s.push(4)
s.push(5)
s.push(3)
print s.pop()
print(s.stack)
print s.pop()
print(s.stack)


# In[97]:




# In[ ]:



