from django.shortcuts import render

# Create your views here.
# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
import os
# Object Detection
from imageai.Detection import ObjectDetection
obj_detector = ObjectDetection()
execution_path = os.getcwd()


# define the path to the face detector
FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))
EYE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_eye.xmll".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))

def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)

	# otherwise, the image does not reside on disk
	else:
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.request.urlopen(url)
			data = resp.read()

		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()

		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)

	# return the image
	return image

@csrf_exempt
def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}

	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])

		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)

			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)

			# load the image and convert
			image = _grab_image(url=url)

		# Image for Object Detection
		cv2.imwrite(os.path.join(execution_path , "admin_app/api/input_media/image.png"),image)

		# return JsonResponse({"image":FACE_DETECTOR_PATH,"sucess":True})
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


		detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
		# detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

		# return JsonResponse({"image":FACE_DETECTOR_PATH,"sucess":True})
		rects = detector.detectMultiScale(
		    gray,
		    scaleFactor=1.2,
		    minNeighbors=5,
		    minSize=(30, 30),
		    #flags=0#cv2.CASCADE_SCALE_IMAG
		)
		#Faces Detected
		for (x,y,w,h) in rects:
		    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		    roi_gray = gray[y:y+h, x:x+w]
		    roi_color = image[y:y+h, x:x+w]
		    # eyes = eye_cascade.detectMultiScale(roi_gray)
		    # for (ex,ey,ew,eh) in eyes:
		    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		#cv2.imwrite('images/',image)
		cv2.imwrite('media/admin_app/image.jpg',image)
		# cv2.waitKey(0)
		# cv2.destroyAllWindows()



		#Object Detect Start
		# execution_path = os.getcwd()
		# return JsonResponse({'path':execution_path})
		OBJ_DETECT_MODEL_PATH = os.path.join(execution_path , "admin_app/api/objectdetectionmodels/resnet50_coco_best_v2.0.1.h5")
		# INPUT_PATH = "{base_path}/input_media/images.jpg".format(base_path=os.path.abspath(os.path.dirname(__file__)))
		# OUTPUT_PATH = "{base_path}/output_media/object.jpg".format(base_path=os.path.abspath(os.path.dirname(__file__)))

		# obj_detector.setModelTypeAsTinyYOLOv3()
		obj_detector.setModelTypeAsRetinaNet()
		# obj_detector.setModelTypeAsYOLOv3()
		# obj_detector.setModelTypeAsTinyYOLOv3()
		obj_detector.setModelPath(OBJ_DETECT_MODEL_PATH)
		obj_detector.loadModel()

		custom = obj_detector.CustomObjects(person=True, car=True, bus=True)
		detections = obj_detector.detectCustomObjectsFromImage( custom_objects=custom, input_image=os.path.join(execution_path , "admin_app/api/input_media/image.png"), output_image_path=os.path.join(execution_path , "admin_app/api/output_media/imagenew.png"), minimum_percentage_probability=30)
		for eachObject in detections:
		     print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
		     print("--------------------------------")
		#for eachObject in detections:
		   # print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
		   #print("--------------------------------")

		#detections = detector.detectObjectsFromImage(input_image="image.jpg", output_image_path="imagenew.jpg", minimum_percentage_probability=30)
		# custom = detector.CustomObjects(person=True, dog=True)
		# detections = detector.detectCustomObjectsFromImage( custom_objects=custom, input_image=os.path.join(execution_path , "image3.jpg"), output_image_path=os.path.join(execution_path , "image3new-custom.jpg"), minimum_percentage_probability=30)


		# detection = obj_detector.detectObjectsFromImage(input_image=INPUT_PATH, output_image_path=OUTPUT_PATH, extract_detected_objects=True, minimum_percentage_probability=30)
		#
		# for eachItem in detection:
		#     print(eachItem["name"] , " : ", eachItem["percentage_probability"])

		#IMAGE SHOW
		#from IPython.display import Image
		#Image("image_new.png")

		#Object Detect End


		# construct a list of bounding boxes from the detection
		rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]

		# update the data dictionary with the faces detected
		data.update({"num_faces": len(rects), "faces": rects, "success": True})

	# return a JSON response
	return JsonResponse(data)
