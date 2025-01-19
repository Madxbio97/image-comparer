import os
from PIL import Image
from logs.process_logs import logger


def load_images(directory):
    images = []
    files = os.listdir(directory)

    target_format = 'PNG'

    for file_name in files:
        try:
            image_path = os.path.join(directory, file_name)
            img = Image.open(image_path)

            if img.format != target_format:
                raise ValueError(f"Формат изображения {img.format} не совпадает с целевым форматом {target_format}.")

            img = img.convert("RGBA")
            images.append((file_name, img))
        except Exception as e:
            logger.error(f"Ошибка при загрузке изображения {file_name}: {e}")

    return images
