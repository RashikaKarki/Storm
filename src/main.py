from Storm import Lexer
from bgcolors import Bcolors

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    print(tokens)
    if error:
        print(f"{Bcolors.FAIL}ERROR{Bcolors.ENDC}")
        print(f"{Bcolors.FAIL}{error}{Bcolors.ENDC}")


while True:
    text = input(f"{Bcolors.OKBLUE}strom > {Bcolors.ENDC} ")
    run(text)

