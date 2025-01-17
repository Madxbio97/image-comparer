from logging import getLogger, StreamHandler, Formatter, FileHandler, INFO

# Настройки логгирования
logger = getLogger(__name__)
logger.setLevel(INFO)
stream_handler = StreamHandler()
stream_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
file_handler = FileHandler('image_matching.log')
file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
