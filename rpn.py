class Stack:
    def __init__(self): 
        self.elements = []
    def push(self,data):
        self.elements.append(str(data))
        return self.elements
    def pop(self): 
        return self.elements.pop(-1)
    def isempty(self): 
        return self.elements == []
    def top(self): 
        return self.elements[-1]
    def len(self):
        return len(self.elements)
    def printer(self): 
        print(self.elements)

def writer(expression):
    try:
        operators = ['+', '-', '*', '/', '(', ')'] #possible operators + parentheses
        for things in expression:
            if things in operators: #it is quite complex piece of code, and it is crucial to remember that here + and - are more important than * and /, unlike in normal mathematicsp
                if things == '+' or things == '-':
                    if stackoperators.isempty() == True or stackoperators.top() == '(':
                        stackoperators.push(things) #just push them into operators stack 
                    else:
                        if stackoperators.top() == '-' or stackoperators.top() == '+':
                            temp = stackoperators.pop()
                            stack.push(temp) #pop operator from top of the operators stack and add it to a equation stack and add new operator to the operator stack
                            stackoperators.push(things)
                        else:
                            stackoperators.push(things) 
                elif things == '*' or things == '/':
                    if stackoperators.isempty() == True or stackoperators.top() == '(':
                        stackoperators.push(things)
                    else:
                        if stackoperators.top() == '+' or stackoperators.top() == '-':
                            try: #I used it, because while below this line will give an indexerror if the stack is empty. So probably it could have been done with while stackiempty == False or something like that
                                while stackoperators.top() == '+' or stackoperators.top() == '-':
                                    temp = stackoperators.pop()
                                    stack.push(temp)
                                stackoperators.push(things)
                            except IndexError:
                                stackoperators.push(things)      
                        else:
                            temp = stackoperators.pop()
                            stack.push(temp)
                            stackoperators.push(things)
                elif things == '(':
                    stackoperators.push(things)
                elif things == ')':
                    while True: 
                        temp = stackoperators.pop()
                        stack.push(temp) #pop and push from one stack to the other to the moment when there is '('. Both parentheses should not be pushed.
                        if stackoperators.top() == '(':
                            stackoperators.pop()
                            break
            else:
                stack.push(things)
        while stackoperators.isempty() == False: #finally, push all of the operators from the operators stack to the elements stack 
            temp = stackoperators.pop() 
            stack.push(temp)
    except IndexError:
        print("You probably entered something incorrectly. Please check it out.")
        quit() #end the program if the input is wrong

def repairer(): #this function helps to print the equation which has been already transformed into reversed polish notation
    equation = [] 
    while stack.isempty() == False:
        equation.append(stack.pop()) #make a list from print
    equation.reverse() #such a list would be reversed, so we need to reverse it once again
    return equation  

def evaluator(repairedequation): #this function will calculate the result of the correctly transformed equation
    try:
        operators = ['+', '-', '*', '/', '(', ')']
        for elements in repairedequation:
            if elements in operators:
                number2 = float(stackoperators.pop())
                number1 = float(stackoperators.pop()) #take 2 elements from the top and the operator
                result = calculator(number2, number1, elements) 
                stackoperators.push(result) #and push the result to the already empty operatorstack
            else: 
                stackoperators.push(elements)
        print("the final result is equal to: ")
        stackoperators.printer()
        if stackoperators.len() > 1: #this error will not crash the program, but it is wrong anyways
            print("You probably added to many numbers in comparison to operators to the stack. Please check it.")
    except ValueError: #errors that i found
        print("Probably you accidently added a space somewhere where you should not, or made other mistake while inputting. Check it please.")
    except IndexError:
        print("You most likely added too many operators in comparison to numbers. Please check it.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")

def calculator(element2, element1, operator): #this function takes two numbers and the operator and returns the result
    if operator == '+':
        return(element1+element2)
    if operator == '-':
        return(element1-element2)
    if operator == '*':
        return(element1*element2)
    if operator == '/':
        return(element1/element2)

stack = Stack()
stackoperators = Stack()

while True:
    try:
        maxlength = int(input("input maximum length of the stack:\n"))
        break
    except ValueError:
        print("that was not a number")

lengthdeclared = maxlength + 1

while lengthdeclared > maxlength: #not longer than the max length of stack
    equation = str(input("enter the equation in normal notation with spaces. It should be also not longer than the maxlength of the stack, excluding spaces:\n"))
    equationlist = equation.split(" ") #str into list
    lengthdeclared = len(equationlist)


writer(equationlist)
repairedequation = repairer()
repairedstring = ''

for elements in repairedequation:
    repairedstring += elements
    repairedstring += ' '

print("equation in reversed polish notation:",repairedstring)

evaluator(repairedequation)
# 2 example equations 
# ( 3 * 6 + 2 ) + ( 14 / 3 + 4 )
# 17 * ( 2 + 3 ) + 4 + ( 8 * 5 )


