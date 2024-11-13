import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in input_nilai:  # Menggunakan input_nilai yang benar
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        
        # Jika semua nilai valid, tampilkan hasil prediksi
        label_hasil.config(text="Hasil Prediksi: Prodi Teknologi Informasi")
    
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))  # Menampilkan pesan kesalahan yang sesuai

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Membuat input nilai mata pelajaran
input_nilai = []
for i in range(10):
    label_mata_pelajaran = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label_mata_pelajaran.pack(pady=5)
    entry_nilai = tk.Entry(root)
    entry_nilai.pack(pady=5)
    input_nilai.append(entry_nilai)

# Membuat tombol untuk hasil prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=20)

# Membuat label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="Hasil Prediksi: ")
label_hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()





#Import Tkinter: Mengimpor modul Tkinter untuk membuat GUI.
#Fungsi hasil_prediksi: Fungsi ini akan dipanggil ketika tombol "Hasil Prediksi" diklik. Ia mengubah teks pada label hasil menjadi "Teknologi Informasi".
#Membuat Jendela Utama: Menginisialisasi jendela utama aplikasi dengan judul.
#Label Judul: Membuat label untuk judul aplikasi.
#Input Nilai Mata Pelajaran: Menggunakan loop untuk membuat 10 label dan entry (input) untuk nilai mata pelajaran.
#Tombol Hasil Prediksi: Membuat tombol yang akan memanggil fungsi hasil_prediksi saat diklik.
#Label Hasil Prediksi: Label untuk menampilkan hasil prediksi.
#Menjalankan Aplikasi: Memanggil mainloop() untuk menjalankan aplikasi.