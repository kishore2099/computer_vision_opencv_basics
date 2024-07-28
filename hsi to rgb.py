import cv2
import numpy as np

def hsi_to_rgb(h, s, i):
    h = float(h)
    s = float(s)
    i = float(i)

    if h >= 0 and h < 120:
        b = i * (1 - s)
        r = i * (1 + (s * np.cos(np.radians(h)) / np.cos(np.radians(60 - h))))
        g = 3 * i - (r + b)
    elif h >= 120 and h < 240:
        h = h - 120
        r = i * (1 - s)
        g = i * (1 + (s * np.cos(np.radians(h)) / np.cos(np.radians(60 - h))))
        b = 3 * i - (r + g)
    else:
        h = h - 240
        g = i * (1 - s)
        b = i * (1 + (s * np.cos(np.radians(h)) / np.cos(np.radians(60 - h))))
        r = 3 * i - (g + b)

    r = np.clip(r * 255, 0, 255)
    g = np.clip(g * 255, 0, 255)
    b = np.clip(b * 255, 0, 255)

    return [int(r), int(g), int(b)]

def convert_hsi_to_rgb(image):
    rows, cols, _ = image.shape
    rgb_image = np.zeros((rows, cols, 3), dtype=np.uint8)

    for row in range(rows):
        for col in range(cols):
            h, s, i = image[row, col].astype(float)
            h = h * 360 / 255  # Scale H from [0, 255] to [0, 360]
            s = s / 255        # Scale S from [0, 255] to [0, 1]
            i = i / 255        # Scale I from [0, 255] to [0, 1]
            rgb_image[row, col] = hsi_to_rgb(h, s, i)
    
    return rgb_image

def count_rgb_pixels(image):
    red_count = np.sum(np.all(image == [255, 0, 0], axis=2))
    green_count = np.sum(np.all(image == [0, 255, 0], axis=2))
    blue_count = np.sum(np.all(image == [0, 0, 255], axis=2))
    return red_count, green_count, blue_count

# Load HSI image
hsi_image = cv2.imread('C:/Users/kisho/Downloads/opencv black and white/upload/HSI_Image.png', cv2.IMREAD_COLOR)

# Convert HSI image to RGB
rgb_image = convert_hsi_to_rgb(hsi_image)

# Save the RGB image
cv2.imwrite('rgb_image.png', rgb_image)

# Count red, green, and blue pixels
red_count, green_count, blue_count = count_rgb_pixels(rgb_image)

# Print the results
print(f'Number of red pixels: {red_count}')
print(f'Number of green pixels: {green_count}')
print(f'Number of blue pixels: {blue_count}')
