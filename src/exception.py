import sys

from src.logger import logging


def error_message_detail(error,error_detail:sys):
    # gives the three infomation details
    _,_,exc_tb=error_detail.exc_info()
    # exc_tb gives all the info related to errorfile which function etc.,
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script  name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    logging.error(error_message)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    # when evert we try to print error it will return error message    
    def __str__(self):
        return self.error_message
    