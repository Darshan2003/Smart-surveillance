import streamlit as st
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import numpy as np

@st.cache_resource()
def load_fire_model():
    model = YOLO("fire_best.pt")
    return model

@st.cache_resource()
def load_accident_model():
    model = YOLO("accident_best.pt")
    return model

st.header('Smart Surveillance System using AI')

uploaded_file = None
model_name = None

with st.sidebar:    
    model_name = st.selectbox(
        'Select a Model',
        ('Fire Detection', 'Accident Detection', 'Tampering Detection')
    )

    if model_name!='Tampering Detection':
        uploaded_file = st.text_input("Enter the path to the video file")

if model_name is not None:
    if model_name=='Tampering Detection':
        cap = cv2.VideoCapture(0)
        fgbg = cv2.createBackgroundSubtractorMOG2()
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        kernel = np.ones((5,5), np.uint8)
        stframe = st.empty()

        while(True):
            ret, frame = cap.read()
            if(frame is None):
                print("End of frame")
                break;
            else:
                a = 0
                bounding_rect = []
                fgmask = fgbg.apply(frame)
                fgmask= cv2.erode(fgmask, kernel, iterations=5) 
                fgmask = cv2.dilate(fgmask, kernel, iterations = 5)
                # cv2.imshow('frame',frame)
                stframe.image(frame, channels="BGR", use_column_width=True)  
                contours,_ = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for i in range(0,len(contours)):
                    bounding_rect.append(cv2.boundingRect(contours[i]))
                for i in range(0,len(contours)):
                    if bounding_rect[i][2] >=40 or bounding_rect[i][3] >=40:
                        a = a+(bounding_rect[i][2])*bounding_rect[i][3]
                    if(a >=int(frame.shape[0])*int(frame.shape[1])/3):
                        cv2.putText(frame,"TAMPERING DETECTED",(5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)   
                    # cv2.imshow('frame',frame) 
                    stframe.image(frame, channels="BGR", use_column_width=True)       
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
    else:
        if uploaded_file is not None:
            if st.button("Start Prediction"):
                model = None
                if model_name == "Fire Detection":
                    model = load_fire_model()
                else:
                    model = load_accident_model()
                    
                video = cv2.VideoCapture(uploaded_file)
                frame_counter = 0
                stframe = st.empty()  # Placeholder for displaying frames.

                if not video.isOpened():
                    st.error(f"Error opening video stream or file: {uploaded_file}")
                else:
                    while video.isOpened():
                        success, frame = video.read()
                        frame_counter += 1
                        if success and frame_counter % 10 == 0:
                            results = model.predict(frame)
                            annotator = Annotator(frame)
                            for r in results:
                                boxes = r.boxes
                                for box in boxes:
                                    b = box.xyxy[0]
                                    c = box.cls
                                    annotator.box_label(b, model.names[int(c)], color=(0, 0, 255))
                            frame = annotator.result()
                            stframe.image(frame, channels="BGR", use_column_width=True)  # Update the placeholder.
                    video.release()
