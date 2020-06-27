import os
from PIL import Image


input_keyboard = input(r"directory: ")


def img_compressor(input_path,name_of_new_folder,end_name,image_quality,output_extension):


    for folder in os.listdir(input_path):
        os.mkdir(input_path+"/"+folder+"/"+name_of_new_folder)  
        #create folder for compressed images
        counter = 0
        print("folder: "+folder+" finished")    
        
        for file in os.listdir(input_path +"/"+folder):
            counter = counter + 1
            filename, file_extension = os.path.splitext(file)

            if (file_extension == ".JPG" or file_extension == ".png" or file_extension == ".jpeg" or file_extension == ".jpg"):
                #add some more extensions if needed
                big_image = Image.open(input_path+"/"+folder+"/"+file)
                converted_image = big_image.save(input_path+"/"+folder+"/"+name_of_new_folder+"/"+folder+"-"+str(counter)+"-"+end_name+"."+output_extension,quality=image_quality)
                #quality from 0-100
            

img_compressor(input_keyboard,"aonvertiert"," knv",1,"jpeg")

print("********finished********")

