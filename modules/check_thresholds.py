from thresholds.thresholds import THRESHOLDS


def check_thresholds(metrics):
    for metric in THRESHOLDS:
        if metric == 'PSNR' and metrics[metric] == float('inf'):
            continue

        min_val = THRESHOLDS[metric]['min']
        max_val = THRESHOLDS[metric]['max']
        if not (min_val <= metrics[metric] <= max_val):
            return False
    return True
