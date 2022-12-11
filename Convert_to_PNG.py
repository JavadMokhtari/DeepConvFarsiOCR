import os
from PIL import Image


# Function for convert images format to PNG
def ConvertToPNG(images_path, new_path):
    # Create a new directory for save new images
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # Get all existing names of images
    fnames = os.listdir(images_path)
    # Save images with new format .png in each class folder
    for fname in fnames:
        if '.bmp' in fname:
            # Split the class number from image file
            class_num = fname.split('.bmp')[0].split('_')[1]
            class_path = os.path.join(new_path, class_num)
            if not os.path.exists(class_path):
                os.makedirs(class_path)
            # Save image in its class path
            try:
                path_storage = os.path.join(class_path, fname[:-4] + '.png')
                img_path = os.path.join(images_path, fname)
                Image.open(img_path).save(path_storage)
            except:
                print('Error occurred while saving')

if __name__=='__main__':
    ConvertToPNG('PDB-Test', 'Test-Data')
    ConvertToPNG('PDB-Train', 'Train-Data')