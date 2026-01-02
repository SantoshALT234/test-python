from PIL import Image
import sys

# We need the image file to know where to place the dots.
# Ensure 'image_b49c4b.jpg' is in the same folder as this script.
image_path = "Ana-de-Armas-5.jpg"

def image_to_dots(path, width=100):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: I cannot find '{path}'. Make sure the photo is in this folder.")
        return

    # 1. Convert to grayscale (black and white)
    img = img.convert("L")

    # 2. Resize it so it fits on your screen
    # We maintain the aspect ratio (height vs width)
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)) * 0.55) # 0.55 corrects for line height
    img = img.resize((width, h_size), Image.Resampling.LANCZOS)

    # 3. Build the dot image
    pixels = img.getdata()
    dot_string = ""
    
    width_counter = 0
    for pixel in pixels:
        # If the pixel is dark (less than 128), we draw a dot '.'
        # If the pixel is light, we draw a space ' '
        if pixel < 128:  
            dot_string += "."
        else:
            dot_string += " "
            
        width_counter += 1
        
        # When we reach the edge of the image, start a new line
        if width_counter == width:
            dot_string += "\n"
            width_counter = 0

    # 4. Print the final result
    print(dot_string)

# Run the function
image_to_dots(image_path, width=120)