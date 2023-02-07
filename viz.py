import cv2
import re, yaml
import pytesseract as tst
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from urx.toolbox import CountsPerSec




if __name__ == '__main__':
  tst.pytesseract.tesseract_cmd = r'D:\\Tesseract-OCR\\tesseract.exe'

  vid = cv2.VideoCapture('./WOW_test3.mp4')
  ret, cnt = True, CountsPerSec()
  fps, total = vid.get(cv2.CAP_PROP_FPS), vid.get(cv2.CAP_PROP_FRAME_COUNT)
  intv = int(fps/3)
  thresh_x, thresh_y = total/fps, 150000

  x, y = [], []

  axes = plt.gca()
  axes.set_xlim(0, thresh_x)
  axes.set_ylim(0, thresh_y)
  line, = axes.plot(x, y, 'r-')

  while True:
    ret, frame = vid.read()
    cnt.increment()
    if not ret: break

    # 由笔记本录制, (1440, 2304, 3)
    if cnt.cnt % intv == 0: # 计算AP
      frame_crp = frame[:38, :100]
      frame_gray = cv2.cvtColor(frame_crp, cv2.COLOR_BGR2GRAY)
      _, frame_gray = cv2.threshold(frame_gray, 200, 255, cv2.THRESH_OTSU)


      ap = tst.image_to_string(frame_gray, config='outputbase digits')
      ap = re.sub("[^0-9]", "", ap)
      
      if len(ap) and int(ap) < thresh_y:
        x.append(cnt.cnt/fps)
        y.append(int(ap))

        print(cnt.fps)

  #       line.set_xdata(x)
  #       line.set_ydata(y)
    
  #       # 可视化
  #       plt.draw()
  #       plt.pause(1e-17)
        
  #       cv2.imshow('AP', frame_gray)
  #   frame = cv2.resize(frame, (640, 400))
  #   cnt.annotate_fps(frame)
  #   cv2.imshow('_', frame)
  #   if cv2.waitKey(1) == 27: break
  # plt.show()

  # 保存数据
  np.array(x).dump('_x.npy')
  np.array(y).dump('_y.npy')
