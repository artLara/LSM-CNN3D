import cv2
import pandas as pd
persona = 4
dire = 'D:\\CIC\\LSM\\CNN_3D\\\LSM-CNN3D\\persona'
videoNames = ['avisame', 'bien', 'buenosDias', 'comoEstas', 'duda', 'examen', 'hola', 'mal', 'mandar', 'whatsapp']
maxFrames = 0
maxPersona = 0
maxSign = ''
df = pd.DataFrame()
names = []
classes = []

namesTrain = []
classesTrain = []

namesTest = []
classesTest = []

for p in range(persona):
	# print('---Persona', p+1)
	for video in videoNames:
		frames = []
		vidcap = cv2.VideoCapture(dire + str(p+1) + '\\' + video + ".mp4")
		success,image = vidcap.read()
		while success:
	        # plt.imshow(image)
			image = cv2.flip(image, 1)
			# image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
			# image = image.astype('float32') / 255.0
			frames.append(image)
			success,image = vidcap.read()

		out = cv2.VideoWriter('persona' + str(p+5) + '\\' +video + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (640, 480))
		for frame in frames:
		    out.write(frame) # frame is a numpy.ndarray with shape (1280, 720, 3)
		out.release()
		# break
	# break