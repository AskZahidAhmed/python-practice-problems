import cv2
import numpy as np

def remove_background(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Create a mask initialized as background
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define the background and foreground models
    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    # Define the rectangle enclosing the foreground object
    rectangle = (1, 1, image.shape[1] - 1, image.shape[0] - 1)

    # Apply GrabCut algorithm to extract foreground
    cv2.grabCut(image, mask, rectangle, background_model, foreground_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask where 0 and 2 pixels are considered background, while 1 and 3 are considered foreground
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the image to remove the background
    image = image * mask[:, :, np.newaxis]

    # Return the resulting image
    return image


# Example usage
input_image = 'Screenshot from 2023-03-19 20-31-42.png'
output_image = 'output_image.png'

result = remove_background(input_image)
cv2.imwrite(output_image, result)
print("Background removed successfully and saved as", output_image)

