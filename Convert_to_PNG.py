import os
from random import randint
from sys import argv
from PIL import Image


# Function for convert images format to PNG
def ConvertToPNG(directories):
    if '--images_dir' in directories:
        images_dir = directories[directories.index('--images_dir')+1]
    else:
        print("Enter images data directory!")
        return
    if '--dir_to_save' in directories:
        dir_to_save = directories[directories.index('--dir_to_save')+1]
    else:
        dir_to_save = 'Converted-Images-' + str(randint(0, 100))

    # Create a new directory for save new images
    if not os.path.exists(dir_to_save):
        os.makedirs(dir_to_save)
    # Get all existing names of images
    fnames = os.listdir(images_dir)
    # Save images with new format .png in each class folder
    for fname in fnames:
        if '.bmp' in fname:
            # Split the class number from image file
            class_num = fname.split('.bmp')[0].split('_')[1]
            class_path = os.path.join(dir_to_save, class_num)
            if not os.path.exists(class_path):
                os.makedirs(class_path)
            # Save image in its class path
            try:
                path_storage = os.path.join(class_path, fname[:-4] + '.png')
                img_path = os.path.join(images_dir, fname)
                Image.open(img_path).save(path_storage)
            except:
                print('Error occurred while saving')

if __name__=='__main__':
    ConvertToPNG(argv[1:])
