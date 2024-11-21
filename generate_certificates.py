import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the Excel file with participants' names
df = pd.read_excel("name_list.xlsx")

# Load the template image
template = Image.open("templates/certificate.png")  # Updated path for the template

# Define the font and size
font = ImageFont.truetype("fonts/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf", 50)  # Updated path for the font

# Define the position where the name will appear (adjust as needed)
name_position = (40, 340)  # Example coordinates; adjust based on your template (top left corner coordiantes 0,0)

# Create 'certificates' directory if it doesn't exist
output_dir = "certificates"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each participant in the Excel file with column named "Name"
for index, row in df.iterrows():
    name = row["Name"]

    # Open a copy of the template for each certificate
    cert = template.copy()
    draw = ImageDraw.Draw(cert)

    # Add the name to the certificate
    draw.text(name_position, name, font=font, fill="#121212")  # Adjust color and position as needed

    # Save the certificate with the participant's name
    cert.save(f"{output_dir}/{name}_certificate.png")

print("Certificates generated successfully!")

