#! /usr/bin/python
import cv2
import sys

cascPath = '/home/robby/Downloads/opencv-3.0.0-beta/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
eye_cascade = cv2.CascadeClassifier('/home/robby/Downloads/opencv-3.0.0-beta/data/haarcascades/haarcascade_eye.xml')

# Try to make the while portion a method so it returns individual boxes! 

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    print ret
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print gray

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        # flags=cv2.HAAR_SCALE_IMAGE
    )

    # img = cv2.CloneImage(frame)
    # print img

    print "There are ", len(faces) , 'faces found!'   
    # Draw a rectangle around the faces

    people = []

    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # person = ()

        # roi_gray = cv2.cvtColor( person , cv2.COLOR_BGR2GRAY)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # Only update the display if there's two eyes in the 'face' rectangle
        if len(eyes) != 0:
            # print cv2.imdecode(roi_color ,  3)
            people.append( roi_color )
            # cv2.imshow( 'YES' , frame[y: y+h, x: x+w])



    to_show = [(x,y,w,h) for person in people]
    count = 0 
    for thing in to_show:
        print x
        print 'thing' ,  thing
        count += 1

        cv2.imshow("I've just seen a face"+ str(count), frame[y: y+h, x: x+w])
        cv2.waitKey(10)


        # print "There are ", len(roi_gray) , 'eye pairs found!' 

    # Display the resulting frame
    
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
