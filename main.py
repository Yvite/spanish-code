spanish_to_python = {
    "suma": "sum",
    "imprimir":"print",
    "printar": "print",
    "principal": "main",
    "definir": "def",
    "por": "for",
    "cuando": "while",
    "para": "for",
    "en": "in",
    "rango": "range",
    "si": "if",
    "sino": "else"
}
def translate_input(input_text):
    for spanish, python in spanish_to_python.items():
        input_text = input_text.replace(spanish, python)
    return input_text
user_input = input("Enter a Python function in Spanish: ")
translated_input = translate_input(user_input)
exec(translated_input)


