import logging.config


logging.config.fileConfig('section11/logging.ini')
logger = logging.getLogger(__name__)
# logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')