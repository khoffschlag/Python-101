from PIL import Image, ImageTk
import tkinter as tk

"""
Task: Extend get_pixel_color method in such a way, that not only RGB values but a real color name
will be printed! If not the exact color is in colors, print the closest one!
"""

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

def get_pixel_color(event):
    # Get the coordinates of the click event
    x, y = event.x, event.y

    # Get the RGB value at the clicked point
    pixel = img.getpixel((x, y))

    # Find the closest color from the colors dictionary
    closest_color = None
    min_distance = float('inf')
    for name, rgb in colors.items():
        # Calculate the Euclidean distance between the pixel color and the dictionary color
        distance = ((pixel[0] - rgb[0]) ** 2) + ((pixel[1] - rgb[1]) ** 2) + ((pixel[2] - rgb[2]) ** 2)
        distance = distance ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_color = name

    # Print the closest color
    print(f"Closest color at ({x}, {y}): {closest_color}")

# Load the image
image_path = "example_image.jpg"  # Replace with the path to your image
img = Image.open(image_path)

# Create a tkinter window
window = tk.Tk()

# Resize the window to fit the image
window.geometry(f"{img.width}x{img.height}")

# Create a canvas to display the image
canvas = tk.Canvas(window, width=img.width, height=img.height)
canvas.pack()

# Convert the PIL image to Tkinter format and display it on the canvas
tk_image = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Bind the left mouse click event to the canvas
canvas.bind("<Button-1>", get_pixel_color)

# Start the tkinter event loop
window.mainloop()
