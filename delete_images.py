import os
import errno

from CONSTANTS import LR_DIR, HR_DIR
from process_logs import logger


# Удаление изображений из директорий LR и HR
def delete_images(lr_file, hr_file):
    lr_path = os.path.join(LR_DIR, lr_file)
    hr_path = os.path.join(HR_DIR, hr_file)
    try:
        os.remove(lr_path)
        os.remove(hr_path)
    except OSError as e:
        if e.errno == errno.ENOENT:
            logger.warning(
                f"Файл {hr_file} уже удалён из директории HR_DIR, поэтому удаление файла из LR_DIR продолжается.")
            logger.info(f"Удалены изображения: {lr_file}, {hr_file}")
        else:
            logger.error(f"Ошибка при удалении изображения {lr_file}: {e}")
