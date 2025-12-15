class CustomCsvWriter:
    """
    Custom CSV writer that writes data into CSV format.
    """

    def __init__(self, file):
        self.file = file

    def _serialize_field(self, field):
        field = str(field)
        if any(c in field for c in [",", '"', "\n"]):
            field = field.replace('"', '""')
            return f'"{field}"'
        return field

    def write_row(self, row):
        line = ",".join(self._serialize_field(f) for f in row)
        self.file.write(line + "\n")

    def write_rows(self, rows):
        for row in rows:
            self.write_row(row)
