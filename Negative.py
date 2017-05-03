
# TUGAS PENGOLAHAN CITRA DIGITAL #

# Nama       : Anis Fikri Azhari
# NIM        : 5301414090
# Prodi      : Pendidikan Teknik Elektro


import numpy as np 
import cv2

# Mengenali camera webcam
camera = cv2.VideoCapture(0) #Mengenali camera webcam

while(True):
    # Mengambil gambar dari frame ke frame
    ret, frame = camera.read()
    # Merubah dari gambar berwarna ke hitam putih
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Memproses gambar hitam putih menjadi negatif dan menampilkannya ke window dengan judul 'Negative Camera'
    cv2.imshow('Negative Camera',-gray) # Simbol '-' merupakan program untuk merubah gambar hitam putih menjadi negatif
    # Program Mengenali Tombol
    key = cv2.waitKey(1) 
    if key == 113: # Angka tersebut diambil dari kode ASCII keyboard yaitu menampilkan huruf "Q"
        break

# Saat semua program diatas telah di eksekusi maka camera/webcam akan bekerja
camera.release()
cv2.destroyAllWindows()