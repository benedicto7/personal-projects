# Mask Classifier

## Instructions

In order to create the mask classifier which is the model used in deep stream sdk, open command prompt/terminal and type:
To use a built and trained model from masker_model_comparison.ipynb (creates .onnx file), must convert the saved model to a .engine file. In command prompt/terminal:

1. pip install tf2onnx
2. pip install pip==22.2.2
3. pip install onnxruntime
4.python3 -m tf2onnx.convert --saved-model ../me_not_me_detector/models/face_classifier --output face_classifier.onnx --inputs-as-nchw input_1
5.#trtexec -h
6.trtexec --onnx=face_classifier.onnx --saveEngine=face_classifier_onnx.engine
