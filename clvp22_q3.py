#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after


###########
#Algorithm#
###########
            
def good_expression(string):
     
    p = {"*":3,"+":2,"(":1,")":1} #operator precedence dictionary
    
    opStack = Stack() #stack for operators
    leftStack = Stack() #stack for operators left of some brackets
    rightStack = Stack() #stack for operators right of some brackets
    lowStack = Stack() #stack holding the precedence of the lowest precedence operator between 2 brackets
    lst = list(string) #list of opertors and operands

    for i in range(0,len(lst)):
        char = lst[i]
        if char not in "0123456789":
            if char == '(':
                opStack.push(char) #push open brackets onto operator stack
                
                if i > 0:
                    Left = p[lst[i-1]] #get the precedence of operator left of the brackets
                else:
                    Left = 0 #if there is no operator left of the brackets set the precedence to 0

                leftStack.push(Left) #push the precedence to the left stack
                    
            elif char == ')':
                top = opStack.pop() #pop next operator
                
                if top == '(': return False #if we find a close brackets immediately we have a double brackets case so redundant brackets
                
                lowStack.push(p[top]) #push the precedence of the next operator to the low stack
                
                if i != len(lst) -1:
                    Right = p[lst[i+1]] #get the precedence of the operator right of the brackets
                else:
                    Right = 0 #if there is no operator right of the brackets set the precedence to 0

                rightStack.push(Right) # push the precedence to the right stack
                
                while top != '(': #loop until we find a close brackets
                    
                    if p[top] < lowStack.top(): #if we find an operator with a lower precedence than we already have
                        lowStack.pop()  #replace the operator on the top of the low stack with precedence of the new operator that has lower precedence
                        lowStack.push(p[top])
                    
                    top = opStack.pop() #find the next operator

                X = lowStack.pop() #set X to the precedence of the lowest precedence operator within the 2 backets (that is not in another pair of backets)
                Left = leftStack.pop() # set Left to the precedence of the operator left of the brackets
                Right = rightStack.pop() #set Right to the precedence of the operator right of the brackets
                
                if not(X < Left or X < Right): #If X is not less than Left or Right then we have redundant brackets
                    return False
            else:
                while (not opStack.isEmpty()) and (p[opStack.top()] >= p[char]):
                      opStack.pop() #pop top operator until the top does not have a higher precedence than the incoming operator
                opStack.push(char) #push operator to operator stack
                
    return True #no redundant brackets after expression has been character wise evaluated

#####################################################
            

def testq3():
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)") 
    print ("all tests passed")
    
#####################################################

