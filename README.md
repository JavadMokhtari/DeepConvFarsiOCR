# DeepConvFarsiOCR
**Implementation of A Deep Convolutional Approach Toward Farsi Character Recognition in Python** <br />Used for both machine printed and handwritten datasets.

# Papers

  - [From machine generated to handwritten character recognition; a deep learning approach](http://ieeexplore.ieee.org/document/7983055/)


## Usage

#### Step 1: Data
  - Download all images from [this link](https://www.mediafire.com/?jh9puuz96ihjuza).
  - Extract them to the home directory of this repository. After this, you should see  `PDB-Train` and `PDB-Test` folders in your home directory.

  - Execute `Convert_to_PNG.py` with the following parameters in another way:
  ```
  python Convert_to_PNG.py --images_dir 'PDB-Train' --dir_to_save 'Train-Data'
  ```
  and
  ```
  python Convert_to_PNG.py --images_dir 'PDB-Test' --dir_to_save 'Test-Data'
  ```
  - These commands will
    - Convert all downloaded bpm images into PNG and store them in the new directory.
    - extract labels from file names and store images of each class in a separate directory.

> Note that all directories given as parameter should NOT include any `/` in them.

#### Step 2: Train
  - run `th cnn.v2.lua --progress`. See the source file for more commands and options.

> Always use the `--id` parameter. This name will be used to store the model and logs.
