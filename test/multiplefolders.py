import os
from PIL import Image

#quality from 0-100
image_quality = 50
output_extension = "jpeg"

input_keyboard = input(r"directory: ")
input_path = input_keyboard

#create folder for compressed images


#search for JPGS,PNGS

for ordner in os.listdir(input_path):
    aa = os.mkdir(input_path+"/"+ordner+"/converted")
    print(aa)
    for file in os.listdir(input_path + "/" +ordner):
        filename, file_extension = os.path.splitext(file)
        if (file_extension == ".JPG" or file_extension == ".png" or file_extension == ".jpeg" or file_extension == ".jpg"):
            big_image = Image.open(input_path+"/"+ordner+"/"+file)
            converted_image = big_image.save(input_path+"/"+ordner+"/converted/"+filename+"-small."+output_extension,quality=image_quality)

for ordner in os.listdir(input_keyboard):
    print(ordner)
    for file in os.listdir(input_path + "/"+ordner):
        print("test"+file)
print("finished")
