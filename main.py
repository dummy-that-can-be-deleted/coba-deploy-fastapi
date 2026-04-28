import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Misalnya ini adalah data awal yang kita punya
data_barang = [
    {"id": 1, "nama": "Laptop", "harga": 10000000},
    {"id": 2, "nama": "Smartphone", "harga": 5000000},
    {"id": 3, "nama": "Tablet", "harga": 3000000},
]


# GET /items - Mengambil semua barang
@app.get("/items")
def get_items():
    return {"data": data_barang}


# POST /items - Menambahkan barang baru
@app.post("/items")
def add_item(item: dict):
    # Perhatikan di atas, kita menggunakan tipe data dict untuk item.
    # Ini nanti kalau pakai Postman, kita kirim data langsung dalam format JSON, misalnya:
    # {
    #     "nama": "Headphone",
    #     "harga": 1500000
    # }

    # Generate ID baru berdasarkan ID terakhir di data_barang
    new_id = data_barang[-1]["id"] + 1 if data_barang else 1
    item["id"] = new_id

    # Di sini kita langsung tambahkan item baru ke data_barang
    data_barang.append(item)

    # Consnya adalah, kita ga bisa akses value nama atau harga di sini
    # Karena item itu dict, jadi kita harus aksesnya dengan item["nama"] atau item["harga"]
    print(f"Barang baru ditambahkan: {item['nama']} dengan harga {item['harga']}")

    return {"message": "Barang berhasil ditambahkan", "data": item}


# Cara alternatifnya adalah dengan menggunakan Pydantic
# Harus install dulu via perintah `pip install pydantic``
from pydantic import BaseModel


class Item(BaseModel):
    nama: str
    harga: int


# POST /items-pydantic - Menambahkan barang baru dengan Pydantic
@app.post("/items-pydantic")
def add_item_pydantic(item: Item):
    new_id = data_barang[-1]["id"] + 1 if data_barang else 1

    # Konversi Pydantic model ke dict untuk nambahin ID
    item_dict = item.dict()
    item_dict["id"] = new_id

    # Ujungnya yang ditambahin adalah "dict" yang sudah ada ID-nya
    data_barang.append(item_dict)

    # Di sini kita bisa akses item.nama dan item.harga secara lansgung.
    print(f"Barang baru ditambahkan: {item.nama} dengan harga {item.harga}")

    return {"message": "Barang berhasil ditambahkan", "data": item_dict}


# GET /stu-perf - Contoh endpoint untuk mengambil data performa mahasiswa
@app.get("/stu-perf")
def get_student_performance():
    # 1. Tahap Baca data (CSV)
    df = pd.read_csv("students-performance.csv")

    # Di pagi tadi awalnya "Series" (banyak baris, cuma 1 kolom),
    # Sekarang kita pakai "DataFrame" (tabel, banyak baris banyak kolom)

    # 2. Tahap Modifikasi DataFrame
    df_mod = df[["gender", "math score", "reading score", "writing score"]]
    df_mod["average score"] = (
        df_mod[["math score", "reading score", "writing score"]].mean(axis=1).round(2)
    )

    # 3. Tahap Konversi DataFrame ke List of Dicts
    data = df_mod.to_dict(orient="records")

    # Baru bisa kita return data yang sudah dalam format list of dicts
    return {"data": data}
