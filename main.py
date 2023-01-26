import json
with open("spanish_to_python.json", "r") as f:
    spanish_to_python = json.load(f)
def translate_input(input_text):
    for spanish, python in spanish_to_python.items():
        input_text = input_text.replace(spanish, python)
    return input_text
user_input = input("Enter a Python function in Spanish: ")
translated_input = translate_input(user_input)
exec(translated_input)


