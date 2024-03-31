import logging
import logging.config
import yaml

with open('logyamlconfig.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

root_logger = logging.getLogger(__name__)
sample_logger = logging.getLogger('sampleLogger')

root_logger.debug('This is a debug message')
sample_logger.info('This is an info message')