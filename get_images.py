from PIL import Image
import imagehash

def get_image_hash(image_path):
    try:
        with Image.open(image_path) as image:
            if image.mode != "RGBA":
                image = image.convert("RGBA")

            return imagehash.dhash(image)
    except OSError as e:
        print(f"Error: could not open file: {image_path} - {e}")
        return None
