"""
Example logging tracebacks
Notes:
    By default, python sends the logs to stderr.
    We can log them instead using try except statements.
    There are two ways to do this.

    GOTCHAs:
    1. When the tracback is logged on the console, it looks like an exception has been thrown.
    2. basicConfig() is only configured once in the life/instance of the program, but we can use
       getLogger() and setLevel() attributes(methods) of the logger to reconfigure the logging level.
"""
import logging
import traceback

# configure logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',  # specify the time format
                    level=logging.DEBUG)

# Logging tracebacks method 1
#   Any logging severity level can be used. We only need to pass kwarg exc_info=True along with the log message.
logger = logging.getLogger()
# logging.debug(f"First example logger: {logger.level}")


def log_tracebacks_method1():
    """
    log a traceback
    """
    my_list = ["Caro", "Rogers", "Kelvin"]
    try:
        print(my_list[5])
    except Exception as e:
        logging.debug("Exception occurred in method 1.Here is the traceback", exc_info=True)
        # log the line below the logged traceback.
        logging.debug("\nThe above was a logged traceback.\nThe exception was handled gracefully by the try except "
                      "statement.\nEasy to mistake for your ordinary stderr traceback. Otherwise line wouldn't be "
                      "printed.\n")


# log_tracebacks_method1()

##############################################################
# Logging tracebacks method 2
#   First we change the severity level to error.
#   use logging.exception(). No kwarg required, exception as error and ERROR severity handles them automatically.

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
# logging.error(f"Second example logger: {logger.level}")


def log_tracebacks_method2():
    """
    log a traceback
    """
    my_list = ["Caro", "Rogers", "Kelvin"]
    try:
        print(my_list[5])
    except Exception as e:
        logging.exception("Exception occurred in method 2.Here is the traceback")
        # log the line below the logged traceback.
        logging.error("\nThe above was a logged traceback.\nThe exception was handled gracefully by the try except "
                      "statement.\nEasy to mistake for your ordinary stderr traceback. Otherwise line wouldn't be "
                      "printed.\n")


# log_tracebacks_method2()


##############################################################
# Logging tracebacks method 3
#   Use traceback module to extract information ang using logging module to log.
#   use logging.exception(). No kwarg required, exception as error and ERROR severity handles them automatically.
def log_tracebacks_method3():
    """
    log a traceback
    """
    my_list = ["Caro", "Rogers", "Kelvin"]
    try:
        print(my_list[5])
    except Exception as e:
        # Option 1: Extract the general traceback information using traceback module then log it.
        # Different method but similar result as option 2
        traceback_info = traceback.format_exc()
        # Log the traceback information
        logging.error(f"Traceback General information:\n{traceback_info}")

        # Option 2: Extract the specific traceback information using traceback module then log it
        # Different from option 1 because you log line by line-specific detail about the traceback.
        # In this option, you are able to select information needed or leave out unnecessary information
        logging.error("Logging Traceback information line by line:\n")
        traceback_info = traceback.extract_tb(e.__traceback__)

        # Log each frame of the traceback

        for frame in traceback_info:
            log_message = f"\nFile: {frame.filename},\nException occurred at line: {frame.lineno},\nFunction: {frame.name}"
            logging.error(log_message)

        logging.error(f"Exception occurred: {e}\n\n")

        logging.error("The above was a logged traceback.\nThe exception was handled gracefully by the try except "
                      "statement.\nEasy to mistake for your ordinary stderr traceback. Otherwise line wouldn't be "
                      "printed.\n")


log_tracebacks_method3()
#%%

#%%

#%%
