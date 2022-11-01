import cv2

# What to name the sketch
sketch_name = input("What would you like to call the saved sketch?: ")
# Reads imported image. You need to type it here manually for now
path = r"C:\Users\colton hendricks\Pictures\Saved Pictures\pic of me.jpg"
print(path)
image = cv2.imread(path)

# Convert RGB image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image inversion
inverted_image = 255 - gray_image

# Create the pencil sketch
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=265.0)

# Save pencil sketch to computer
cv2.imwrite(sketch_name, pencil_sketch)

# Feedback for user
if cv2.imwrite(sketch_name, pencil_sketch):
    print(f"{sketch_name} was saved successfully")
else:
    print("The image was not saved successfully")
