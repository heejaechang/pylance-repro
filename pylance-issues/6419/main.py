class BinFileReaderBase:
    def read_file(self, filename: str):
        """
        Implement file reading.

        Args:
        ------
        `filename`: str
            File to read.

        Return:
        ------
        `file_read`: bool
            Whether the file was read successfully.
        """
        ...


BinFileReaderBase().read_file