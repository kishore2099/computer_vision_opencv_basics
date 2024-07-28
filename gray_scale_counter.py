import cv2

# Define the image path
image_path = ('C:/Users/kisho/Downloads/opencv black and white/upload/lenna.png')

# Load the image in grayscale mode
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print(f"Error: Could not open or find the image at {image_path}")
    exit()

# Define thresholds for black and white pixels
black_threshold = 0
white_threshold = 255

# Count the number of black and white pixels
num_black_pixels = (image == black_threshold).sum()
num_white_pixels = (image == white_threshold).sum()

# Print the results
print(f'Number of black pixels: {num_black_pixels}')
print(f'Number of white pixels: {num_white_pixels}')
