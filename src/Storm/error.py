class Error:
    def __init__(self, error_name, error_details = None) -> None:
        self.error_name = error_name
        self. error_details = error_details

    def __repr__(self) -> str:
        if self.error_details != None: return f'{self.error_name} \n Details : {self.error_details}'
        return f'{self.error_name}'


class ErrorIllegalChar(Error):
    def __init__(self, details) -> None:
        super().__init__('Illegal Character Deteted', details)
        