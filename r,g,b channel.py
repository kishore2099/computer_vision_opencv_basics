import cv2
import numpy as np

def calculate_total_rgb(image):
    total_r = np.sum(image[:, :, 2])  # Red channel
    total_g = np.sum(image[:, :, 1])  # Green channel
    total_b = np.sum(image[:, :, 0])  # Blue channel
    return total_r, total_g, total_b

# Load the colored image
image_path = 'C:/Users/kisho/Downloads/opencv black and white/upload/coloured_image.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Could not open or find the image at {image_path}")
    exit()

# Calculate total R, G, and B values
total_r, total_g, total_b = calculate_total_rgb(image)

# Print the total R, G, and B values
print(f'Total R value: {total_r}')
print(f'Total G value: {total_g}')
print(f'Total B value: {total_b}')
