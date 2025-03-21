from app import app
from flask import request, redirect, render_template
import os
import uuid
from app import db

# Pages
@app.route('/')
def home():
    # Ambil Halaman HTML Home
    return render_template('index.html')


@app.route('/LihatBarang')
def lihatBarang():
    # Akses Variabel Global
    # global db

    # # Ambil Halaman HTML LihatBarang
    # file = open("./templates/read.html", "r")
    # page = file.read()
    # file.close()

    # Ambil Data dari Database
    documents = db.collection("Inventori").get()
    # data = "" # Kontainer Data ke HTML
    # if(len(documents)>0):
    #     # Jika Ada Data, Masukkan Data ke String HTML
    #     for document in documents:
    #         data += "<tr>" # Pembukaan Row HTML
    #         data += f"<td>{document.id} - " \
    #                 f"<a href='/UbahBarang?idbarang={document.id}'>Ubah</a> - " \
    #                 f"<a href='/HapusBarang?idbarang={document.id}'>Hapus</a></td>"
    #         data += f"<td>{document.to_dict()['nama']}</td>"
    #         data += f"<td>{document.to_dict()['jumlah']}</td>"
    #         data += f"<td>{document.to_dict()['deskripsi']}</td>"
    #         data += "</tr>" # Penutupan Row HTML
    # else:
    #     # Jika Tidak Ada Data, Tampilkan Kosong
    #     data = "<tr><td colspan='4'>Data Kosong</td></tr>"
    # page = page.replace("<tr>Data</tr>", data)

    # Konversi Data Firestore ke Format List
    data = []
    for document in documents:
        item = document.to_dict()
        item["id"] = document.id  # Simpan ID dokumen
        data.append(item)
    
    # Render Template dengan Data
    return render_template("read.html", data=data)























# @app.route('/TambahBarang')
# def tambahBarang():
#     # Akses Variabel Global
#     global db
#     # UUID Generator -> Kapital -> Potong 10 Karakter
#     idBarang = str(uuid.uuid4()).replace("-","").upper()[0:10]
#     # Ambil Halaman HTML TambahBarang
#     file = open("./static/add.html", "r")
#     page = file.read()
#     file.close()
#     # Modifikasi input untuk ID Barang di HTML
#     page = page.replace("IDBARANG", idBarang)
#     # Tampilkan HTML dengan Return
#     return page

# @app.route('/kirimData', methods=["POST"])
# def kirimData():
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
#     file = open("static/update.html", "r")
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
#     file = open("WebApp/html/delete.html", "r")
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