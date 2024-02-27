# LSM-CNN3D: 10 dynamic signs classification

The main pourpose of this project is classify 10 signs from Mexican Sign Lenaguage (MSL), so it is divided in 4 parts: dataset, pre-processing, classification and evaluation.

## Dataset
The dataset is building with 4 signers (just 1 professional) doing 10 differents signs, that's why is a balanced dataset. These signs are enumerate following:

1. Avísame (warn)
2. Bien (good)
3. Buenos días (good morning)
4. ¿Cómo estas? (how are you?)
5. Duda (doubt)
6. Examen (exam)
7. Hola (hello)
8. Mal (bad)
9. Mandar (send)
10. WhatsApp

I propose apply data augmentation, so all videos are flipping. Therefore 70 videos are using for training and 10 videos (of differents signers) are using fot testing.

## Pre-processing
Pre-processing is necessary for specify the input shape of CNN-3D. The next image discribe preprocessing. You can check the pre-processing code in the notebook file.
![preprocessing](https://github.com/artLara/LSM-CNN3D/assets/63621038/bfc4c286-593b-4d07-b055-b06899f0e3f5)

## Classification
CNN-3D is a specific neural network for extract information of data in sequence of images, so it is perfect to process dynamic signs in videos. The architecture used is displayed in the next image and you can check the code in the notebook.
![architecture](https://github.com/artLara/LSM-CNN3D/assets/63621038/002224f5-d92b-4b8d-9ea0-702c599c3d09)

## Evaluation
The evaluation is based in accuracy metric because this dataset is balanced. After 200 epochs, the accuracy is 70% using test data.

![image](https://github.com/artLara/LSM-CNN3D/assets/63621038/6ceab686-4563-4dc3-8beb-bd4ea32c12b2)


[Link of notebook in Google Colab](https://drive.google.com/file/d/1SM0t5vaGmEZNNs4SI2_sMQaEvlOg37ca/view?usp=sharing)
