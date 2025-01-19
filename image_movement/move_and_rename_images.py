import os
import shutil
from logs.process_logs import logger
from constants.DIR import HR_DIR


def move_and_rename_image(src_file, dest_dir, new_name):
    src_path = os.path.join(HR_DIR, src_file)
    dest_path = os.path.join(dest_dir, new_name)
    shutil.move(str(src_path), str(dest_path))
    logger.info(f"The image was moved and renamed: {src_file} -> {new_name}")
