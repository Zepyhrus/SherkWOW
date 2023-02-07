import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
  x, y = np.load('_x.npy', allow_pickle=True), np.load('_y.npy', allow_pickle=True)

  plt.plot(x, y, 'r-')
  plt.show()




