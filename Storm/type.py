import re

# PATTERNS
DIGIT = r'\d'
OPERATOR = r'[\(\)\+\-\*\/]'
DOT = r'\.'
FLOAT = r'\.'
INT = r'[0-9]'

# OPERATORS

operator_mapping = {'+' : 'PLUS OPERATOR', '-' : 'MINUS OPERATOR', '*' : 'MULTIPLICATION OPERATOR', '/' : 'DIVISION OPERATOR','(' : 'LEFT PARAM',')': 'RIGHT PARAM'}

def get_type(cur_char):
    is_digit = re.search(DIGIT, cur_char)
    is_operator = re.search(OPERATOR, cur_char)
    is_dot = re.search(DOT, cur_char)
    if is_digit:
        return "DIGIT"
    elif is_operator:
        return operator_mapping[cur_char]
    elif is_dot:
        return "DOT"
    else:
        return None

def get_number_type(number):
    is_float = re.search(FLOAT, number)
    if is_float:
        return "FLOAT"
    else:
        return "INT"


