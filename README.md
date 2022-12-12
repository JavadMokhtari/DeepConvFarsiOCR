# DeepConvFarsiOCR
**Implementation of A Deep Convolutional Approach Toward Farsi Character Recognition in Python** <br />Used for both machine printed and handwritten datasets.

# Papers

  - [From machine generated to handwritten character recognition; a deep learning approach](http://ieeexplore.ieee.org/document/7983055/)


## Usage

#### Step 1: Data
  - Download all images from [this link](https://www.mediafire.com/?jh9puuz96ihjuza) and extract them.

  - Execute `Convert_to_PNG.py` with the following parameters:
  ```
  python Convert_to_PNG.py --images_dir 'PATH-TO-IMAGES-FOLDER' --dir_to_save 'PATH-TO-NEW-DIRECTORY'
  ```
  * Like the following command:
  ```
  python Convert_to_PNG.py --images_dir 'PDB-Train/' --dir_to_save 'Train-Data/'
  ```
  - Run this command for both `PDB-Train` and `PDB-Test` folders. These will:
    - Convert all downloaded bpm images into png and store them in the new directory.
    - extract labels from file names and store images of each class in a separate directory.

#### Step 2: Train
  - There are two models `PersianOCR.Plain.v1.py` and `PersianOCR.v2.py`. Run one of them with the following parameters:
  ```
  python OCR-MODEL-FILE.py --train_data_dir 'PATH-TO-CLASSIFIED-TRAIN-DATA' --epochs NO-EPOCHS --model_storage_dir 'PATH-FOR-SAVE-MODEL'
  ```
  * Example:
  ```
  python PersianOCR.Plain.v1.py --train_data_dir 'Train-Data/' --epochs 10 --model_storage_dir 'models/'
  ```
  > The `--epochs` and `--model_storage_dir` arguments is **optional** but `--train_data_dir` is **required**
  
#### Step 3: Predict
  -- Run `Predict.py` module like the below command:
  ```
  python Predict.py --img_dir 'PATH-TO-AN-IMAGE' --saved_model_dir 'PATH-TO-A-SAVED-MODEL'
  ```
  * Example:
  ```
  python Predict.py --img_dir 'Test-Data/0/100_0.png' --saved_model_dir 'models/ocr_model_v1.h5'
  ```
