# Import Libraries
import tensorflow as tf
from tensorflow import keras
from sys import argv
import os


def Train(params):
    # Manage input arguments 
    if '--train_directory' in params:
        train_directory = params[params.index('--train_directory')+1]
    else:
        train_directory = 'Train-Data/'
    if '--epochs' in params:
        epochs = int(params[params.index('--epochs')+1])
    else:
        epochs = 20
    if '--model_storage_dir' in params:
        model_storage_dir = params[params.index('--model_storage_dir')+1]
    else:
        model_storage_dir = 'models'
        
    # Some constant parameters
    IMG_WIDTH = 30
    IMG_HEIGHT = 30

    # Set random seed
    tf.random.set_seed(1)

    # Create an Image Generator
    img_gen = keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2)
    train_data_dir = os.path.dirname(train_directory)

    # Create train dataset with ImageGenerator from local directory
    train_ds = img_gen.flow_from_directory(
        directory=train_data_dir,
        subset='training',
        shuffle=True,
        color_mode='grayscale',
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        interpolation='bilinear',
        batch_size=48)

    print(train_ds.class_indices)
    # Create validation dataset with ImageGenerator from local directory
    val_ds = img_gen.flow_from_directory(
        directory=train_data_dir,
        subset='validation',
        shuffle=True,
        color_mode='grayscale',
        target_size=(IMG_WIDTH, IMG_HEIGHT),
        interpolation='bilinear',
        batch_size=16)
    print(val_ds.class_indices)

    # Define CNN + FullyConnectedNetwork Model without BN and Dropout
    ocr_model_v1 = keras.models.Sequential([
    keras.layers.Conv2D(64, 5, input_shape=(IMG_WIDTH, IMG_HEIGHT, 1)),
    keras.layers.MaxPool2D(),
    keras.layers.ReLU(),
    keras.layers.Conv2D(128, 5),
    keras.layers.MaxPool2D(),
    keras.layers.ReLU(),
    keras.layers.Flatten(data_format='channels_last'),
    keras.layers.Dense(1024),
    keras.layers.ReLU(),
    keras.layers.Dense(36),
    keras.layers.Softmax()])

    # Compile Model
    ocr_model_v1.compile(optimizer='adam',
                    loss='categorical_crossentropy',
                    metrics='accuracy')

    # Define path to save checkpionts
    checkpoint_path = os.path.join('logs', 'Plain_model')
    # Define callbacks
    # Early Stopping prevents from overfitting
    earlystopping_cb = keras.callbacks.EarlyStopping(patience=3)
    # Save weights of model while training
    checkpoint_cb = keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                save_best_only=True,
                                                save_weights_only=True)
    # Fit model to train data
    model_history = ocr_model_v1.fit(train_ds,
        epochs=epochs,
        validation_data=val_ds,
        callbacks=[earlystopping_cb, checkpoint_cb])

    # Create directory if it doesn't exist
    if not os.path.exists(model_storage_dir):
        os.mkdir(model_storage_dir)
    # Save model
    ocr_model_v1.save(os.path.join(model_storage_dir, 'ocr_model_v1.h5'))

    print(f"Last accuracy on validation dataset is:{model_history.history['val_accuracy'][-1] * 100:5.2f}")
    return True


if __name__=="__main__":
    Train(argv[1:])
