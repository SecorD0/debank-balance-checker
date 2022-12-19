import logging

from data.config import ERRORS_FILE

logging.basicConfig(
    handlers=(logging.FileHandler(ERRORS_FILE),),
    level=logging.INFO,
    format=u'%(asctime)s\n%(filename)s, line %(lineno)d\n%(message)s\n------------------------',
    datefmt='%d.%m.%y %H:%M:%S'
)
