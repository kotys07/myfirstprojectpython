class Stack:
    def __init__(self):
        self.stack = list()
        self.maxSixe = 6
        self.top = 0

    def push(self,data):
        if self.top>=self.maxSixe:
            return ("Stack Full!!!")
        self.stack.append(data)
        self.top += 1
        return True

    def pop(self):
        if self.top<=0:
            return ("Stack Empty!!!")
        item = self.stack.pop()
        self.top -= 1
        return item

    def size(self):
        return self.top

s = Stack()

print(s.push(2))
print(s.push(3))
print(s.size())
print(s.push(4))
print(s.push(5))
print(s.size())
print(s.push(6))
print(s.push(8))
print(s.push(6))
print(s.size())
print(s.pop())
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())