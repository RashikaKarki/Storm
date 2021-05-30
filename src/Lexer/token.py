class Token:
    def __init__(self, value = None, type = None) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        if self.type: return f'{self.type} : {self.value}'
        return f'{self.value}'

