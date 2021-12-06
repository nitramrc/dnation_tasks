import os
import logging  # Create the Logger


def get_console_handler(log_format: str = '%(message)s') -> logging.StreamHandler:
    """
    Setup console handler
    :param: format of the logging message
    :return: console handler
    """
    # progressbar.streams.wrap_stderr()
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # console_handler.setLevel(logging.DEBUG)
    logger_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(logger_formatter)
    return console_handler


def setup_root_log(file_name: str = 'main', set_logstash: bool = False):
    """
    Root logger setup
    :param: file_name:string name of the log file, e.g. main, data, exp
    :param: set_logstash:bool setting logstash ON or OFF
    """
    log_path = os.path.join('logs', file_name + '.log')

    # If applicable, delete the existing log file to generate a fresh log file during each execution
    if os.path.isfile(log_path):
        os.remove(log_path)

    # Create the Logger
    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)
    # logger.setLevel(logging.DEBUG)

    # Create a Formatter for formatting the log messages
    logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create the Handler for logging data to a file
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)
    # Add the Formatter to the Handler
    file_handler.setFormatter(logger_formatter)

    # Add the Handler to the Logger
    logger.addHandler(file_handler)
    logger.addHandler(get_console_handler())
    if set_logstash:
        """logstash json filter parse message, extra fields ,exc_info"""
        logger.addHandler(logstash.LogstashHandler('logstash', 5959, version=1))
    # logger.info('Logger configured')
    logger.debug('Logger configured')
