
# TUGAS PENGOLAHAN CITRA DIGITAL #

# Nama       : Anis Fikri Azhari
# NIM        : 5301414090
# Prodi      : Pendidikan Teknik Elektro


import numpy as np
import cv2

camera = cv2.VideoCapture(0) #Mengenali camera webcam

while(True):
    # Mengambil gambar dari frame ke frame
    ret, frame = camera.read()
    # Menampilkan hasil dari gambar bewarna pada window dengan judul 'Color Camera'
    cv2.imshow('Color Camera',frame)
    # Program Mengenali Tombol
    key = cv2.waitKey(1) 
    if key == 120: # Angka tersebut diambil dari kode ASCII keyboard yaitu menampilkan huruf "X"
        break

# Saat semua program diatas telah di eksekusi maka camera/webcam akan bekerja
camera.release()
cv2.destroyAllWindows()