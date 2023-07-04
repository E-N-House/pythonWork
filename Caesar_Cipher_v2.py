alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
alphabet_twice = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
continue_playing = True

def ceasar(method, input_text, shift_amount):
    new_text = ""
    shift_amount = shift_amount % len(alphabet)
    if method == "decode":
        shift_amount *= -1
    for char in input_text:
        try:
            position = alphabet_twice.index(char)
            new_position = position + shift_amount
            new_char = alphabet_twice[new_position]
            new_text += new_char
        except ValueError:
            new_text += char
    print(f"The {method}d message is {new_text}")


while continue_playing:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceasar(method=direction, input_text=text, shift_amount=shift)
        continue_y_n = input(
            "Would you like to continue? \n Please Type no or yes.\n").lower()
        if continue_y_n == "no":
            continue_playing = False
    direction = print("You entered something other than 'encode' or 'decode'")
