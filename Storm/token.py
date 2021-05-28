class Token:
    def __init__(self, type, value = None) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        if self.value: return f'{self.type} : {self.value}'
        return f'{self.type}'

