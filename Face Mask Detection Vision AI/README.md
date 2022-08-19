# Mask Detection Vision AI 

## Description

## Requirements
* TAO Toolkit
* TensorRT
* Deep stream SDK
* Docker

## Instructions
1. 

## Final Result of Project
https://user-images.githubusercontent.com/90052277/185654258-7655f5cd-9dea-44ca-a430-bd952c68cbe0.mp4
https://user-images.githubusercontent.com/90052277/185654268-d26c4716-ed97-4d63-afff-23b219d22135.mp4
https://user-images.githubusercontent.com/90052277/185654275-0bccd13a-bcbc-4faa-a12c-24a20b0f51d0.mp4

Data Augmentation, Build Model, and Training <br/>
http://192.168.1.10:38889/lab
<br/>

Deep Stream SDK (Test with video/camera) <br/>
http://192.168.1.10:8688/lab 
<br/>

deepstream-app -c deepstream_app_source1_peoplenet.txt

Description: 

Used pre-model created by Agung (me/not_me)... 
Agung Fazrulhaq agung.fazrulhaq@epsindo.co.id

To use a built and trained model from masker_model_comparison.ipynb, must convert the saved model to a .engine file. In command prompt/terminal:
pip install tf2onnx
pip install pip==22.2.2
pip install onnxruntime

python3 -m tf2onnx.convert --saved-model ../me_not_me_detector/models/face_classifier --output face_classifier.onnx --inputs-as-nchw input_1
#trtexec -h
trtexec --onnx=face_classifier.onnx --saveEngine=face_classifier_onnx.engine


