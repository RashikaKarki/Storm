from Storm import token


from Storm.type import get_number_type, get_type 
from Storm.token import Token
from Storm.type import get_type
from Storm.error import ErrorIllegalChar
from Storm.position import Position

class Lexer:
    def __init__(self, text, file_name = None) -> None:
        self.file_name = file_name
        self.text = text
        self.pos = Position(-1, 1, -1, self.file_name, self.text)
        self.cur_char = None

    def __increment(self):
        self.pos.increment(self.cur_char)
        self.cur_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def make_tokens(self):
        list_tokens = []
        self.__increment()
        while self.cur_char != None:
            if self.cur_char in " \t\n":
                self.__increment()
            else:
                token_type = get_type(self.cur_char)
                if token_type != 'DIGIT' and token_type != None:
                    list_tokens.append(Token(token_type, self.cur_char))
                    self.__increment()
                elif token_type == 'DIGIT':
                    token_type, value = self.make_numbers()
                    list_tokens.append(Token(token_type, value))
                else:
                    return [], ErrorIllegalChar(self.file_name, self.pos.line_number, f'Invalid character \'{self.cur_char}\' found')
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
                break
            self.__increment()
        return get_number_type(num_str), num_str




        