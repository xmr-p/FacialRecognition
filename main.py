import cv2

vPath = "videos/"
fPath = "frames/"
gPath = "grayscale/"
facesP = "faces/"
extension = ".mp4"
nVids = 17
nFrames = 0

def splitToFrames(videosPath, framesPath, frameNum, videosExt, numVids):
	for i in range(numVids):
		capture = cv2.VideoCapture(videosPath + str(i) + videosExt)
		while True:
			success, frame = capture.read()
			if success:
				cv2.imwrite(f"{framesPath}{frameNum}.jpg", frame)
			else:
				break
			frameNum += 1
		print(f"   - Video {i}: DONE")
		capture.release()
	print("[1]- SPLITTING: DONE")
	return frameNum

def imgToGrayscale(frame, grayscalePath, indx):
	img = cv2.imread(frame)
	grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(f"{grayscalePath}{indx}.jpg", grayImg)
	print(f"   - Frame {indx} grayscale: DONE")

def detectFaces(n):
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	for i in range(n):
		gray = cv2.imread(gPath + str(i) + ".jpg")
		faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30)) 
		for (x, y, w, h) in faces:
			cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
			roiColor = gray[y:y + h, x:x + w]
		status = cv2.imwrite(f"{facesP}{i}.jpg", roiColor)
		print(f"   - Image {i}.jpg written: ", status)
	
def main():
	print("[1]- SPLITTING: STARTING...")
	nFrames = splitToFrames(vPath, fPath, 0, extension, nVids)
	print("[2]- GRAYSCALING: STARTING...")
	nf = nFrames
	for i in range(nf):
		imgToGrayscale((fPath + str(i) + ".jpg"), gPath, i)
	print("[2]- GRAYSCALING: DONE")  
	print("[3]- FACE DETECTION: STARTING...")
	detectFaces(nf)
	print("[3]- FACE DETECTION: DONE")
		
main()
