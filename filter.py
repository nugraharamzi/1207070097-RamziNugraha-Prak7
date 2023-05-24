# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt
#jika menggunakan google colab jgn lupa load code di bawah ini
#from google.colab.patches import cv2_imshow


#bgr
img = cv2.imread('ramzi.jpg')

#rgb
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# tampilkan gambar awal tanpa filter
plt.imshow(img)
plt.show()

# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5,5),np.float32)/25
print(kernel)

# lakukan filtering
kucing_filter = cv2.filter2D(img,-1,kernel)

plt.imshow(kucing_filter)
plt.show()

# salt and pepper

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)

# plot pertama, gambar asli
plt.subplot(121),plt.imshow(cat),plt.title('Original')
plt.xticks([]), plt.yticks([])

# kedua, hasil filter
plt.subplot(122),plt.imshow(kucing_filter),
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Plot!
plt.show()

kucing_blur = cv2.blur(img,(5,5))

plt.imshow(kucing_blur)
plt.show()

# ini adalah cara lain untuk membuat sebuah kernel, 
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]         
          ])/25
print(kernel)

# buat lagi filteringnya
kucing_filter = cv2.filter2D(img,-1,kernel)

# tampilkan
plt.imshow(kucing_filter)
plt.show()

