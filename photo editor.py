#read many images
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load and display image 1
image_1 = Image.open("C:\\Users\\amalh\\OneDrive - MSFT\\Desktop\\Downloaded Images\\adorable-fluffy-cat-laying-down_Caroly_Shutterstock-407128867.jpg")   
plt.imshow(image_1)
plt.title("Image 1")
plt.show()

# Load and display image 2
image_2 = Image.open("C:\\Users\\amalh\\OneDrive - MSFT\\Desktop\\Downloaded Images\\dilute-tortoiseshell-cat_Mary-Swift_Shutterstock-1101316464.jpg")   
plt.imshow(image_2)
plt.title("Image 2")
plt.show()

# Load and display image 3
image_3 = Image.open("C:\\Users\\amalh\\OneDrive - MSFT\\Desktop\\Downloaded Images\\pexels-cottonbro-4709285.jpg")   
plt.imshow(image_3)
plt.title("Image 3")
plt.show()

# Load and display image 4
image_4 = Image.open("C:\\Users\\amalh\\OneDrive - MSFT\\Desktop\\Downloaded Images\\pexels-photo-326875-1219471917.jpeg")   
plt.imshow(image_4)
plt.title("Image 4")
plt.show()
#make sure to install Pillow library
