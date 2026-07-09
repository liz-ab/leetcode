class MyQueue(object):

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x):
        self.st1.append(x)
        

    def pop(self):
        while self.st1:
            k=self.st1.pop()
            self.st2.append(k)
        b=self.st2.pop()
        while self.st2:
            a=self.st2.pop()
            self.st1.append(a)
        return b

    def peek(self):
        while self.st1:
            k=self.st1.pop()
            self.st2.append(k)
        b=self.st2[-1]
        while self.st2:
            a=self.st2.pop()
            self.st1.append(a)
        return b
        

    def empty(self):
        if(len(self.st1)==0):
            return True 
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()