class Error:
    def __init__(self, file_name, line_number, error_name, error_details = None) -> None:
        self.file_name = file_name
        self.line_number = line_number
        self.error_name = error_name
        self. error_details = error_details

    def __repr__(self) -> str:
        if self.file_name != None: 
            error_info = f'{self.error_name} in line {self.line_number} of {self.file_name}'
        else: 
            error_info = f'{self.error_name} in line {self.line_number}'
        if self.error_details != None: return f'{error_info}\n Details : {self.error_details}'
        return f'{error_info}'


class ErrorIllegalChar(Error):
    def __init__(self,file_name, line_number, details) -> None:
        super().__init__(file_name, line_number,'Illegal Character Detected',  details)

        