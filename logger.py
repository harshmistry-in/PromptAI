import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(module)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s'))

logger.addHandler(console_handler)