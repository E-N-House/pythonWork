# Calculator functions
def add(n1, n2):
  """ Takes two numbers and adds them together """
  return n1 + n2

def subtract(n1, n2):
  """ Takes two numbers and subtracts number 1 from number 2 """
  return n1 - n2

def multiply(n1, n2):
  """ Takes two numbers and multiplies together """
  return n1 * n2

def divide(n1, n2):
  """ Takes two numbers and divides number 1 by number 2 """
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

# User interactions
num1 = int(input("What is the first number?:  "))
num2 = int(input("What is your second number?:  "))
chosen_opperator = input("which operation would you like to preform? '+', '-', '*', or '/':  ")
function = operations[chosen_opperator]
print(function(num1, num2))
