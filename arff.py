import cv2
import os

imagesFolderPath = "faces"
outputArffPath = "arff-files/faces.arff"

def resizeImage(image, size=(50, 50)):
	return cv2.resize(image, size)

def createArff(imagesFolder, outputArff, relationName='faces', attributeClass='class'):
	with open(outputArff, 'w') as arffFile:
		arffFile.write(f'@relation {relationName}\n\n')
		persons = [person for person in os.listdir(imagesFolder) if os.path.isdir(os.path.join(imagesFolder, person))]
		numPixels = 50 * 50
		pixelAttributes = [f'@attribute pixel{i} numeric' for i in range(1, numPixels + 1)]
		arffFile.write('\n'.join(pixelAttributes))
		arffFile.write(f'\n@attribute {attributeClass} {{{", ".join(persons)}}}\n\n@data\n')
		for person in persons:
			personFolder = os.path.join(imagesFolder, person)
			for filename in os.listdir(personFolder):
				if filename.endswith('.jpg') or filename.endswith('.png'):
					imagePath = os.path.join(personFolder, filename)
					img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
					resizedImg = resizeImage(img)
					pixelValues = resizedImg.flatten()
					arffFile.write(f"{', '.join(map(str, pixelValues))}, {person}\n")

createArff(imagesFolderPath, outputArffPath)
