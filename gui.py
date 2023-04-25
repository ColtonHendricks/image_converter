import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

# Create window
window = tk.Tk()
window.title("PNG to SVG Converter")
window.geometry("400x600")

# Add logo image
logo_img = Image.open("IMG_5684.png")
logo_img = logo_img.resize((481, 183), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(window, image=logo_img)
logo_label.pack(pady=20)

# Add message label
msg_label = tk.Label(window, text="Please choose a PNG to convert:", font=("Helvetica", 14))
msg_label.pack(pady=20)


# Open file dialog when button is clicked
def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        print(f"File selected: {file_path}")


# Add choose file button
choose_file_btn = tk.Button(window, text="Choose File", font=("Helvetica", 12), command=choose_file)
choose_file_btn.pack(pady=20)

# Add name entry label
name_label = tk.Label(window, text="Enter a name for the converted file:", font=("Helvetica", 14))
name_label.pack(pady=20)

# Add name entry widget
name_entry = tk.Entry(window, font=("Helvetica", 12))
name_entry.pack(pady=20)


# Function to convert PNG to SVG
def convert():
    # What to name the sketch
    sketch_name = name_entry.get() + ".png"

    # Reads imported image
    print(file_path)
    image = cv2.imread(file_path)

    # Convert RGB image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection algorithm to the grayscale image
    low_threshold = 90
    high_threshold = 150
    canny_edges = cv2.Canny(gray_image, low_threshold, high_threshold)

    # Invert the output of the Canny edge detection algorithm
    inverted_edges = 255 - canny_edges

    # Save binary image to computer
    cv2.imwrite(sketch_name, inverted_edges)

    # Feedback for user
    if cv2.imwrite(sketch_name, inverted_edges):
        print(f"{sketch_name} was saved successfully")
    else:
        print("The image was not saved successfully")


# Add convert button
convert_btn = tk.Button(window, text="Convert PNG to SVG", font=("Helvetica", 12), command=convert)
convert_btn.pack(pady=20)

# Start window event loop
window.mainloop()

