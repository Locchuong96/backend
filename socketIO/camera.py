
import threading
import time 
import cv2

class Camera:
	def __init__(self):
		self.thread = None
		self.current_frame = None
		self.last_access = None
		self.is_running: bool = False
		self.camera = cv2.VideoCapture(0)
		# check your camera is open or not, if not raise error
		if not self.camera.isOpened():
			raise Exception(f"[CAMERA] Could not open video 0 device")
		self.camera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
		self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

	def __del__(self):
		'''
		Release the camera connection at exit
		'''
		self.camera.release()

	def start(self):
		'''
		Create a thread running function _capture
		'''
		if self.thread is None:
			self.thread = threading.Thread(target=self._capture)
			self.thread.start()

	def get_frame(self):
		self.last_access = time.time()
		return self.current_frame

	def stop(self):
		'''
		Stop camera, join thread and set bool is_running = False
		'''
		self.is_running = False
		self.thread.join()
		self.thread = None

	def _capture(self):
		'''
		Get new frame and looping
		'''
		self.is_running = True
		self.last_access = time.time()
		while self.is_running:
			time.sleep(0.1) # sleep 0.1 s before going to new frame
			ret,frame = self.camera.read() # read new frame
			if ret:
				ret,encoded = cv2.imencode('.jpg',frame) # try to decode the image into *.jpg
				if ret:
					self.current_frame = encoded # if decode success then set it to current_frame
				else:
					print("[CAMERA] Failed to encode frame")
			else:
				print("[CAMERA] Failed to encode frame")
		print("[CAMERA] Reading thread stopped")
		self.thread = None
		self.is_running = False
