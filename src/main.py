from Parser import Parser
from Lexer import Lexer
from bgcolors import Bcolors

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    print(tokens)
    if error:
        print(f"{Bcolors.FAIL}ERROR{Bcolors.ENDC}")
        print(f"{Bcolors.FAIL}{error}{Bcolors.ENDC}")
    if len(tokens) >= 1:
        parser = Parser(tokens)
        ast = parser.parse()
        print(ast)


while True:
    text = input(f"{Bcolors.OKBLUE}strom > {Bcolors.ENDC} ")
    run(text)

