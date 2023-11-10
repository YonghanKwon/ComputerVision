import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

def min(a,b):
    if a>b:
        return b
    else:
        return a
def max(a,b):
    if a>b:
        return a
    else:
        return b
    
def AL(arr,dist_func):
    for i in range(1,h):
        for j in range(1,w):
            arr[i][j]=min(arr[i][j],arr[i-1][j]+dist_func(-1,0))
            arr[i][j]=min(arr[i][j],arr[i-1][j-1]+dist_func(-1,-1))
            arr[i][j]=min(arr[i][j],arr[i][j-1]+dist_func(0,-1))
            if i!=h-1:
                arr[i][j]=min(arr[i][j],arr[i+1][j-1]+dist_func(1,-1))
def BR(arr,dist_func):
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i!=h-1:
                arr[i][j]=min(arr[i][j],arr[i+1][j]+dist_func(1,0))
            if j!=w-1:
                arr[i][j]=min(arr[i][j],arr[i][j+1]+dist_func(0,1))
            if i!=h-1 and j!=w-1:
                arr[i][j]=min(arr[i][j],arr[i+1][j+1]+dist_func(1,1))
            if i!=0 and j!=w-1:
                arr[i][j]=min(arr[i][j],arr[i-1][j+1]+dist_func(-1,1))
def eclidean(a,b):
    return math.sqrt(math.pow(a,2)+math.pow(b,2))
def city(a,b):
    return abs(a)+abs(b)
def chess(a,b):
    return max(abs(a),abs(b))


img_file='CV_assign2.png'

img=cv.imread(img_file,cv.IMREAD_GRAYSCALE)
h,w=img.shape
print(h,w)
img_dist_orig=np.zeros((h,w))
#initialization
for i in range(h):
    for j in range(w):
        if img[i][j] == 0:
            img_dist_orig[i][j]=0
        elif img[i][j]==255:
            img_dist_orig[i][j]=h*w

img_dist_eucl=img_dist_orig.copy()
img_dist_city=img_dist_orig.copy()
img_dist_chess=img_dist_orig.copy()
max_eucl=0
max_city=0
max_chess=0
AL(img_dist_eucl,eclidean)
BR(img_dist_eucl,eclidean)
print('euclidean')
AL(img_dist_city,city)
BR(img_dist_city,city)
print('city')
AL(img_dist_chess,chess)
BR(img_dist_chess,chess)
print('chess')


for i in range(h):
    for j in range(w):
        if max_eucl < img_dist_eucl[i][j]:
            max_eucl=img_dist_eucl[i][j]
        if max_city < img_dist_city[i][j]:
            max_city=img_dist_city[i][j]
        if max_chess < img_dist_chess[i][j]:
            max_chess=img_dist_chess[i][j]
print(h*w,max_eucl,max_city,max_chess)
for i in range(h):
    for j in range(w):
        img_dist_eucl[i][j]=255*img_dist_eucl[i][j]/max_eucl
        img_dist_city[i][j]=255*img_dist_city[i][j]/max_city
        img_dist_chess[i][j]=255*img_dist_chess[i][j]/max_chess
plt.subplot(1,3,1)
plt.xticks([])
plt.yticks([])
plt.title('img_eucl')
plt.imshow(img_dist_eucl,cmap='gray')
plt.subplot(1,3,2)
plt.xticks([])
plt.yticks([])
plt.title('img_city')
plt.imshow(img_dist_city,cmap='gray')
plt.subplot(1,3,3)
plt.xticks([])
plt.yticks([])
plt.title('img_chess')
plt.imshow(img_dist_chess,cmap='gray')
plt.show()