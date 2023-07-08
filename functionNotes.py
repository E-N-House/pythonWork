# keyword is def my_func(var): then indented code block
def my_function():
  print("hello")
  print("bye")

# can place inputs within the () very similiar to js
def format_name(f_name, l_name):
  return f"{f_name.title()} {l_name.title()}"

name = format_name("hhhhh", "bye")
def greeting(full_name):
  print(f"Hello {name} welcome to the show")

greeting(name)

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
     return False

def days_in_month(input_year, input_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if input_month == 2:
      if is_leap(input_year):
          return 29
      else:
          return 28
  else:
      return month_days[input_month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
