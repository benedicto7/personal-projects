# Face Mask Detection Vision AI 

## Description
Face Mask Detection is a vision AI application that detects whether the person is wearing a mask or not. It detects and displays bounding boxes and labels that indicates whether the person is wearing a mask or not depending on the state of the person (mask/no_mask). In this project, I was personally mentored and helped by Mr. Agung Fazrulhaq (agung.fazrulhaq@epsindo.co.id) to create this face mask detection. This project used a pre-model created by Mr. Agung (me/not_me) which detects if the person is him or another person. Additionally, this project used peoplenet, in the Deep Stream SDK, which detects if the object detect is a person or not.


## Overview
* `Augmentation` augments my initial data to add variety and amount to my data set. 
* `Datasets` are the datasets that will be used to train and test my model. It is separated into three categories: augmentation (all my data), training (initial data), testing (data to be tested).
* `Deep stream SDK` is where the face mask detection model is deployed. This means that the model is able to test videos (live camera/pre-record), unlike `Model` where the model tests static images.
* `Model` is where the face mask detection model is built and trained. 

## Requirements
* TAO Toolkit
* TensorRT
* Deep stream SDK
* JupyterLab
* Docker

## Instructions
1. Download and run all files on JupyterLab

## Final Result of Project
https://user-images.githubusercontent.com/90052277/185654356-efaab18d-d309-4bf2-8f8d-493c67240676.mp4

https://user-images.githubusercontent.com/90052277/185654428-9a0d090d-9308-4489-8d30-59b318f3bddf.mp4

https://user-images.githubusercontent.com/90052277/185654451-026e60ec-dfa2-41db-b9c3-a08f50df2500.mp4

## Local Host to JupyterLab
Data Augmentation, Build Model, and Training <br/>
http://192.168.1.10:38889/lab
<br/>

Deep Stream SDK (Test with video/camera) <br/>
http://192.168.1.10:8688/lab 
<br/>
