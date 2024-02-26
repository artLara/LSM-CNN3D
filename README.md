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
The idea 
