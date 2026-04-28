# pip install fastapi uvicorn
from fastapi import FastAPI

# uvicorn main:app --reload
# --reload ini akan baca file kamu terus terusan

# instance
app = FastAPI()


# URL:       http://localhost:8000/
# Route: GET                      /
# Route / Endpoint itu "mirip" = sama aja
# "/" = root
@app.get("/")
def root():
    """Ini hanyalah untuk percobaan saja

    Returns:
        - dict: Kuncinya adalah "pesan"
    """

    # Do something...

    # Apa yang dikembalikan?
    # Karena ini adalah REST API
    # Maka yang dikembalikan itu adalah..... JSON
    # kumpulan dari dict / list
    return {"pesan": "hello world"}


# URL:       http://localhost:8000/iseng
# Route: GET                      /iseng
@app.get("/iseng")
def get_iseng():
    return {"hanyalah": "iseng belaka"}


# URL:       http://localhost:8000/nama/masukkin_nama_kamu
# Route: GET                      /nama/{name}
@app.get("/nama/{name}")
def baca_name(name):
    # si curly bracket dari @app.get, itu akan menjadi arg di dalam fungsi
    return {"name": name, "message": f"Halo, nama yang dituliskan adalah {name}"}


# URL:       http://localhost:8000/barangs/10
# Route: GET                      /barangs/{item_id}
@app.get("/barangs/{item_id}")
def baca_item_id(item_id: int):  # type hint
    # Do something
    print(f"Item id yang didapatkan adalah {item_id}")
    print(type(item_id))

    return {"id": item_id}


# =================
list_items = []


# URL:         http://localhost:8000/items
# Route: POST  http://localhost:8000/items
@app.post("/items")
def tambah_items(nama: dict):
    print(f"Nama barang adalah {nama}")

    list_items.append(nama)
    print(f"List items: {list_items}")

    return {"message": "barang berhasil ditambahkan"}
