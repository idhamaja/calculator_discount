# ==============================================
# KALKULATOR DISKON SEDERHANA
# ==============================================

# Memanggil library tkinter (untuk membuat jendela/aplikasi berGUI)
# "as tk" artinya kita singkat namanya menjadi tk
import tkinter as tk


# ----------------------------------------------
# FUNGSI: dijalankan saat tombol "Hitung" diklik
# ----------------------------------------------
def hitung():

    # try = "coba jalankan kode ini"
    # Kalau ada error (misalnya user mengetik huruf), lompat ke except
    try:
        # .get() mengambil teks yang diketik user di kolom input
        # float() mengubah teks menjadi angka desimal
        harga = float(entry_harga.get())

        # "or 0" artinya: kalau kolom kosong, pakai angka 0
        diskon = float(entry_diskon.get() or 0)

        # int() mengubah teks menjadi bilangan bulat (tanpa koma)
        jumlah = int(entry_jumlah.get())

    # except = "kalau terjadi error jenis ValueError, jalankan ini"
    # ValueError muncul saat teks tidak bisa diubah jadi angka
    except ValueError:
        # .config() mengubah tampilan label
        # fg="red" membuat tulisan berwarna merah
        label_hasil.config(text="Input harus berupa angka!", fg="red")

        # return = hentikan fungsi, jangan lanjut ke perhitungan
        return

    # ----- Proses perhitungan -----
    subtotal = harga * jumlah            # total harga sebelum diskon
    potongan = subtotal * diskon / 100   # besar uang yang didiskon
    total = subtotal - potongan          # total yang harus dibayar

    # Menampilkan hasil ke label
    # f"..." disebut f-string, untuk memasukkan variabel ke dalam teks
    # {subtotal:,.0f} artinya: beri pemisah ribuan, tanpa angka desimal
    # \n artinya pindah baris
    label_hasil.config(
        text=f"Subtotal : Rp {subtotal:,.0f}\n"
             f"Potongan : Rp {potongan:,.0f}\n"
             f"Total    : Rp {total:,.0f}",
        fg="green",   # tulisan berwarna hijau
    )


# ----------------------------------------------
# MEMBUAT TAMPILAN (GUI)
# ----------------------------------------------

# Membuat jendela utama (dinamakan "root")
root = tk.Tk()

# Mengatur judul yang tampil di bagian atas jendela
root.title("Kalkulator Diskon")

# ----- Kolom input harga -----
# Label = teks biasa. .pack() = tempatkan di jendela (urut dari atas ke bawah)
tk.Label(root, text="Harga per barang (Rp)").pack()

# Entry = kolom untuk mengetik. Disimpan di variabel agar isinya bisa dibaca
entry_harga = tk.Entry(root)
entry_harga.pack()

# ----- Kolom input diskon -----
tk.Label(root, text="Diskon (%)").pack()
entry_diskon = tk.Entry(root)
entry_diskon.pack()

# ----- Kolom input jumlah -----
tk.Label(root, text="Jumlah barang").pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# ----- Tombol -----
# command=hitung artinya: saat diklik, jalankan fungsi hitung
# PENTING: tulis "hitung" tanpa tanda kurung ()
# pady=10 memberi jarak 10 piksel di atas dan bawah tombol
tk.Button(root, text="Hitung", command=hitung).pack(pady=10)

# ----- Label untuk menampilkan hasil -----
# Awalnya kosong (text=""), nanti diisi oleh fungsi hitung()
# font=("Courier", 11) agar huruf rata dan rapi
# justify="left" membuat teks rata kiri
label_hasil = tk.Label(root, text="", font=("Courier", 11), justify="left")

# padx = jarak kiri-kanan, pady = jarak atas-bawah
label_hasil.pack(padx=20, pady=10)

# ----------------------------------------------
# MENJALANKAN PROGRAM
# ----------------------------------------------

# mainloop() membuat jendela tetap terbuka dan menunggu aksi user
# Tanpa baris ini, jendela akan muncul sebentar lalu langsung hilang
root.mainloop()