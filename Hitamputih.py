
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
    # Merubah dari gambar berwarna ke hitam putih
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Menampilkan hasil dari perubahan gambar bewarna ke hitam putih pada window dengan judul 'BlackWhite Camera'
    cv2.imshow('BlackWhite Camera',gray)
    # Program Mengenali Tombol
    key = cv2.waitKey(1) 
    if key == 120: # Angka tersebut diambil dari kode ASCII keyboard yaitu menampilkan huruf "X"
        break

# Saat semua program diatas telah di eksekusi maka camera/webcam akan bekerja
camera.release()
cv2.destroyAllWindows()