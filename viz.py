import cv2
import re, yaml
import pytesseract as tst
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from urx.toolbox import CountsPerSec


def extract(frame):
  frame_num = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  _, frame_num = cv2.threshold(frame_num, 200, 255, cv2.THRESH_OTSU)

  num = tst.image_to_string(frame_num, config="outputbase digits")
  # num = re.sub("[^0-9]", "", num)

  return num, frame_num

if __name__ == '__main__':
  tst.pytesseract.tesseract_cmd = r'D:\\Tesseract-OCR\\tesseract.exe'

  vid = cv2.VideoCapture('./test1.mp4')
  ret, cnt = True, CountsPerSec()
  fps, total = vid.get(cv2.CAP_PROP_FPS), vid.get(cv2.CAP_PROP_FRAME_COUNT)
  intv = int(fps/3)
  thresh_x, thresh_y = total/fps, 150000

  x, yap, yasp = [], [], []

  axes = plt.gca()
  axes.set_xlim(0, thresh_x)
  axes.set_ylim(0, thresh_y)
  line, = axes.plot(x, yap, 'r-')
  line2, = axes.plot(x, yasp, 'g-')


  while True:
    ret, frame = vid.read()
    cnt.increment()
    if not ret: break

    # 由笔记本录制, (1440, 2304, 3)
    if cnt.cnt % intv == 0: # 计算AP
      t, frame_ap = extract(frame[:30, :200])
      t = t.strip()
      asp, ap = t[-5:], t[:-5]
      

      if len(ap) and len(asp):
        x.append(cnt.cnt/fps)
        yap.append(int(ap))
        yasp.append(int(asp))
  
        # 可视化
        line.set_xdata(x)
        line.set_ydata(yap)

        line2.set_xdata(x)
        line2.set_ydata(yasp)

        plt.draw()
        plt.pause(1e-17)
        
      cv2.imshow('AP', frame_ap)
      # cv2.imshow('ASP', frame_asp)
    frame = cv2.resize(frame, (960, 600))
    cnt.annotate_fps(frame)
    cv2.imshow('_', frame)
    if cv2.waitKey(1) == 27: break
  plt.show()

  # 保存数据
  np.array(x).dump('_x.npy')
  np.array(yap).dump('_yap.npy')
  np.array(yasp).dump('_yasp.npy')
