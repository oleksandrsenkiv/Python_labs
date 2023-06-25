import logging

'''
logged is module with logged decorator
'''


def logged(exeption, mode):
    '''
        A decorator that logs exceptions raised by the decorated function.

        Args:
            exception (Exception): The type of exception to be caught and logged.
            mode (str): The logging mode. Can be either "console" or "file".

        Returns:
            function: The decorated function.
            '''

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exeption as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(level=logging.INFO, filename="error.log", filemode="w")
                    logging.error(str(e))
            return None

        return wrapper

    return decorator
