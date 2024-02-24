import pandas as pd
persona = 8
videoNames = ['avisame', 'bien', 'buenosDias', 'comoEstas', 'duda', 'examen', 'hola', 'mal', 'mandar', 'whatsapp']
names = []
classes = []

namesTrain = []
classesTrain = []

namesTest = []
classesTest = []

for p in range(persona):
	for video in videoNames:
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
			
		if p>=4:
			namesTrain.append('persona' + str(p+1) + '/' + video + ".mp4")
			classesTrain.append(video)
		# print('Name: ','persona' + str(p+1) + '\\' + video + ".mp4", 'class: ', video)
		names.append('persona' + str(p+1) + '/' + video + ".mp4")
		classes.append(video)



df = pd.DataFrame()
df['Name'] = names
df['Class'] = classes
df.to_csv('dataset.csv', index=False)

df = pd.DataFrame()
df['Name'] = namesTrain
df['Class'] = classesTrain
df.to_csv('train.csv', index=False)

df = pd.DataFrame()
df['Name'] = namesTest
df['Class'] = classesTest
df.to_csv('test.csv', index=False)