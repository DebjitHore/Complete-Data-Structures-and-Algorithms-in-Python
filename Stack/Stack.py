
class Stack:
  def __init__(self):
    self.list=[]
  def __str__(self):
    #values= reversed(self.list)
    values= self.list.reverse()
    values= [str(x) for x in self.list]
    return '\n'.join(values)

#isEmpty

  def isEmpty(self):
    if self.list==[]:
      print("Stack is empty") 
    else:
      print("Stack is not empty")
#push
  def push(self, value):
    self.list.append(value)
    return "Element has been successfully inserted"
#pop
  def pop(self):
    if self.isEmpty():
      return "There is no element in the stack"
    else:
      return self.list.pop()
    #peek
  def peek(self):
    if self.isEmpty():
      return "No element"
    else:
      return self.list[-1]

  def delete(self):
    self.list= None






#Check if stack is empty or not

customStack= Stack()

customStack.isEmpty()

# push new elements
customStack.push(4)
customStack.push(12)
customStack.push(3)


#popping from the Stack  
customStack.pop()
print(customStack)

print(customStack.peek())