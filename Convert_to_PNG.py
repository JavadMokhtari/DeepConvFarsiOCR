import os
from PIL import Image


# Function for convert images format to PNG
def ConvertToPNG(img_path, new_path):
    # Create a new directory for save new images
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # Get all existing names of images
    fnames = os.listdir(img_path)
    # Save images with new format .png in each class folder
    for fname in fnames:
        if '.bmp' in fname:
            # Split the class number from image file
            class_num = fname.split('.bmp')[0].split('_')[1]
            class_path = new_path + class_num + '/'
            if not os.path.exists(class_path):
                os.makedirs(class_path)
            # Save image in its class path
            try:
                Image.open(img_path + fname).save(class_path + fname[:-4] + '.png')
            except:
                print('Error occurred while saving')


ConvertToPNG('PDB-Test/', 'Test-Data/')
ConvertToPNG('PDB-Train/', 'Train-Data/')