from app import app

# @app.route('/UbahBarang')
# def ubahBarang():
#     # Akses Variabel Global
#     global db
#     # Ambil ID Barang dari GET Request
#     idBarang = request.args.get('idbarang')
#     # Ambil Data di Database
#     data = db.collection("Inventori").document(idBarang).get().to_dict()
#     namaBarang = data['nama']
#     jumlahBarang = data['jumlah']
#     deskripsiBarang = data['deskripsi']
#     # Ambil Halaman HTML TambahBarang
#     file = open("./html/update-item.html", "r")
#     page = file.read()
#     file.close()
#     # Modifikasi input di HTML
#     page = page.replace("IDBARANG", idBarang.replace("Doc-",""))
#     page = page.replace("NAMABARANG", namaBarang)
#     page = page.replace("JUMLAHBARANG", jumlahBarang)
#     page = page.replace("DESKRIPSIBARANG", deskripsiBarang)
#     # Tampilkan HTML dengan Return
#     return page


# @app.route('/kirimPerubahan', methods=["POST"])
# def kirimPerubahan():
#     # Ambil Data dari Form
#     idBarang = str(request.form.get('id'))
#     namaBarang = str(request.form.get('nama'))
#     jumlahBarang = str(request.form.get('jumlah'))
#     deskripsiBarang = str(request.form.get('deskripsi'))
#     # Masukkan ke Struktur Data
#     data = {
#         'id': idBarang,
#         'nama': namaBarang,
#         'jumlah': jumlahBarang,
#         'deskripsi': deskripsiBarang
#     }
#     # Kueri ke Database
#     db.collection('Inventori').document('Doc-'+idBarang).set(data)
#     # Tampilkan Lihat Barang
#     return redirect("/LihatBarang")


# @app.route('/HapusBarang')
# def hapusBarang():
#     # Akses Variabel Global
#     global db
#     # Ambil ID Barang dari GET Request
#     idBarang = request.args.get('idbarang')
#     # Ambil Data di Database
#     data = db.collection("Inventori").document(idBarang).get().to_dict()
#     namaBarang = data['nama']
#     jumlahBarang = data['jumlah']
#     deskripsiBarang = data['deskripsi']
#     # Ambil Halaman HTML TambahBarang
#     file = open("./html/delete-item.html", "r")
#     page = file.read()
#     file.close()
#     # Modifikasi input di HTML
#     page = page.replace("IDBARANG", idBarang.replace("Doc-",""))
#     page = page.replace("NAMABARANG", namaBarang)
#     page = page.replace("JUMLAHBARANG", jumlahBarang)
#     page = page.replace("DESKRIPSIBARANG", deskripsiBarang)
#     # Tampilkan HTML dengan Return
#     return page


# @app.route('/hapusData', methods=["POST"])
# def hapusData():
#     # Ambil Data dari Form
#     idBarang = str(request.form.get('id'))
#     # Kueri ke Database
#     db.collection('Inventori').document('Doc-'+idBarang).delete()
#     # Tampilkan Lihat Barang
#     return redirect("/LihatBarang")
