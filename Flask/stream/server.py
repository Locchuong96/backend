from flask import Flask,render_template,Response
import cv2 

app = Flask(__name__)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def gen_frames():
	while True:
		ret,frame = cap.read()
		if not ret:
			break 
		else:
			success, buffer = cv2.imencode('.jpg',frame)
			frame = buffer.tobytes()

			yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/video')
def video():
	return Response(gen_frames(),mimetype = 'multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
	app.run(host = '192.168.1.9',port = '5000')
