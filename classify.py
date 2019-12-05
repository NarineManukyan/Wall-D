#REQUIES BOTH KERAS AND IMAGEAI imports
#https://medium.com/@guymodscientist/image-prediction-with-10-lines-of-code-3266f4039c7a
from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(execution_path + "\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()

if __name__=="__main__":
    predictions, percentage_probabilities = prediction.predictImage("PASS JPEG?PNG INTO MODEL HERE",
                                                                    result_count=5)
    for index in range(len(predictions)):
        print(predictions[index], " : ", percentage_probabilities[index])