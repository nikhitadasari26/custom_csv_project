class CustomCsvReader:
    """
    Custom CSV reader that parses CSV files character by character.
    """

    def __init__(self, file):
        self.file = file
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration

        row = []
        field = ""
        in_quotes = False

        while True:
            char = self.file.read(1)

            if char == "":
                self.eof = True
                if field or row:
                    row.append(field)
                    return row
                raise StopIteration

            if char == '"':
                if in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':
                        field += '"'
                    else:
                        in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    in_quotes = True

            elif char == "," and not in_quotes:
                row.append(field)
                field = ""

            elif char == "\n" and not in_quotes:
                row.append(field)
                return row

            else:
                field += char
