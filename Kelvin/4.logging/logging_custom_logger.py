"""
logging_custom_logger.py
Created by Kelvin for PythonExperts on 2nd February 2024
Copyright (c)

This scripts illustrates how to create custom loggers.

"""
import logging

# Create a logger and give it a name similar to the module.
# Use Logger() class and pass in a custom name for your logger
logger = logging.getLogger(__name__)  # __name__ refers to the current module

# create handlers using Handler() class subclasses such as
# Each handler class represents a destination
#   StreamHandler() for stdout/console
#   FileHandler for outputting to a file
#   STMPHandler for outputting for emailing
#   HTTPHandler for sending logs to web server though GET and POST HTTP methods.

# NOTE: All logs from different handlers are logged simultaneously.

#   1. console handler: - to log to stdout
c_handler = logging.StreamHandler()
#   2. file handler: - to log to file.Specify the file name
f_handler = logging.FileHandler("logfile.txt")

"""
Set severity level for each handler
Each handler can be set to have its own severity level

Loggers log the level set or higher.
"""
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters, formatter can have different patterns they don't have to match.
# Custom logger has no format and one should be defined for each Handler.
# The Formatter() class of the logging module fits the job.
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# The formatter objects so far are independent of the logging handlers. Let's associate
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)


# Link the handlers to the custom logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Lets try out our custom logger.
logger.warning("This is a warning")
logger.error("This is an error")

"""
How the code worked
- We created a custom logger with two handlers one for the stdout/console and one for the stderr/file.
- Each handler was set to have its own severity.
- Remember python logs the severity level set or more severe
- When the custom logger is run, the two lines will be logged on the console because the console handler
  was set to ERROR level which is less severe to WARNING. Only the error log will be logged to file because the
  file log handler level was set to ERROR level which is higher than WARNING.
  
- Play around with the severity level for the handlers and observe the output of the logger both on console and
  on the file.
"""