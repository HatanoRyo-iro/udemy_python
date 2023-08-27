import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('section11/logtest.log')
logger.addHandler(h)


logger.debug('debug')