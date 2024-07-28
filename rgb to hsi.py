import cv2
import numpy as np

def rgb_to_hsi(r, g, b):
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    i = (r + g + b) / 3.0

    min_val = min(r, g, b)
    s = 1 - (min_val / i) if i != 0 else 0

    if s == 0:
        h = 0
    else:
        if r == g == b:
            h = 0
        else:
            num = 0.5 * ((r - g) + (r - b))
            denom = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
            theta = np.arccos(num / denom) if denom != 0 else 0
            if b <= g:
                h = theta
            else:
                h = 2 * np.pi - theta

    h = np.degrees(h)
    if h < 0:
        h += 360

    return h, s, i

def convert_rgb_to_hsi(image):
    rows, cols, _ = image.shape
    hsi_image = np.zeros((rows, cols, 3), dtype=np.float32)

    for row in range(rows):
        for col in range(cols):
            r, g, b = image[row, col]
            h, s, i = rgb_to_hsi(r, g, b)
            hsi_image[row, col] = [h, s, i]
    
    return hsi_image

def calculate_total_hsi(hsi_image):
    total_h = np.sum(hsi_image[:, :, 0])
    total_s = np.sum(hsi_image[:, :, 1])
    total_i = np.sum(hsi_image[:, :, 2])
    return total_h, total_s, total_i

# Load RGB image
rgb_image = cv2.imread('C:/Users/kisho/Downloads/opencv black and white/upload/coloured_image.jpeg', cv2.IMREAD_COLOR)

# Convert RGB image to HSI
hsi_image = convert_rgb_to_hsi(rgb_image)

# Calculate total H, S, and I values
total_h, total_s, total_i = calculate_total_hsi(hsi_image)

# Print the total H, S, and I values
print(f'Total H value: {total_h}')
print(f'Total S value: {total_s}')
print(f'Total I value: {total_i}')
