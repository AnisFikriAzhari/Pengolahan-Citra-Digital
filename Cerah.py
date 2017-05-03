
# TUGAS PENGOLAHAN CITRA DIGITAL #

# Nama       : Anis Fikri Azhari
# NIM        : 5301414090
# Prodi      : Pendidikan Teknik Elektro


import numpy as np
import cv2

# Mengenali camera webcam
camera = cv2.VideoCapture(0) 

while(True):
    # Mengambil gambar dari frame ke frame
    ret, frame = camera.read()
    # Merubah dari gambar berwarna ke hitam putih
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Merubah tingkat kecerahan gambar
    bright = cv2.addWeighted (gray,1.5, np.zeros(gray.shape, gray.dtype), 0, 5)
    # Menampilkan Hasil Perubahan Gambar pada window dengan judul 'BlackWhite Cerah'
    cv2.imshow('BlackWhite Cerah',bright)
    # Program Mengenali Tombol
    key = cv2.waitKey(1) 
    if key == 120: # Angka tersebut diambil dari kode ASCII keyboard yaitu menampilkan huruf "X"
        break

# Saat semua program diatas telah di eksekusi maka camera/webcam akan bekerja
camera.release()
cv2.destroyAllWindows()



