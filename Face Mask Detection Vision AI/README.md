# Mask Detection Vision AI 

Description: 

Used pre-model created by Agung (me/not_me)... 

Requirement: 
-docker, deepstream sdk, tao, jupyterlab

Instruction: 



To use a built and trained model from masker_model_comparison.ipynb, must convert the saved model to a .engine file. In command prompt/terminal:
pip install tf2onnx
pip install pip==22.2.2
pip install onnxruntime

python3 -m tf2onnx.convert --saved-model ../me_not_me_detector/models/face_classifier --output face_classifier.onnx --inputs-as-nchw input_1
#trtexec -h
trtexec --onnx=face_classifier.onnx --saveEngine=face_classifier_onnx.engine


