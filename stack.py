#Last In First Out (LIFO) - like a stack of plates, the last plate placed ontop is the first to later be removed
#lists are treated as a stack in python
stack = []

#push 
stack.append(10)
stack.append(20)
stack.append(30)
#data is printed in order it was added or "stacked"
print(stack)
print("---------")

#pop - the last value is removed first, last added first removed
x = stack.pop() #removes 30, the top of the stack
print(x) 
print(stack)

print("---------")

y = stack.pop() #removes 20, the new top of the stack
print(y)
print(stack)


print("---------")
#peak 
print(stack[-1]) #note -1 lets you peak at the list element in a list, or the top of the stack