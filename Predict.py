from PIL import Image
from tensorflow import keras
from numpy import array
from os.path import join, normpath
from sys import argv


def predict(directories):
    # Manage input arguments
    if '--img_dir' in directories:
        img_dir = normpath(directories[directories.index('--img_dir')+1])
    else:
        print("Enter your image directory to predict!")
        return
    if '--saved_model_dir' in directories:
        saved_model_dir = normpath(directories[directories.index('--saved_model_dir')+1])
    else:
        print("Enter your saved model directory!")
        return

    # Labels of data
    class_values = [
        ("ا", 0),
        ("ب", 1),
        ("پ", 12),
        ("ت", 23), 
        ("ث", 30),
        ("ج", 31),
        ("چ", 32),
        ("ح", 33),
        ("خ", 34),
        ("د", 35),
        ("ذ", 2),
        ("ر", 3),
        ("ز", 4),
        ("ژ", 5),
        ("س", 6),
        ("ش", 7),
        ("ص", 8),
        ("ض", 9),
        ("ط", 10),
        ("ظ", 11),
        ("ع", 13),
        ("غ", 14),
        ("ف", 15),
        ("ق", 16),
        ("ک", 17),
        ("گ", 18),
        ("ل", 19),
        ("م", 20),
        ("ن", 21),
        ("و", 22),
        ("ه", 24),
        ("ی", 25),
        ("ئـ",26),
        ("آ", 27),
        ("هـ",28),
        ("ـه",29)]
    
    # import image as a numpy array
    img = Image.open(img_dir).convert('L').resize((30, 30))
    sample = array(img)

    # Load model
    ocr_model = keras.models.load_model(saved_model_dir)

    # Predict one sample of data
    pred = ocr_model.predict(sample.reshape((1, 30, 30, 1))).round(3).argmax()
    for letter, value in class_values:
        if pred == value:
            predicted_letter = letter
    print("\n\n--------------------------------")
    print(pred)
    print(f"$ The predicted letter is: {predicted_letter}")
    return True

if __name__=="__main__":
    predict(argv[1:])

