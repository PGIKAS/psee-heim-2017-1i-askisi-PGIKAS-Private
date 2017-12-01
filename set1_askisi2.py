import numpy as np
from scipy.misc import imread, imsave
import sys

if len(sys.argv)!=2:
    exit(0)



image = imread(sys.argv[1]).astype(np.float32)
imageNew = imread(sys.argv[1]).astype(np.float32)

M = image.shape[0]
N = image.shape[1]

for k in range(9):
    thres = np.amin(image) + k*(np.amax(image) -  np.amin(image))/9

    for i in range(M):
        for j in range(N):
            if image[i][j]<=thres:
                imageNew[i][j]=0
            else:
                imageNew[i][j]=255


    imsave(str(k)+'.png', imageNew)
