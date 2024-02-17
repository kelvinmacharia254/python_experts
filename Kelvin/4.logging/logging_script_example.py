"""
This script illustrates how to configure logging severity.
Change levels and observe the output.

print statements get priority over Log messages
"""
import logging

# This configuration is only done once in your program.
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",  # specify the time format
    level=logging.DEBUG,
)

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

    print("Print statements get priority over logs. This print statement is below the log messages in the source "
          "code but prints above them when the program is executed.")


example_logging_function()

#%%
