# White Box Model Deployment API

API deployment untuk model Machine Learning regresi (Random Forest, Ridge, Decision Tree, Linear) menggunakan FastAPI dan Docker.

## Fitur

- Health check endpoint untuk memastikan API berjalan
- Mendapatkan model terbaik beserta skor evaluasi
- Melihat performa semua model yang sudah dilatih
- Melakukan prediksi menggunakan model tertentu dengan input fitur

## Cara Menjalankan

### Prasyarat

- Python 3.8+
- Docker (untuk menjalankan container)

### Build Docker Image

```
docker build -t white-box-model-api .
```

### Jalankan Docker Container

Jalankan container dan mapping port 8000 di container ke port 8100 di host (bisa ganti port sesuai kebutuhan):

```
docker run -p 8100:8000 white-box-model-api
```

Pastikan port 8100 belum digunakan oleh aplikasi lain. Gunakan perintah berikut untuk cek:

```
sudo lsof -i :8100
```

Jika port sudah digunakan, ganti ke port lain yang kosong.

Endpoint API
1. Root / Health Check

Method: GET

URL: http://localhost:8100/

Response:
```
{
  "message": "ML Model Deployment API is running."
}
```

2. Mendapatkan Model Terbaik
Method: GET

URL: http://localhost:8100/best-model

Response:
```
{
  "best_model": "random_forest",
  "score": 0.3071684786743205
}
```

3. Melihat Performa Semua Model
Method: GET

URL: http://localhost:8100/model-performance

Response: JSON berisi skor, RMSE, dan parameter terbaik dari semua model.

4. Prediksi dengan Model Tertentu
Method: POST

URL: http://localhost:8100/predict

Header: Content-Type: application/json

Body contoh:
```
{
  "model_name": "ridge",
  "TOTAL_COAL_FLOW": 300,
  "GEN_ACTIVE_POWER": 500,
  "ECON_OUT_WTR_TEMP_R": 500
}
```

Response contoh:
```
{
  "model": "ridge",
  "prediction": [1013.5823982767538]
}
```
