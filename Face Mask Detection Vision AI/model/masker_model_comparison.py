# Date: August 19, 2022
# Author: Agung Fazrulhaq (agung.fazrulhaq@epsindo.co.id)
# Edited: Benedicto Elpidius


#!/usr/bin/env python
# coding: utf-8


# In[1]: Import Libraries

# Common imports
import os
import numpy as np

# Visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

# TensorFlow imports may differs from version to versions
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping

# In[2]: Set Some Parameters

# Dataset information: Test dataset is set explicitly, because the amount of data is very small
train_aug_image_folder = os.path.join('datasets', 'augmentation')
train_image_folder = os.path.join('datasets', 'training')
test_image_folder = os.path.join('datasets', 'testing')

# Size of all images are turned the same because original images have different sizes
img_height, img_width = 250, 250 
num_classes = 2  # mask - no_mask

# Training settings
validation_ratio = 0.2  # 20% of the images are used for validation - 80% of the images are used for training
batch_size = 16

AUTOTUNE = tf.data.AUTOTUNE


# In[3]: Create Dataset; Read datasets from folders

# Train and validation sets of initial dataset
train_ds = keras.preprocessing.image_dataset_from_directory(
    train_image_folder,
    validation_split=validation_ratio,
    subset="training",
    seed=42,
    image_size=(img_height, img_width),
    label_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

val_ds = keras.preprocessing.image_dataset_from_directory(
    train_image_folder,
    validation_split=validation_ratio,
    subset="validation",
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode='categorical',
    shuffle=True)

# Train and validation sets of augmented dataset
train_aug_ds = keras.preprocessing.image_dataset_from_directory(
    train_aug_image_folder,
    validation_split=validation_ratio,
    subset="training",
    seed=42,
    image_size=(img_height, img_width),
    label_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

val_aug_ds = keras.preprocessing.image_dataset_from_directory(
    train_aug_image_folder,
    validation_split=validation_ratio,
    subset="validation",
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode='categorical',
    shuffle=True)

# Test model later on using testing dataset 
test_ds = keras.preprocessing.image_dataset_from_directory(
    test_image_folder,
    image_size=(img_height, img_width),
    label_mode='categorical',
    shuffle=False)

# Print the total number of images/files in testing directory of mask and no mask
count1 = os.listdir("/workspace/masker_detection/datasets/testing/mask")
print(len(count1))

count2 = os.listdir("/workspace/masker_detection/datasets/testing/no_mask")
print(len(count2))

count3 = os.listdir("/workspace/masker_detection/datasets/testing")
print(len(count3))

class_names = test_ds.class_names
class_names

# In[4]: Build The Model 

# Here I experimented with different models
# Each model is represented in it own cells

# In[5]: VGG16 Model

base_model = keras.applications.vgg16.VGG16(weights='imagenet',
                                            include_top=False,  # without dense part of the network
                                            input_shape=(img_height, img_width, 3))

# Set layers to non-trainable
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers on top of the convolutional layers of VGG16
flatten = keras.layers.Flatten()(base_model.output)
dense_4096_1 = keras.layers.Dense(4096, activation='relu')(flatten)
dense_4096_2 = keras.layers.Dense(4096, activation='relu')(dense_4096_1)
output = keras.layers.Dense(num_classes, activation='sigmoid')(dense_4096_2)

VGG16 = keras.models.Model(inputs=base_model.input, outputs=output, name='VGG16')

VGG16.summary()

# In[6]: ResNet50 Model

base_model = keras.applications.ResNet50(weights='imagenet',
                                         include_top=False,  # without dense part of the network
                                         input_shape=(img_height, img_width, 3))

# Set layers to non-trainable
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers on top of ResNet
global_avg_pooling = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(num_classes, activation='sigmoid')(global_avg_pooling)

ResNet50 = keras.models.Model(inputs=base_model.input, outputs=output, name='ResNet50')

ResNet50.summary()

# In[7]: ResNet152 Model

base_model = keras.applications.ResNet152(weights='imagenet',
                                          include_top=False,  # without dense part of the network
                                          input_shape=(img_height, img_width, 3))

# Set layers to non-trainable
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers on top of ResNet
global_avg_pooling = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(num_classes, activation='sigmoid')(global_avg_pooling)

ResNet152 = keras.models.Model(inputs=base_model.input, outputs=output, name='ResNet152')

ResNet152.summary()

# In[8]: Xception Model

base_model = keras.applications.Xception(weights='imagenet',
                                         include_top=False,  # without dense part of the network
                                         input_shape=(img_height, img_width, 3))

# Set layers to non-trainable
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers on top of Xception
global_avg_pooling = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(num_classes, activation='sigmoid')(global_avg_pooling)

Xception = keras.models.Model(inputs=base_model.input, outputs=output, name='Xception')

Xception.summary()

# In[9]: MobileNet Model

base_model = keras.applications.MobileNet(weights='imagenet',
                                          include_top=False,  # without dense part of the network
                                          input_shape=(img_height, img_width, 3))

# Set layers to non-trainable
for layer in base_model.layers:
    layer.trainable = False

# Add custom layers on top of MobileNet
global_avg_pooling = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(num_classes, activation='sigmoid')(global_avg_pooling)

MobileNet = keras.models.Model(inputs=base_model.input, outputs=output, name='MobileNet')

MobileNet.summary()

# In[10]: Training

# Choose one of the models in next cell. Possible options:
# - VGG16
# - ResNet50
# - ResNet152
# - Xception
# - MobileNet

# In[11]: Choosing Model to train

# Train model ResNet50
mask_classifier = ResNet50
mask_classifier.summary()  # to check that model is choosen correctly

# Train model on augmented dataset
train_on_aug = True 

if train_on_aug:
    train_ds = train_aug_ds
    val_ds = val_aug_ds

if train_on_aug:
    name_to_save = f"models/mask_classifier_{mask_classifier.name}_aug.h5"
else:
    name_to_save = f"models/mask_classifier_{mask_classifier.name}.h5"

# In[12]: All models trains in one context, so this part of the code is the same

# ModelCheckpoint to save model in case of interrupting the learning process
checkpoint = ModelCheckpoint(name_to_save, monitor="val_loss", mode="min", save_best_only=True, verbose=1)

# EarlyStopping to find best model with a large number of epochs
# Stops the training when the model has stopped improving
earlystop = EarlyStopping(monitor='val_loss',
                          restore_best_weights=True,
                          patience=5,  # number of epochs with no improvement after which training will be stopped
                          verbose=1)

callbacks = [earlystop, checkpoint]

mask_classifier.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.Adam(learning_rate=0.01), metrics=['accuracy'])

epochs = 50

history = mask_classifier.fit(train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds)

mask_classifier.save(name_to_save)

# Creates a directory containing the built and trained model
mask_classifier.save("models/mask_classifier")

# In[13]: Choosing Model to test

# Test model ResNet50
model_name = 'mask_classifier_ResNet50_aug.h5'
mask_classifier = keras.models.load_model(f'models/{model_name}')

def test_image_classifier_with_folder(model, path, y_true, img_height=250, img_width=250, class_names=['mask', 'no_mask']):
    '''
    Read all images from 'path' using tensorflow.keras.preprocessing.image module, 
    than classifies them using 'model' and compare result with 'y_true'.
    Calculate total accuracy based on 'path' test set.

    Parameters:
        model : Image classifier
        path (str): Path to the folder with images you want to test classifier on 
        y_true : True label of the images in the folder. Must be in 'class_names' list
        img_height (int): The height of the image that the classifier can process 
        img_width (int): The width of the image that the classifier can process
        class_names (array-like): List of class names 

    Returns:
        None
    '''
    
    num_classes = len(class_names)  # Number of classes
    total = 0  # number of images total
    correct = 0  # number of images classified correctly

    for filename in os.listdir(path):
        # read each image in the folder and classifies it
        test_path = os.path.join(path, filename)
        test_image = keras.preprocessing.image.load_img(
            test_path, target_size=(img_height, img_width, 3))
       
        # from image to array, can try type(test_image)
        test_image = keras.preprocessing.image.img_to_array(test_image)
        
        # shape from (250, 250, 3) to (1, 250, 250, 3)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)

        y_pred = class_names[np.array(result[0]).argmax(axis=0)]  # predicted class
        iscorrect = 'correct' if y_pred == y_true else 'incorrect' # mask_on mask_off
        
        print('{} - {}'.format(iscorrect, filename))
        
        for index in range(num_classes):
            print("\t{:6} with probabily of {:.2f}%".format(
                class_names[index], result[0][index] * 100))

        total += 1
        if y_pred == y_true:
            correct += 1

    print("\nTotal accuracy is {:.2f}% = {}/{} samples classified correctly".format(
        correct/total*100, correct, total))

# Test mask images
test_image_classifier_with_folder(mask_classifier, 'datasets/testing/mask', y_true='mask')

# Test no_mask images
test_image_classifier_with_folder(mask_classifier,
                                  'datasets/testing/no_mask',
                                  y_true='no_mask')

# In[14]: Test a particular Mask Image

# Choose one image to test
test_path = 'datasets/testing/mask/test_image.jpeg'
test_image = keras.preprocessing.image.load_img(test_path, target_size=(img_height, img_width, 3))

# Outputs the chosen image
test_image

# Detect whether the image is using a mask or not
test_image = keras.preprocessing.image.img_to_array(test_image)  # from image to array
# shape from (250, 250, 3) to (1, 250, 250, 3)
test_image = np.expand_dims(test_image, axis=0)
result = mask_classifier.predict(test_image)

for index in range(num_classes):
    print("{:6} with probabily of {:.2f}%".format(
        class_names[index], result[0][index] * 100))

# In[15]: Test a particular No Mask Image

# Choose one image to test
test_path = 'datasets/testing/no_mask/test_image.jpg'
test_image = keras.preprocessing.image.load_img(test_path, target_size=(img_height, img_width, 3))

# Outputs the chosen image
test_image

# Detect whether the image is using a mask or not
test_image = keras.preprocessing.image.img_to_array(test_image)  # from image to array

# shape from (250, 250, 3) to (1, 250, 250, 3)
test_image = np.expand_dims(test_image, axis=0)
result = mask_classifier.predict(test_image)

for index in range(num_classes):
    print("{:6} with probabily of {:.2f}%".format(
        class_names[index], result[0][index] * 100))

# In[16]: Plotting

dataset_size = [1, 2, 3, 4, 5, 10, 15, 20, 25]
training_time_per_epoch = [2, 4, 6, 8, 9, 19, 30, 35, 46]

fig = plt.figure(figsize=(8, 4))
plt.plot(dataset_size, training_time_per_epoch, marker='o', label="Training Time")

plt.title("The Dependence of the Training Time on the Dataset Size", fontsize='16')
plt.xlabel("The coefficient of the dataset increasing", fontsize='14')
plt.ylabel("Training Time for Epoch, s", fontsize='14')
plt.legend(loc='best')
plt.savefig('article/img/dataset_size_to_learning_time.jpg')
plt.show()

# The dependence of the training time (per epoch) on the dataset size is linear

dataset_size = [1, 2, 3, 4, 5, 10, 15, 20, 25]
val_loss = [0.8011, 0.2802, 0.2479, 0.2653, 0.191, 0.2191, 0.09886, 0.10429, 0.1322]
val_accuracy = [0.8276, 0.9138, 0.908, 0.8718, 0.911, 0.911, 0.9589, 0.9497, 0.9479]

fig = plt.figure(figsize=(8, 4))
plt.plot(dataset_size, val_loss, c="red", linewidth=2, marker='o', label="Validation Loss")
plt.plot(dataset_size, val_accuracy, c="green", linewidth=2, marker='o', label="Validation Accuracy")

plt.title("The Dependence of the Model Quality on the Dataset Size", fontsize='16')
plt.xlabel("The coefficient of the dataset increasing", fontsize='14')
plt.ylabel("Model Quality", fontsize='14')
plt.legend(loc='best')
plt.savefig('article/img/dataset_size_to_model_quality.jpg')
plt.show()