import cv2 as cv
import numpy as np
import tensorflow as tf


def main():
	# Load the trained face detection model
	model_face_detection_02 = tf.keras.models.load_model('models/model_face_detection_02.h5')


	capture = cv.VideoCapture(0)

	while True:
	    isTrue, frame = capture.read()

	    frame_pred = cv.resize(frame, (150, 150), interpolation=cv.INTER_AREA)
	    
	    pred = np.array(model_face_detection_02.predict(frame_pred[None] / 255)).reshape(155, 4)
	    
	    frame = cv.resize(frame, (1920, 1080), interpolation=cv.INTER_LINEAR)

	    
	    for rect in pred:
		cv.rectangle(frame, (int(rect[0] * 1920), int(rect[1] * 1080)), (int(rect[2] * 1920), int(rect[3] * 1080)), (200, 200, 200), thickness=2)

	    
	    cv.imshow("Video (press q to quit)", frame)
	    
	    if cv.waitKey(5) & 0xFF == ord('q'):
		break
		
	capture.release()
	cv.destroyAllWindows()






if __name__ == "__main__":
	main()

