# Example configuring logging severity
import logging

# Configure logging
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# This configuration is only done once in your program.
# Example adding other parameters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d - %b - %y %H:%M:%S',  # specify the time format
                    level=logging.DEBUG)

# Change the logging level to desired severity
logger = logging.getLogger()
logger.setLevel(logging.INFO)
print(logger, logger.level)

# logging.getLogger().setLevel(logging.INFO) # logger reconfiguration using a chained alternative
def example_logging_function():
    # DEBUG level
    logging.debug('This is a debug message.')

    # INFO level
    logging.info('This is an informational message.')

    # WARNING level
    logging.warning('This is a warning message.')

    # ERROR level
    logging.error('This is an error message.')

    # CRITICAL level
    logging.critical('This is a critical message.')

example_logging_function()