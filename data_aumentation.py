import cv2
persona = 4
path = 'D:\\CIC\\LSM\\CNN_3D\\\LSM-CNN3D\\persona'
videoNames = ['avisame', 'bien', 'buenosDias', 'comoEstas', 'duda', 'examen', 'hola', 'mal', 'mandar', 'whatsapp']

for p in range(persona):
	for video in videoNames:
		frames = []
		vidcap = cv2.VideoCapture(path + str(p+1) + '\\' + video + ".mp4")
		success,image = vidcap.read()
		out = cv2.VideoWriter('persona' + str(p+5) + '\\' +video + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 24, (640, 480))
		while success:
			image = cv2.flip(image, 1)
			out.write(image) # frame is a numpy.ndarray with shape (1280, 720, 3)
			success,image = vidcap.read()
		out.release()
		# break
	# break