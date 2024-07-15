import logging


import logging

def setup_logging(log_file):
    """
    Set up logging configuration.

    Args:
        log_file (str): The path to the log file.

    Returns:
        None
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def log_info(message):
    logging.info(message)


def log_error(message):
    logging.error(message)
