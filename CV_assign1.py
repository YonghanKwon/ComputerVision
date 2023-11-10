import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#load
img_file='lena.jpg'
img_color=cv.imread(img_file)
#gray_scaling
b,g,r=cv.split(img_color.astype(np.uint16))
img_gray=((b+g+r)/3).astype(np.uint8)
#histogram before Equalization
hist_before=np.zeros(256)
#histogram after Equalization
hist_after=np.zeros(256)
h,w=img_gray.shape
bit_n=0
img_gray_res=img_gray.copy()
LUT=np.zeros(256)

for i in range(h):
    for j in range(w):
        bit_n=img_gray[i][j]
        hist_before[bit_n]=hist_before[bit_n]+1

MN=h*w

sum_hist=0
for i in range(256):
    sum_hist=sum_hist+hist_before[i]
    LUT[i]=255*sum_hist/MN

for i in range(h):
    for j in range(w):
        img_gray_res[i][j]=LUT[img_gray[i][j]]
        hist_after[img_gray_res[i][j]]=hist_after[img_gray_res[i][j]]+1

pdf_orig=hist_before/np.sum(hist_before)
cdf_orig=np.cumsum(pdf_orig)
pdf_Eq=hist_after/np.sum(hist_after)
cdf_Eq=np.cumsum(pdf_Eq)

plt.subplot(3,2,1)
plt.xticks([])
plt.yticks([])
plt.title('img_orig')
plt.imshow(img_gray,cmap='gray')
plt.subplot(3,2,2)
plt.xticks([])
plt.yticks([])
plt.title('img_Eq')
plt.imshow(img_gray_res,cmap='gray')
plt.subplot(3,2,3)
plt.title('Hist_before')
plt.plot(hist_before)
plt.subplot(3,2,5)
plt.title('cdf_orig')
plt.plot(cdf_orig)
plt.subplot(3,2,4)
plt.title('Hist_after')
plt.plot(hist_after)
plt.subplot(3,2,6)
plt.title('cdf_Eq')
plt.plot(cdf_Eq)
plt.show()