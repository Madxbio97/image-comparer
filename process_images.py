import os
from collections import defaultdict
import uuid
from get_images import get_image_hash


def generate_unique_path(path):
    unique_id = str(uuid.uuid4())[:8]
    return f"{path}_{unique_id}"


def process_image(first_dir, second_dir):
    second_hashes = {}

    for filename in os.listdir(second_dir):
        file_path = os.path.join(second_dir, filename)

        hash_value = get_image_hash(file_path)

        if hash_value is not None:
            second_hashes[filename] = hash_value

    renames = defaultdict(list)

    for filename in os.listdir(first_dir):
        first_file_path = os.path.join(first_dir, filename)

        hash_value = get_image_hash(first_file_path)

        if hash_value is not None:
            for second_filename, second_hash in second_hashes.items():
                if abs(hash_value - second_hash) <= 5:
                    renames[first_file_path].append(second_filename)

    for old_path, new_names in renames.items():
        for new_name in new_names:
            new_path = os.path.join(os.path.dirname(old_path), new_name)

            while os.path.exists(new_path):
                new_path = generate_unique_path(new_path)

            os.rename(old_path, new_path)
