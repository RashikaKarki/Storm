from Storm import error
from Storm.lexer import Lexer

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    print(tokens)
    if error:
        print("ERROR")
        print(error)


while True:
    text = input("storm > ")
    run(text)

