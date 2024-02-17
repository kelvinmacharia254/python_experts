"""
logging_custom_logger.py
Created by Kelvin for PythonExperts on 2nd February 2024
Copyright (c) PythonExperts All rights reserved
Credits to the Python Foundation

This scripts illustrates how to create custom loggers.

Components of a logger:
1. Handler/ Destination for logging message
  Each handler class represents a destination.
      a) StreamHandler() for stdout/console.
      b) FileHandler for logging to a file.
      c) STMPHandler for logging for emailing.
      d) HTTPHandler for sending logs to web server through POST HTTP methods.

NOTE: All logs from different handlers are logged simultaneously with the same messages.
    : You can configure all handlers if you require that
2. Formatter: Defined ow the log message strings looks like.
3. Severity level: Defines severity of an event
"""
import logging

# Step 1: Create a logger
# Create a logger and give it a name similar to the module.
# Use Logger() class and pass in a custom name for your logger.
logger = logging.getLogger(__name__)  # __name__ refers to the current module
print(logger.name)

# Step 2: Configure handlers
# Create handlers using Handler() class. You set as many as options available
#    a) Console handler
console_handler = logging.StreamHandler()
#    b) file handler: - to log to file. Specify the file name
file_handler = logging.FileHandler("logfile.txt")

# Step 3: Set severity level for each of the handlers.
# Set severity level for each handler.
# Each handler can be set to have its own severity level
# Loggers log the level set or higher.

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Step 4: Configure a formatter
# Create formatters, formatter can have different patterns for each handler they don't have to match.
# Custom logger has no format and one should be defined for each Handler.
# Without a formatter, the logger will just log the log message passed. This lacks meta-data and context.
# Logs metadata includes information timestamps, execution line number e.t.c
# The Formatter() class of the logging module fits the job.
console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Step 5: Associate formatters to the handlers
# The formatter objects so far are independent of the logging handlers. Let's associate
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# step 6: Link handler to the custom logger
# Link the handlers to the custom logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Lets try out our custom logger.
logger.warning("This is a warning")
logger.error("This is an error")

"""
How the code works
- We created a custom logger with two handlers one for the stdout/console and one for the stderr/file.
- Each handler was set to have its own severity level.
- Remember python logs the severity level set or more severe than that
- When the custom logger is run, the two lines will be logged on the console because the console handler
  was set to ERROR level which is less severe to WARNING. Only the error log will be logged to file because the
  file log handler level was set to ERROR level which is higher than WARNING.
  
- Comment out the original code around with the severity level for the handlers and observe the output 
  of the logger both on console and on the file.
"""
