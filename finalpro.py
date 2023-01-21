import cv2, time
import tkinter
import tkinter.font as font



def camera():
  motion=0
  video=cv2.VideoCapture(0)
  fourcc = cv2.VideoWriter_fourcc(*'DIVX')
  out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(video.get(3)),int(video.get(4))))
  while True:
    check, frame1=video.read()
    check, frame2=video.read()
    delta_frame=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(delta_frame,cv2.COLOR_BGR2GRAY)
    blurred=cv2.GaussianBlur(gray,(21,21),0)
    _,threshold_frame=cv2.threshold(blurred,50,255,cv2.THRESH_BINARY)
    threshold_frame=cv2.dilate(threshold_frame,None,iterations=2)
    (cntr,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cntr:
        if cv2.contourArea(contour)>=5000:
            continue
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        motion=motion+1
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("abcde",frame1)
    if motion>=50:
        
        print(motion)
        out.write(frame1)
  video.release()
  cv2.destroyAllWindows()



top = tkinter.Tk()
top.geometry("500x500")
myFont = font.Font(family='Helvetica', size=20, weight='bold')
redbutton = tkinter.Button(top, text = "Start", fg = "green", command = camera)


redbutton['font'] = myFont
redbutton.place(x = 100, y = 100)
top.mainloop()