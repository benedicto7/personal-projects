# Date: July 25, 2022 - August 19, 2022
# Author: Agung Fazrulhaq (agung.fazrulhaq@epsindo.co.id)
# Edited: Benedicto Elpidius


#!/usr/bin/env python
# coding: utf-8


# In[1]: Import libraries

# Common imports
import os
import numpy as np

# Visualization
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns # pip install seaborn
get_ipython().run_line_magic('matplotlib', 'inline')

# TensorFlow imports may differs from version to versions
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# In[2]: Setup

# Dataset information
image_folder = os.path.join('datasets', 'training') # access training folder

# Size of all images are turned the same because original images have different sizes
img_height, img_width = 250, 250  
num_classes = 2  # mask - no_mask

# | - training
#     | - mask
#         | - ...
#     | - no_mask
#         | - ...

# In[3]: Look at the data 

# Initial dataset is 50 images: 25 mask and 25 no mask
dataset = keras.preprocessing.image_dataset_from_directory(image_folder, seed=None, image_size=(img_height, img_width), label_mode='categorical', shuffle=True)

# Checks the total number of images of each folder
count1 = os.listdir("/workspace/masker_detection/datasets/training/mask") # mask
print(len(count1))

count2 = os.listdir("/workspace/masker_detection/datasets/training/no_mask") # no_mask
print(len(count2))

# Initialize the two class name of mask and no_mask
class_names = dataset.class_names
print(class_names)

# Helper function to get classname of the image
def get_classname(class_names, mask):
    '''
    Returns an element of the array 'class_names' with the index
    where the maximum value from the 'mask' array is located.
    Used to get classname with categorical labels.

    Parameters:
        class_names (array-like): Target array
        mask (array-like): Mask array, elements must be numbers
    Returns:
        One of the element from 'class_names'

    >>> get_classname(['first', 'second'], [0, 1])
    'second'
    >>> get_classname(['first', 'second', third], [1, 0, 0])
    'first'
    '''
    
    assert len(class_names) == len(mask), "The arrays must be of the same length"

    return class_names[np.array(mask).argmax(axis=0)]

# Form a dataset with maximum count foremost items out of the stated dataset
dataset.take(3)

# The square root of the total number of images shown: images per row / col.
sqrt_img = 2 
plt.figure(figsize=(8, 8))
for images, labels in dataset.take(3):
    for index in range(sqrt_img**2):
        # grid 'sqrt_img' x 'sqrt_img'
        plt.subplot(sqrt_img, sqrt_img, index + 1)
        plt.imshow(images[index] / 255)
        
        class_name = get_classname(class_names, labels[index])
        
        plt.title("Class: {}".format(class_name))
        plt.axis("off")

# In[4]: Data Augmentation

# The number of samples processed before the model is updated
batch_size = 10

# Create data generator based on ImageDataGenerator object
train_datagen = ImageDataGenerator(rotation_range=20,
    width_shift_range=0.4,
    height_shift_range=0.4,
    brightness_range=(0.7, 1),
    shear_range=0.4,
    zoom_range=0.4,
    horizontal_flip=True,
    vertical_flip=False,
    fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
    image_folder,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

# To see an example of an augmented image
image, label = train_generator.next()

plt.figure(figsize=(6, 6))
plt.imshow(image[0] / 255)  # first image from batch
plt.title("Augmented image from ImageDataGenerator")
plt.axis("off")

# Sometimes the image shown is blurred/smudge

# In[5]: Option 1 - Generate n * batch_size random samples; Generate a total of 200 augmentated data: 100 mask and 100 no mask.

n = 20
aug_image_folder = os.path.join('datasets', 'augmentation')

if not os.path.exists(aug_image_folder):
    os.makedirs(aug_image_folder)  # create folder if doesn't exist

# Note that the content of the folder is not deleted and files are added at every step

train_generator.save_to_dir = aug_image_folder
train_generator.save_format = 'jpg'

# If 'save_to_dir' is set, `next()` method
# will generate `batch_size` images each time 
# and save them to 'save_to_dir' folder

for i in range(n):
    print("Step {} of {}".format(i+1, n))
    
    train_generator.next()
    
    print("\tGenerate {} random images".format(train_generator.batch_size))

print("\nTotal number images generated = {}".format(n*train_generator.batch_size))

# One of the problem is to label data again - so you need to create two ImageDataGenerator objects
# This example is good, and this dataset can be successfully used to train CNN, 
# but if you want to get more control, we can set number of images we want to get explicitly

# In[6]: Option 2 - Generate n samples for each image; Generate a total of 125 mask data. This includes 100 augmentated data and the original 25 data.
# Then generate a total of 125 no mask data. This includes 100 augmentated data and the original 25 data.

n = 5
aug_image_folder = os.path.join('datasets', 'augmentation')

if not os.path.exists(aug_image_folder):
    os.makedirs(aug_image_folder)  # create folder if doesn't exist

# Note that the content of the folder is not deleted and files are added at every step

train_datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.4,
    height_shift_range=0.4,
    brightness_range=(0.7, 1),
    shear_range=0.4,
    zoom_range=0.4,
    horizontal_flip=True,
    vertical_flip=False,
    fill_mode='nearest')

# Generate 'mask' folder
image_folder_to_generate = os.path.join(image_folder, 'mask')
image_folder_to_save = os.path.join(aug_image_folder, 'mask')

if not os.path.exists(image_folder_to_save):
    os.makedirs(image_folder_to_save)  # create folder if doesn't exist

i = 0
total = len(os.listdir(image_folder_to_generate))  # number of files in folder
for filename in os.listdir(image_folder_to_generate):
    print("Step {} of {}".format(i+1, total))
    
    # for each image in folder: read it
    image_path = os.path.join(image_folder_to_generate, filename)
    image = keras.preprocessing.image.load_img(image_path, target_size=(img_height, img_width, 3))
    image = keras.preprocessing.image.img_to_array(image)  # from image to array
    
    # shape from (250, 250, 3) to (1, 250, 250, 3)
    image = np.expand_dims(image, axis=0)
    
    # create ImageDataGenerator object for it
    current_image_gen = train_datagen.flow(image, batch_size=1, save_to_dir=image_folder_to_save, save_prefix=filename, save_format="jpg")
    
    # generate n samples
    count = 0
    for image in current_image_gen:  # accessing the object saves the image to disk
        count += 1
        if count == n:  # n images were generated
            break
            
    print('\tGenerate {} samples for file {}'.format(n, filename))
    i += 1

print("\nTotal number images generated = {}".format(n*total))

# Generate 'no_mask' folder
image_folder_to_generate = os.path.join(image_folder, 'no_mask')
image_folder_to_save = os.path.join(aug_image_folder, 'no_mask')

if not os.path.exists(image_folder_to_save):
    os.makedirs(image_folder_to_save)  # create folder if doesn't exist

i = 0
total = len(os.listdir(image_folder_to_generate))  # number of files in folder
for filename in os.listdir(image_folder_to_generate):
    print("Step {} of {}".format(i+1, total))
    
    # for each image in folder: read it
    image_path = os.path.join(image_folder_to_generate, filename)
    image = keras.preprocessing.image.load_img(
        image_path, target_size=(img_height, img_width, 3))
    image = keras.preprocessing.image.img_to_array(
        image)  # from image to array
    
    # shape from (250, 250, 3) to (1, 250, 250, 3)
    image = np.expand_dims(image, axis=0)

    # create ImageDataGenerator object for it
    current_image_gen = train_datagen.flow(image, batch_size=1, save_to_dir=image_folder_to_save, save_prefix=filename, save_format="jpg")

    # generate n samples
    count = 0
    for image in current_image_gen:  # accessing the object saves the image to disk
        count += 1
        if count == n:  # n images were generated
            break
            
    print('\tGenerate {} samples for file {}'.format(n, filename))
    i += 1

print("\nTotal number images generated = {}".format(n*total))