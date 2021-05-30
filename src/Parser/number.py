class NumberNode:
    """
    Takes in number tokens
    """
    def __init__(self, number_token) -> None:
        self.number_token = number_token

    def __repr__(self) -> str:
        return f'{self.number_token}'

class BinaryOperationNode:
    """
    For Binary operations like +|-|*|/
    """
    def __init__(self, left_node, operator, right_node) -> None:
        self.left_node = left_node
        self.operator = operator
        self.right_node = right_node

    def __repr__(self) -> str:
        return f'({self.left_node}, {self.operator} , {self.right_node})'
