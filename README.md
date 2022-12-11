# DeepConvFarsiOCR
A Deep Convolutional Approach Toward Farsi Character Recognition. Used for both machine printed and handwritten datasets.
This fork illustrates an implementation of following paper in Python.

# Papers

  - [From machine generated to handwritten character recognition; a deep learning approach](http://ieeexplore.ieee.org/document/7983055/)


## Usage

#### Step1: Data
  - Download all images from [this link](https://www.mediafire.com/?jh9puuz96ihjuza).
  - Extract them to the home directory of this repository. After this, you should see  `PDB-Train` and `PDB-Test` folders in your home directory.
  - Simply execute `Convert_to_PNG.py` to start converting images:
  ```
  python3 Convert_to_PNG.py
  ```
  - Or execute `Convert_to_PNG.py` with the following parameters in another way:
  ```
  python3 Convert_to_PNG.py 'ConvertToPNG()' 'DOWNLOADED-PDB-Train-DIRECTORY' 'NEW-DIERCTORY-TO-STORAGE-TRAIN'
  ```
  and
  ```
  python3 Convert_to_PNG.py 'ConvertToPNG()' 'DOWNLOADED-PDB-Test-DIRECTORY' 'NEW-DIERCTORY-TO-STORAGE-TEST'
  ```
  - These commands will
    - Convert all downloaded bpm images into PNG and store them in new directory.
    - extract labels from file names and store images of each class in a separate directory.

> Note that all files paths given to `--src` and `--dest` should be RELATIVE and should NOT include any `/` in them.

#### Step2: Data Sourcing
  This step converts the raw data stored in binary files to [`dp:DataSource`](https://github.com/nicholas-leonard/dp/blob/master/data/datasource.lua). This operation is done using `data.source.lua` and it is called internally by `cnn.v2.lua`. Hence, it cannot accepts parameters and should be manually adjusted. [The following parameters](https://github.com/Kianenigma/DeepConvFarsiOCR/blob/master/cnn.v2.data.source.lua#L51) are important:
  ```
  local validRatio = .5
  local train_bin = './PDB_Train.bin'
  local test_bin = './PDB_Test.bin'
  ```

  - `train_bin` and `test_bin` should be qual to `--dest` parameters in the previous section.
  - `validRatio` indicates what portion of the test dataset should be used for cross-validation.


#### Step3: Train
  - run `th cnn.v2.lua --progress`. See the source file for more commands and options.

> Always use the `--id` parameter. This name will be used to store the model and logs.
