import cv2
import os

facesFolder = "faces"
resizedFacesFolder = "resized-faces"
arffFolder = "arff-files"
dimensions100x100 = (100, 100)
dimensions500x500 = (500, 500)

def resizeAndSaveFaces(inputFolder, outputFolder, dimensions):
	os.makedirs(outputFolder, exist_ok=True)
	for faceFile in os.listdir(inputFolder):
		if faceFile.endswith('.jpg'):
			facePath = os.path.join(inputFolder, faceFile)
			face = cv2.imread(facePath)
			resizedFace = cv2.resize(face, dimensions, interpolation=cv2.INTER_LINEAR)
			outputFacePath = os.path.join(outputFolder, f'{faceFile[:-4]}_{dimensions[0]}x{dimensions[1]}.jpg')
			cv2.imwrite(outputFacePath, resizedFace)

def createArffFile(outputFolder, arffFilePath, dimensions):
	grayscaleValues = []
	for faceFile in os.listdir(outputFolder):
		if faceFile.endswith('.jpg'):
			facePath = os.path.join(outputFolder, faceFile)
			face = cv2.imread(facePath, cv2.IMREAD_GRAYSCALE)
			flattenedFace = face.flatten()
			grayscaleValues.append(flattenedFace.tolist())
	with open(arffFilePath, 'w') as arffFile:
		arffFile.write('@relation faces\n\n')
		for i in range(dimensions[0] * dimensions[1]):
			arffFile.write(f'@attribute pixel_{i} numeric\n')
		arffFile.write('@data\n')
		for values in grayscaleValues:
			arffFile.write(','.join(map(str, values)) + '\n')

os.makedirs(arffFolder, exist_ok=True)

for personFolder in os.listdir(facesFolder):
	personFacesPath = os.path.join(facesFolder, personFolder)
	if os.path.isdir(personFacesPath):
		print(f"\nProcessing for {personFolder}:\n")
		resized100x100Folder = os.path.join(resizedFacesFolder, f'{personFolder}_100x100')
		resized500x500Folder = os.path.join(resizedFacesFolder, f'{personFolder}_500x500')
		resizeAndSaveFaces(personFacesPath, resized100x100Folder, dimensions100x100)
		resizeAndSaveFaces(personFacesPath, resized500x500Folder, dimensions500x500)
		arffFilePath100x100 = os.path.join(arffFolder, f'{personFolder}_100x100.arff')
		arffFilePath500x500 = os.path.join(arffFolder, f'{personFolder}_500x500.arff')
		createArffFile(resized100x100Folder, arffFilePath100x100, dimensions100x100)
		createArffFile(resized500x500Folder, arffFilePath500x500, dimensions500x500)
