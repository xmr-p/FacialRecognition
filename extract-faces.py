import cv2
import os

videosFolder = "videos"
facesFolder = "faces"

def separateVideoFrames(videoPath, framesFolder):
	print(f"Separating frames from {videoPath}")
	videoCapture = cv2.VideoCapture(videoPath)
	os.makedirs(framesFolder, exist_ok=True)
	frameCount = 0
	while True:
		ret, frame = videoCapture.read()
		if not ret:
			break
		framePath = os.path.join(framesFolder, f'frame_{frameCount}.jpg')
		cv2.imwrite(framePath, frame)
		frameCount += 1
	videoCapture.release()
	print(f"Frames separated and saved to {framesFolder}")

def convertFramesToGrayscale(framesFolder, grayscaleFolder):
	print(f"Converting frames in {framesFolder} to grayscale")
	os.makedirs(grayscaleFolder, exist_ok=True)
	for frameFile in os.listdir(framesFolder):
		framePath = os.path.join(framesFolder, frameFile)
		frame = cv2.imread(framePath)
		grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayscalePath = os.path.join(grayscaleFolder, frameFile)
		cv2.imwrite(grayscalePath, grayFrame)
	print(f"Frames converted to grayscale and saved to {grayscaleFolder}")

def extractFacesFromGrayscale(grayscaleFolder, facesFolder):
	print(f"Extracting faces from grayscale images in {grayscaleFolder}")
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	os.makedirs(facesFolder, exist_ok=True)
	for grayscaleFile in os.listdir(grayscaleFolder):
		grayscalePath = os.path.join(grayscaleFolder, grayscaleFile)
		grayFrame = cv2.imread(grayscalePath)
		faces = faceCascade.detectMultiScale(grayFrame, scaleFactor=1.3, minNeighbors=5)
		for i, (x, y, w, h) in enumerate(faces):
			face = grayFrame[y:y + h, x:x + w]
			facePath = os.path.join(facesFolder, f'face_{i}_{grayscaleFile}')
			cv2.imwrite(facePath, face)
	print(f"Faces extracted and saved to {facesFolder}")

os.makedirs(facesFolder, exist_ok=True)

for personFolder in os.listdir(videosFolder):
	personPath = os.path.join(videosFolder, personFolder)
	if os.path.isdir(personPath):
		print(f"\nProcessing videos for {personFolder}:\n")
		framesFolder = os.path.join(personPath, 'frames')
		grayscaleFolder = os.path.join(personPath, 'grayscale')
		personFacesFolder = os.path.join(facesFolder, personFolder)
		for videoFile in os.listdir(personPath):
			if videoFile.endswith('.mp4'):
				videoPath = os.path.join(personPath, videoFile)
				separateVideoFrames(videoPath, framesFolder)
				convertFramesToGrayscale(framesFolder, grayscaleFolder)
				extractFacesFromGrayscale(grayscaleFolder, personFacesFolder)

