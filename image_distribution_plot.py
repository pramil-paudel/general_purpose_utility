import cv2
import numpy as np

import matplotlib.image as mpimg

import matplotlib.pyplot as plt

# for the surface map
from mpl_toolkits.mplot3d import Axes3D
def plot_data():
    imbgr = cv2.imread('R_004.jpg')
    imrgb = cv2.cvtColor(imbgr, cv2.COLOR_BGR2RGB)
    # imlab = cv2.cvtColor(imbgr, cv2.COLOR_BGR2LAB)
    #
    # # Show the original image and individual color channels
    # plt.figure(0)
    # plt.subplot(2, 2, 1)
    # plt.imshow(imrgb)
    # plt.subplot(2, 2, 2)
    # plt.imshow(imbgr[:, :, 0], cmap='Blues')
    # plt.subplot(2, 2, 3)
    # plt.imshow(imbgr[:, :, 1], cmap='Greens')
    # plt.subplot(2, 2, 4)
    # plt.imshow(imbgr[:, :, 2], cmap='Reds')
    # plt.show()
    #
    # # show the LAB space iamge
    # plt.figure(1)
    # plt.subplot(2, 2, 1)
    # plt.imshow(imrgb)
    # plt.subplot(2, 2, 2)
    # plt.imshow(imlab[:, :, 0], cmap='Greys')
    # plt.subplot(2, 2, 3)
    # plt.imshow(imbgr[:, :, 1], cmap='cool')
    # plt.subplot(2, 2, 4)
    # plt.imshow(imbgr[:, :, 2], cmap='cool')
    #
    # plt.show()
    #
    # # contour map
    # plt.figure(2)
    # y = range(imlab.shape[0])
    # x = range(imlab.shape[1])
    # X, Y = np.meshgrid(x, y)
    # plt.contour(X, Y, imlab[:, :, 0], 50)
    # plt.show()

    # surface map
    plt.figure(3)
    ax = plt.axes(projection='3d')
    y = range(imrgb.shape[0])
    x = range(imrgb.shape[1])
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, imrgb[:, :, 0])

    plt.show()

if __name__ == '__main__':
    plot_data()