from PIL import Image
import os

def check_and_convert_image(image_path):
    """Checks if an image is in JPG format and converts it from PNG or JPEG if needed."""

    filename, extension = os.path.splitext(image_path)
    extension = extension.lower()

    print(extension)
    if extension == '.jpg':
        print(f"Image '{image_path}' is already in JPG format.")
        return image_path

    if extension in ('.png', '.jpeg'):
        try:
            with Image.open(image_path) as img:
                img = img.convert('RGB')  # Ensure RGB mode for JPG conversion
                jpg_path = filename + '.jpg'
                img.save(jpg_path, 'jpg')
                print(f"Image converted to JPG and saved as '{jpg_path}'.")
                return jpg_path
        except Exception as e:
            print(f"Error converting image: {e}")
    else:
        print(f"Unsupported image format: {extension}")

# check_and_convert_image('notebook/samples/lynaeydofd_fr0.jpg')