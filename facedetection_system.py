import cv2
import numpy as np

# Load an image
image = cv2.imread('face.jpg')

# Convert to grayscale using NumPy
gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Normalize pixel values between 0 and 1
normalized = gray / 255.0

# Resize image using NumPy slicing
resized = normalized[::2, ::2]

# Display the original and resized image
cv2.imshow("Original", image)
cv2.imshow("Processed", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
