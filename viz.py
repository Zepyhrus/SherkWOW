import cv2






if __name__ == '__main__':
  vid = cv2.VideoCapture('./WOW_test1.mp4')
  ret = True

  while ret:
    ret, frame = vid.read()

    if frame.shape == (1440, 2304, 3):
      # 由笔记本录制
      frame = frame[210:250, -200:]





      
    else:
      break

    cv2.imshow('_', frame)
    if cv2.waitKey(1) == 27: break

