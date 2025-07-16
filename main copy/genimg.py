from PIL import Image, ImageDraw, ImageFont

def generate_text_image(matrix, cell_size=20, font_size=12, output_file="images/matrix_output.png"):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create image canvas
    img_width = cols * cell_size
    img_height = rows * cell_size
    image = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Draw each character
    for y in range(rows):
        for x in range(cols):
            char = str(matrix[y][x])
            x_pos = x * cell_size + (cell_size - font_size) // 2
            y_pos = y * cell_size + (cell_size - font_size) // 2
            draw.text((x_pos, y_pos), char, fill="black", font=font)

    image.save(output_file)
    print(f"Image saved as '{output_file}'")

# Example matrix of letters and numbers
matrix = [
    ['A', '1', 'B', '2'],
    ['C', '3', 'D', '4'],
    ['E', '5', 'F', '6'],
    ['G', '7', 'H', '8']
]

#generate_text_image(matrix)
