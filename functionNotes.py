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
