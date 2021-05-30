class Position:
    def __init__(self, index, line_number, column, file_name, file_content) -> None:
        self.index = index
        self.line_number = line_number
        self.column = column
        self.file_name = file_name
        self.file_content = file_content

    def increment(self, cur_char):
        self.index += 1
        self.column += 1
        if cur_char == "\n":
            self.line_number += 1
            self.column = 0
        return self

    def copy(self):
        return Position(self.index, self.line_number, self.line_number, self.file_name, self.file_content)
