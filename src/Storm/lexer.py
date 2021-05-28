from typing import Text
from Storm import token


from Storm.type import * 
from Storm.token import Token
from Storm.type import get_type
from Storm.error import *

class Lexer:
    def __init__(self, text) -> None:
        self.text = text
        self.pos = -1
        self.cur_char = None

    def __increment(self):
        self.pos += 1
        self.cur_char = self.text[self.pos] if self.pos < len(self.text) else None

    def __decrement(self):
        self.pos -= 1
        self.cur_char = self.text[self.pos] if self.pos < 0 else None

    def make_tokens(self):
        list_tokens = []
        self.__increment()
        while self.cur_char != None:
            if self.cur_char in " \t":
                self.__increment()
            else:
                token_type = get_type(self.cur_char)
                if token_type != 'DIGIT' and token_type != None:
                    list_tokens.append(Token(token_type, self.cur_char))
                    self.__increment()
                elif token_type == 'DIGIT':
                    token_type, value = self.make_numbers()
                    list_tokens.append(Token(token_type, value))
                    self.__increment()
                else:
                    return [], ErrorIllegalChar(self.cur_char)
                    

        return list_tokens, None

    def make_numbers(self):
        num_str = ''
        dot_count = 0
        while self.cur_char != None:
            char_type = get_type(self.cur_char)
            if char_type == "DOT":
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
            elif char_type == "DIGIT":
                num_str += str(self.cur_char)
            else:
                self.__decrement()
                break
            self.__increment()
        return get_number_type(num_str), num_str




        