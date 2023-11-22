import cv2

vPath = "videos/"
fPath = "frames/"
gPath = "grayscale/"
extension = ".mp4"
nVids = 3
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
	

def main():
	print("[1]- SPLITTING: STARTING...")
	nFrames = splitToFrames(vPath, fPath, 0, extension, nVids)
	print("[2]- GRAYSCALING: STARTING...")
	for i in range(nFrames):
		imgToGrayscale((fPath + str(i) + ".jpg"), gPath, i)
	print("[2]- GRAYSCALING: DONE")  
		
main()
