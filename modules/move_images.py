import os

def move_image(src_path, dst_path, new_name=None):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    if new_name is None:
        new_name = os.path.basename(src_path)

    dst_file = os.path.join(dst_path, new_name)
    os.rename(src_path, dst_file)