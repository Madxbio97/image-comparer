import os
from thresholds import THRESHOLDS


def check_thresholds(metrics):
    for metric in THRESHOLDS:
        if metric == 'PSNR' and metrics[metric] == float('inf'):
            continue

        min_val = THRESHOLDS[metric]['min']
        max_val = THRESHOLDS[metric]['max']
        if not (min_val <= metrics[metric] <= max_val):
            return False
    return True


def move_image(src_path, dst_path, new_name=None):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    if new_name is None:
        new_name = os.path.basename(src_path)

    dst_file = os.path.join(dst_path, new_name)
    os.rename(src_path, dst_file)
