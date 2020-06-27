  
import os
from PIL import Image

#quality from 0-100
image_quality = 50
output_extension = "jpeg"

input_keyboard = input(r"directory: ")
input_path = input_keyboard

#create folder for compressed images
os.mkdir(input_path+"/converted")

#search for JPGS,PNGS

for file in os.listdir(input_path):
    filename, file_extension = os.path.splitext(file)
    if (file_extension == ".JPG" or file_extension == ".png" or file_extension == ".jpeg"):
        big_image = Image.open(input_path+"/"+file)
        converted_image = big_image.save(input_path+"/converted/"+filename+"-small."+output_extension,quality=image_quality)

print("finished")
