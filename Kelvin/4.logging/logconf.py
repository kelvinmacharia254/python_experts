import logging
import logging.config

logging.config.fileConfig('logconf.conf', disable_existing_loggers=False)
# disable_existing_loggers=False kwargs allows other loggers to work alongside

# 'logconf.conf' defines a root and samplerLogger
# get root logger
root_logger = logging.getLogger()
# get sample logger
sampler_logger = logging.getLogger('samplerLogger')
print(root_logger, root_logger.handlers)
print(sampler_logger, sampler_logger.handlers)
root_logger.info('This is a debug message')
# sampler_logger.disabled = True # A logger can be disabled using this line
sampler_logger.warning('This is a debug message')
#%%
