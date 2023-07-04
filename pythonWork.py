import math
# paint cans needed excercise
def paint_calculations(height, width, coverage):
  result = math.ceil((height*width)/cover)
  print(f"You'll need {result} cans of paint")
height_input = int(input("Height of Wall: "))
width_input = int(input("Width of Wall: "))
coverage_per_can = 5
  
  
paint_calculations(height=height_input, width=width_input, cover=coverage_per_can)
                   
# finding prime numbers excercise first version manually typing in
def prime_checker_v1(number):
    edge_case_primes = [2, 3, 5, 7]
    if number == 1:
        print("It's not a prime number")
    elif number in edge_case_primes:
        print("It's a prime number.")
    elif number%2 == 0 or number%3==0 or number%5==0 or number%7==0:
        print("It's not a prime number")
    else:
        print("It's a prime number")
      
# finding prime using loop over prime divisables in edge prime cases
def prime_checker_v2(number):
    edge_case_primes = [2, 3, 5, 7]
    isPrime = True
    if number == 1:
        print("It's not a prime number.")
    elif number in edge_case_primes:
        print("It's a prime number.")
    else:
        for i in edge_case_primes:
            if number % i == 0:
                isPrime = False
        if isPrime:
            print("It's a prime number.")
        elif isPrime == False:
            print("It's not a prime number.")



  
input_number = int(input("Enter number to check: "))
prime_checker(number=input_number)
