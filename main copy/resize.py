from PIL import Image , ImageOps

def resize_image(input_path, output_path, max_size=100):


    img = Image.open('input/img.png')

 

    # Get original dimensions
    original_width, original_height = img.size

    # Calculate scaling factor
    scale = min(max_size / original_width, max_size / original_height)

    # If image is already below max size, just save it
    if scale >= 1:
        print("Image is already smaller than the max size.")
        img.save(output_path)
        return
    rotated = img.rotate(90, expand=True)  # or rotate(270)

    # Calculate new size
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    # Resize and save
# ...existing code...
    # Resize and save
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_img.save(output_path)
    print(f"Image resized and saved as '{output_path}' ({new_width}x{new_height})")
# ...existing code...

# Example usage
#resize_image("img.png", "resized.png", max_size=1000)


