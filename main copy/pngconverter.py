import os
from PIL import Image

def convert_folder_to_png(folder_path):
    # Supported image formats (you can add more if needed)
    supported_extensions = (".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp", ".jfif", ".heic")

    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(folder_path, filename)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(folder_path, base_name + ".png")

            try:
                with Image.open(input_path) as img:
                    # Convert if needed
                    if img.mode in ("RGBA", "P", "LA"):
                        img = img.convert("RGBA")
                    else:
                        img = img.convert("RGB")

                    img.save(output_path, "PNG")
                    print(f"✅ Converted: {filename} → {base_name}.png")
            except Exception as e:
                print(f"❌ Failed to convert {filename}: {e}")

# Usage
#convert_folder_to_png("images")
