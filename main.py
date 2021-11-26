MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": " "}

continue_converting = True

while continue_converting:
    user_input = input("Please enter a message you want to convert to Morse Code:\n").upper()
    morse_code = ""
    for char in user_input:
        morse_code += MORSE_CODE_DICT[char]
    print(f"This is the message you wanted to convert to Morse Code:\n{morse_code}")
    user_continue = input("Do you want to convert another message to Morse Code? Type yes/no: ").lower()
    if user_continue == "yes":
        continue
    else:
        continue_converting = False

print("Thank you for converting with us!!")

