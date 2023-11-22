import cv2

def splitToFrames(videosPath, frameNum):
	for i in range(17):
		capture = cv2.VideoCapture(videosPath + str(i))
		while True:
			success, frame = capture.read()
			if success:
				cv2.imwrite(f"frames/vid-{i}frame-{frameNum}.jpg", frame)
			else:
				break
			frameNr += 1
		capture.release()

def main():
	splitToFrames("videos/", 0)
main()
