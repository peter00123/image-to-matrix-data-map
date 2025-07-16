
from PIL import Image
from resize import resize_image
from pngconverter import convert_folder_to_png






# Convert images in the 'images' folder to PNG format
convert_folder_to_png("input")

image = Image.open('input/img.png')
resize_image(image, 'images/resized.png', max_size=100)

image = Image.open('images/resized.png') 
greyscale_image = image.convert('L')

greyscale_image.save('images/img_greyscale.png')

#greyscale_image.show()

sorted_chars = [
    ' ', 
    'i',  'T', 'F',  '3', 'Z', 'K', 'N',
    'H', 'A', 'X',  'U', 'M', '5', 'B',  'R', 
    'G', '0', '8',  'W'
]
from PIL import Image

# Open the image
image = Image.open('images/img_greyscale.png')  # Replace with your image file
pixels = image.load()

width, height = image.size
finalimage = []
for y in range(height):
    for x in range(width):
        pixel_value = pixels[x, y]
        if pixel_value > 200:
            finalimage.append(sorted_chars[0])  # blank
        elif pixel_value < 30:
            finalimage.append('w')  # or sorted_chars[-1] if 'w' is last
        else:
            # Map the pixel value to the sorted_chars range (excluding first and last)
            idx = int((pixel_value - 30) / (170 / (len(sorted_chars) - 2))) + 1
            idx = min(idx, len(sorted_chars) - 2)
            finalimage.append(sorted_chars[idx])

for i in range(0, len(finalimage), width):
    print(''.join(finalimage[i:i + width]))

matrix_2d = []
for i in range(0, len(finalimage), width):
    row = finalimage[i:i + width]
    matrix_2d.append(row)

print("start to generate image from matrix")
#    print(''.join(row)) 
"""
print("Matrix 2D:")
for row in matrix_2d:
    print(''.join(row))     

print(matrix_2d)
"""
from genimg import generate_text_image
generate_text_image(matrix_2d, cell_size=20, font_size=12, output_file="images/matrix_output.png")
print("Image generated from matrix.")

from PIL import Image, ImageOps

# Open the image
img = Image.open('images/matrix_output.png')

# Invert the image colors
inverted_img = ImageOps.invert(img.convert('RGB'))

# Save the result
inverted_img.save('final_output.png')


# Open the image
img = Image.open('final_output.png')

# Rotate the image by 90 degrees (counterclockwise)
rotated_img = img.rotate(0, expand=True)

# Save the rotated image
rotated_img.save('final_output.png')    
