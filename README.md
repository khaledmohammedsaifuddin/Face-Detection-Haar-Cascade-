# Face-Detection-Haar-Cascade-
Face Detection Technique using Raspberry Pi with Pi camera. 
# Goals
-To introduce with OpenCv </br>
-Interface Pi camera with Raspberry Pi and test the camera</br>
-Detect human face using Haar Cascade classifier
# Description 
Here, this project is done using OpenCv with python, Raspberry Pi and Pi camera. I used Haar features based cascade classifier where a cascade function is trained from a lot of positive and negative images. 
### Negative Images: 
Actually, negative images/background samples/background images are the image that don't contain the 'desired object'. And these samples will be used to train the machine, what not to look for, when searching for desired object.
### Positive images: 
Actually, these are images we are looking for. 
# Creating own classifier
As, we know Opencv can be used as a trainer as well as a detector. So, we can train our own classifier for any object using Opencv by following the steps form here: [Cascade Classifier Training](https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html). 
#### OR
By following these steps from here: [Creating a Cascade of Haar-Like Classifier: Step by Step](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf)

But as OpenCv conatains many pre-trained classifier, I have used form those pre-trained. 


