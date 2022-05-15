import cv2
import pandas as pd
persona = 4
dire = 'D:\\CIC\\LSM\\CNN_3D\\videos\\persona'
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
		# cap = cv2.VideoCapture(dire + str(p+1) + '\\' + video + ".mp4")
		# length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		# print(video, 'contiene ', length, 'frames')
		# if length > maxFrames:
		# 	maxFrames = length
		# 	maxPersona = p+1
		# 	maxSign = video
		if (p == 0 and video == 'avisame') or (p == 0 and video == 'buenosDias'):
			namesTest.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTest.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'test')

		elif p==0: 
			namesTrain.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTrain.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'train')


		if p == 1 and video == 'bien' or p == 1 and video == 'comoEstas' or p == 1 and video == 'duda':
			namesTest.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTest.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'test')

		elif p==1: 
			namesTrain.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTrain.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'train')


		if p == 2 and video == 'examen' or p == 2 and video == 'hola':
			namesTest.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTest.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'test')

		elif p==2: 
			namesTrain.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTrain.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'train')


		if p == 3 and video == 'mal' or p == 3 and video == 'whatsapp' or p == 3 and video == 'mandar':
			namesTest.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTest.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'test')

		elif p==3: 
			namesTrain.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTrain.append(video)
			print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video, 'train')
			
		# print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video)
		names.append('persona' + str(p+1) + '/' + video + ".mp4")
		classes.append(video)


# print('\n>>>Max frames=',maxFrames)
# print('>>>Persona=',maxPersona)
# print('>>>Sign=',maxSign)
df['Name'] = names
df['Class'] = classes
df.to_csv('D:\\CIC\\LSM\\CNN_3D\\LSM-CNN3D\\all.csv', index=False)

df = pd.DataFrame()
df['Name'] = namesTrain
df['Class'] = classesTrain
df.to_csv('D:\\CIC\\LSM\\CNN_3D\\LSM-CNN3D\\train.csv', index=False)

df = pd.DataFrame()
df['Name'] = namesTest
df['Class'] = classesTest
df.to_csv('D:\\CIC\\LSM\\CNN_3D\\LSM-CNN3D\\test.csv', index=False)