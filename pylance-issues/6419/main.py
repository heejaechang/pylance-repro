 # SCENARIO: hover on a bound method reference should show the method signature and docstring
 # TARGET: `read_file` in `BinFileReaderBase().read_file`
 # TRIGGER: hover over `read_file`
 # EXPECT: hover shows the method signature plus the docstring text
 # VERIFY: if hover drops the signature or docstring, the bug still reproduces
 # RECOVER: no recovery needed

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