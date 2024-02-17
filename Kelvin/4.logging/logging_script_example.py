"""
This script illustrates how to configure logging severity.
Change levels and observe the output.

Providing a filename to the basicConfig() function in Python's logging module, by default, logs will not be sent
to the console (stdout). The basicConfig() function initializes logging and configures the root logger with the
specified options, including directing output to a file.

Providing a filename to basicConfig() doesn't explicitly prevent logs from being sent to the console.
Instead, it simply configures the logging system to send logs to the specified file.
Logs can still appear on the console in addition to being written to the file,
you would need to explicitly add a StreamHandler (or another appropriate handler) for console output.
"""
import logging

# This configuration is only done once in your program.
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",  # specify the time format
    # filename="logfile_example1.txt",
    level=logging.DEBUG,
)
root_logger = logging.getLogger()
f_handler = logging.FileHandler("root_file.txt")
root_logger.addHandler(f_handler)

# comment or comment this block to see it's effect
# Change the logging level to desired severity. You can't use
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# print(logger, logger.level)


# logger reconfiguration using a chained alternative
# It has the same effect as above.Comment or uncomment
# logging.getLogger().setLevel(logging.INFO)
def example_logging_function():
    """
    illustrates how to configure several logging levels
    :return:
    """
    # DEBUG level
    logging.debug("This is a debug message.")

    # INFO level
    logging.info("This is an informational message.")

    # WARNING level
    logging.warning("This is a warning message.")

    # ERROR level
    logging.error("This is an error message.")

    # CRITICAL level
    logging.critical("This is a critical message.")


example_logging_function()

# %%
