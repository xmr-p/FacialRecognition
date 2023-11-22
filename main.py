import cv2

vPath = "videos/"
fPath = "frames/"
extension = ".mp4"
nVids = 17

def splitToFrames(videosPath, framesPath, frameNum, videosExt, numVids):
	for i in range(numVids):
		frameNum = 0
		capture = cv2.VideoCapture(videosPath + str(i) + videosExt)
		while True:
			success, frame = capture.read()
			if success:
				cv2.imwrite(f"{framesPath}vid-{i}-frame-{frameNum}.jpg", frame)
			else:
				break
			frameNum += 1
		print(f"[1]- Video {i}: DONE")
		capture.release()
	print("[1]- Splitting: DONE")

def main():
	splitToFrames(vPath, fPath, 0, extension, nVids)
main()
