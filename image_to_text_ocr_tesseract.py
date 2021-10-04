# watch this video for more info and demonstration
# https://youtu.be/OT_z3PI3DQQ

## CODE STARTS ##

# install these modules:
# pip install opencv-python
# pip install pillow
# pip install pytesseract

#  os module is inbuilt


# Now import the modules
import os
import cv2
import pytesseract
from PIL import Image

# specify the path of the input image and the tesseract engine executable
# replace this with the path of your image and tesseract executable ....
image_path=r'G:\Images\image1.png'
tess_exe_path=r'I:\OCR\tesseract.exe'

# to get tesseract executable , watch this video :
# https://youtu.be/344Bit3kWE8

image=cv2.imread(image_path) # read the input image
pytesseract.pytesseract.tesseract_cmd= tess_exe_path # tell the computer where the tesseract executable is located
grayscale_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Convert the image to black and white for better processing
cv2.medianBlur(grayscale_image,3) # blur the image for better processing


# write a temporary file where we will store the black and white image and later we will delete it
temporary_file="{}.jpg".format(os.getpid())  # get a name for saving the black and white file temporarily
cv2.imwrite(temporary_file,grayscale_image) # save the black and white file temporarily

text=pytesseract.image_to_string(Image.open(temporary_file))  # image to text conversion

os.remove(temporary_file) # delete the black and white image file

print(text) # print the text that we obtained after processing