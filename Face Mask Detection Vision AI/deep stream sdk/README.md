# Deep Stream SDK

## Prerequisite
* In order to launch/deploy the model into deep stream SDK, we must have both the `.onnx` and `.engine` file models.

## Overview
* `config_infer_primary_peoplenet.txt` is the configuration for peoplenet, which detects whether the object is a person or not.
* `config_mask_model.txt` is the configuration for face mask detection, which uses the `.onnx` and `.engine` file models. 
* `deepstream_app_source1_peoplenet.txt` is the configuration in order to deploy to deep stream SDK so that we can detect whether the person is wearing a mask or not in the video (live camera/pre-record).
* `here_configs.zip` 
* `labels.txt` displays the label name for bounding boxes depending on whether the person wears a mask or not.

## Instructions
In the command prompt/terminal type:
1. deepstream-app -c deepstream_app_source1_peoplenet.txt
