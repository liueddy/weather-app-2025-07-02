import functools
from datetime import datetime
from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler
import os


def log_request(func):
    @functools.wraps(func) # needed to preserve the original function obj

    # this is functionally like an @before for j-unit tests
    def wrapper_log_request(*args, **kwargs):
        """logs flask requests for debugging BEFORE processing each request

        ----------- THIS FUNCTION ONLY WORKS FOR FLASK REQUESTS -----------

        prints to console in the following format:
            [<datetime>]
                <method>
                <path>
                <args>
        writes to file in log folder "flask.log" in following format on a single line: 
            {
                "date":   <datetime>,
                "method": <method>,
                "path":   <path>,
                "args":   <args>
            }
        """
        print(f"[{datetime.now().isoformat()}]\n\t{request.method}\n\t{request.path}\n\t{request.args}\n")
        json_writable = {
            "date": datetime.now(),
            "method": request.method,
            "path": request.path,
            "args": request.args
        }

        # init logger
        logger = logging.getLogger('logger2')
        logger.propagate = False  # stop duplicate logs
        print(logger.handlers)
        if not logger.handlers:
            handler = RotatingFileHandler(os.path.join(os.getcwd(),'log/flask.log'), # write to "log" folder
                                        maxBytes=2000, 
                                        backupCount=10, 
                                        encoding="utf-8")
            logger.addHandler(handler)

        # make debug logs to log file
        logger.setLevel(logging.DEBUG)
        logger.debug(str(json_writable))

        # end wrapper and call function
        return func(*args, **kwargs)
    return wrapper_log_request



# def outter_log_req(*outter_args):
#     def log_request(func):
#         @functools.wraps(func)
#         def wrapper_log_request(*args, **kwargs):
#             print("\n\nlogging start:",str(func))
#             print("datetime:\n\t",datetime.now().isoformat())
#             print(outter_args)
#             return func(*args, **kwargs)
#         return wrapper_log_request
#     return log_request
