import svgwrite
from PIL import Image
import io
import base64

file_name = input("What file do you want to convert?: ")
svg_name = input("What do you want the resulting file to be called?: ")
# Load the PNG image
png_image = Image.open(file_name).convert("RGBA")

# Create a new SVG file and add the image as a background
svg_image = svgwrite.Drawing(svg_name, size=png_image.size)
svg_image.add(svg_image.rect(insert=(0, 0), size=png_image.size, fill="rgb(255, 255, 255)"))
buffered = io.BytesIO()
png_image.save(buffered, format="PNG")
png_data = buffered.getvalue()
svg_image.add(svg_image.image(href="data:image/png;base64," + base64.b64encode(png_data).decode("utf-8"),
                              insert=(0, 0), size=png_image.size))

# Save the SVG file
svg_image.save()

print("PNG to SVG conversion complete.")
