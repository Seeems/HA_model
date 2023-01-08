import logging
import os

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


def setup(name: str, level: int = logging.INFO) -> logging.Logger:
    """Function to setup a specific logger.

    INPUT:
    name: str -> Logger name and filename of logs
    level: int -> Logging level, default is INFO, expected format: logging.DEBUG

    OUTPUT:
    logger: logging.Logger -> New created Logger
    """
    path = os.path.dirname(os.path.realpath(__file__)) + '/logs'
    if not os.path.exists(path):
        os.makedirs(path + '/logs')
    handler = logging.FileHandler(os.path.join(path, name) + '.log')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
