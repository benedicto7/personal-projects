# Mask Classifier

## Instructions
Running masker_model_comparison.ipynb creates an `.onnx` file model as well as additional `mask classifier` file models, which will be used for deep stream SDK. However, an `.engine` file model is also required to run deep stream SDK. Therefore, to create the `.engine` file model, we must convert the saved `.onnx` file model into an `.engine` file model. In the command prompt/terminal:
1. pip install tf2onnx
2. pip install pip==22.2.2
3. pip install onnxruntime
4.python3 -m tf2onnx.convert --saved-model ../me_not_me_detector/models/face_classifier --output face_classifier.onnx --inputs-as-nchw input_1
5.#trtexec -h
6.trtexec --onnx=face_classifier.onnx --saveEngine=face_classifier_onnx.engine
