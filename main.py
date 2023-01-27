import json
import builtins
import sys

with open("spanish_to_python.json", "r") as f:
    spanish_to_python = json.load(f)

# Create a dictionary that maps English error messages to Spanish translations
error_translations = {
    "invalid syntax": "sintaxis inválida",
    "unexpected EOF while parsing": "EOF inesperado mientras se analizaba",
    "name '{}' is not defined": "el nombre '{}' no está definido"
}

def translate_input(input_text):
    for spanish, python in spanish_to_python.items():
        input_text = input_text.replace(spanish, python)
    return input_text

def spanish_excepthook(type, value, traceback):
    # If the error message is in our error_translations dictionary, use the translated message
    if value.args[0] in error_translations:
        builtins.print(error_translations[value.args[0]].format(*value.args[1:]))
    else:
        builtins.print(value)
    builtins.print("\n")

sys.excepthook = spanish_excepthook

while True:
    print("Note: Some commands may not work. If you get an error, try again with a different command. Type 'end command' to exit. Type 'esp end command' to exit in Spanish. (Note: This is not a complete list of Python commands.")
    user_input = input("Enter a Python function in Spanish (or type 'end command' to exit): ")
    if user_input == "esp end command":
        break
    translated_input = translate_input(user_input)
    try:
        exec(translated_input)
    except Exception as e:
        spanish_excepthook(*sys.exc_info())

    if user_input != "end command":
        user_input = input("Enter a Python function in Spanish (or type 'end command' to exit): ")
        if user_input == "end command":
            break
        translated_input = translate_input(user_input)
        exec(translated_input)
        
    try:
        exec(translated_input)
    except Exception as e:
        spanish_excepthook(*sys.exc_info())
