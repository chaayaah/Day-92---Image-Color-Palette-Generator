import numpy as np
from PIL import Image

# Read in image file
img = Image.open('Test_1.jpg')

# Convert image to NumPy array
img_arr = np.array(img)

# Print shape of array (dimensions of matrix)
print(img_arr.shape)

# Print first 5 rows and columns of array (first 5x5 pixels of image)
print(img_arr[:5, :5])