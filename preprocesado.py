import cv2

persona = 4
dire = 'D:\\CIC\\LSM\\CNN_3D\\videos\\persona'
videoNames = ['avisame', 'bien', 'buenosDias', 'comoEstas', 'duda', 'examen', 'hola', 'mal', 'mandar', 'whatsapp']
maxFrames = 0
maxPersona = 0
maxSign = ''
for p in range(persona):
	print('---Persona', p+1)
	for video in videoNames:
		cap = cv2.VideoCapture(dire + str(p+1) + '\\' + video + ".mp4")
		length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		print(video, 'contiene ', length, 'frames')
		if length > maxFrames:
			maxFrames = length
			maxPersona = p+1
			maxSign = video


print('\n>>>Max frames=',maxFrames)
print('>>>Persona=',maxPersona)
print('>>>Sign=',maxSign)
