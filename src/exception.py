import sys


def error_message_detail(error):
    _,_, exc_tb = sys.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name
        line_number = exc_tb.tb_lineno
    else:
        file_name = "<unknown>"
        line_number = 0
    error_message = f"Error occurred in python script [{file_name}] in line [{line_number}] error message: [{error}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message


