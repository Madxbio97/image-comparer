def is_match(metrics, thresholds):
    for metric, value in metrics.items():
        min_threshold, max_threshold = thresholds.get(metric, (0, float('inf')))
        if not (min_threshold <= value <= max_threshold):
            return False
    return True


def format_metrics(metrics):
    result_str = '\n'.join([f'{metric}: {value:.4f}' for metric, value in metrics.items()])
    return result_str
