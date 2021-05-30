"""
Check if the token match our grammar and parse the tokens
"""

from os import terminal_size
from Parser.number import BinaryOperationNode, NumberNode
from Lexer import Lexer

class Parser:
    def __init__(self, tokens, index = 0) -> None:
        self.tokens = tokens
        self.index = index
        self.current_token = tokens[index]

    def increment(self):
        self.index += 1
        if self.index < len(self.tokens):
           self. current_token = self.tokens[self.index]
        return self.current_token

    def parse(self):
        res = self.exp()
        return res

    def factor(self):
        token = self.current_token
        if token.type in ['INT','FLOAT']:
            self.increment()
            return NumberNode(token)
        return token

    def term(self):
        return self.binary_operation(self.factor, ["*","/"])

    def exp(self):
        """
        Priority is given to * and / 
        """
        return self.binary_operation(self.term, ["+","-"])

    def binary_operation(self, func , operations):
        """
        Algorithm explained with example:

        1.5 * 2.5 * 3 + 7.8 * 3 
        > loop where function is self.term and operator is +, -
            left = ....
                >loop where function is self.factor and operator is *, /
                    left = 1.5 
                    Operator = *
                    right = 2.5
                    left = (1.5 * 2.5)
                    operator = *
                    right = 3
                    left = ((1.5 * 2.5) * 3)
                    returns left
                > end of loop
            left = ((1.5 * 2.5) * 3)
            operator = +
            right = ....
                > loop where function is self.factor and operator is *, /
                    left = 7.8
                    operator = *
                    right = 3
                    left = (7.8 * 3)
                > end of loop
            right = (7.8 * 3)
            left = (((1.5 * 2.5) * 3) + (7.8 * 3)) 
        """
        left = func()

        # To handle cases with enclosed parenthesis
        if str(left) == "(":
            left = str(left)
            count = 0
            while True:
                self.increment()
                print(self.current_token)
                if str(self.current_token) == ")" and count == 0:
                    self.increment()
                    break
                elif str(self.current_token) == "(":
                    count += 1
                elif str(self.current_token) == ")":
                    count -= 1
                else:
                    pass
                left += str(self.current_token)
            left += ")"
            plain_left = left.replace("INT", "").replace("FLOAT","").replace(":","").replace(" ","")
            lexer = Lexer(plain_left[1:-1])
            tokens, error = lexer.make_tokens()
            
            parser = Parser(tokens)
            left = parser.parse()
            

        while str(self.current_token) in operations:
            if self.current_token == "EOL":
                break
            operator = self.current_token
            self.increment()
            right = func()
            left = BinaryOperationNode(left, operator, right)
        return left
        

