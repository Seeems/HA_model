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

    if not os.path.exists('HA_model/logs'):
        os.makedirs('HA_model/logs')

    handler = logging.FileHandler(os.path.join('HA_model/logs/', name) + '.log')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
