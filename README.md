# Laporan Proyek Machine Learning - White Box Model Deployment API

### 1. Pendahuluan
Proyek ini bertujuan untuk membangun dan mendistribusikan model regresi Machine Learning (Random Forest, Ridge, Decision Tree, Linear Regression) dalam bentuk API menggunakan FastAPI dan Docker. Model ini digunakan untuk memprediksi variabel target berbasis fitur-fitur numerik.

### 2. Business Understanding
Model ini dirancang untuk digunakan dalam konteks operasional industri, khususnya dalam memprediksi nilai-nilai sensor atau parameter penting (seperti suhu, aliran batubara, atau daya aktif) agar mendukung pengambilan keputusan yang lebih presisi dalam pengelolaan proses atau aset.

Tujuan Bisnis:

- Memprediksi parameter penting secara akurat
- Memungkinkan integrasi prediksi ML ke dalam sistem lain melalui API
- Menyediakan visibilitas atas performa semua model yang telah dilatih

### 3. Data Understanding
Data yang digunakan berasal dari sensor/telemetri sistem, dengan beberapa fitur utama seperti:

- TOTAL_COAL_FLOW
- GEN_ACTIVE_POWER
- ECON_OUT_WTR_TEMP_R

Target prediksi adalah nilai sensor atau variabel numerik yang relevan (misalnya MAIN_STM_TEMP).
Dataset telah dibagi menjadi data latih dan data uji.

### 4. Data Preparation
- Data dibersihkan dari nilai-nilai kosong
- Semua fitur bersifat numerik sehingga tidak memerlukan encoding tambahan
- Data distandarisasi untuk model yang sensitif terhadap skala, seperti Ridge dan Linear Regression
- Dilakukan split data (train/test) dengan proporsi 80:20

### 5. Modeling
Model-model yang digunakan:
- Random Forest
- Ridge Regression
- Decision Tree
- Linear Regression

Setiap model dievaluasi menggunakan metrik:
- R² (R-squared)
- RMSE (Root Mean Square Error)

Model terbaik dipilih berdasarkan nilai R² tertinggi.

### 6. Evaluation
Berikut contoh hasil evaluasi model:

| Model             | R² Score | RMSE   | Best Parameters                  |
| ----------------- | -------- | ------ | -------------------------------- |
| Random Forest     | 0.307    | 112.45 | `n_estimators=100, max_depth=10` |
| Ridge Regression  | 0.294    | 114.22 | `alpha=1.0`                      |
| Decision Tree     | 0.220    | 121.35 | `max_depth=8`                    |
| Linear Regression | 0.201    | 123.80 | -                                |

Model terbaik: Random Forest

### 7. Deployment
Model dan pipeline telah di-package dan disediakan melalui sebuah REST API berbasis FastAPI. API ini kemudian dikemas menggunakan Docker agar bisa dijalankan secara konsisten di berbagai lingkungan.

Prasyaratan 
a. Python 3.8+
b. Docker

Build Docker Image
```
docker build -t white-box-model-api .
```

Jalankan Docker Container
```
docker run -p 8100:8000 white-box-model-api
```

Cek Port Terpakai
```
sudo lsof -i :8100
```

## 1. Endpoint API
Root / Health Check
- GET /
Response:

```
{ "message": "ML Model Deployment API is running." }
```

## 2. Mendapatkan Model Terbaik
- GET /best-model
Response:
```
{ "best_model": "random_forest", "score": 0.3071 }
```

## 3. Melihat Performa Semua Model
- GET /model-performance
- Response: JSON yang berisi skor evaluasi seluruh model

## 4. Prediksi dengan Model Tertentu
- POST /predict
- Header: Content-Type: application/json
- Contoh Request Body:

```
{
  "model_name": "ridge",
  "TOTAL_COAL_FLOW": 300,
  "GEN_ACTIVE_POWER": 500,
  "ECON_OUT_WTR_TEMP_R": 500
}
```

- Contoh Response:

```
{
  "model": "ridge",
  "prediction": [1013.58]
}
```

### 8. Kesimpulan
Model Random Forest memberikan performa terbaik dalam memprediksi target berdasarkan data yang diberikan. API yang dibangun memungkinkan pengguna untuk:
- Mengecek status model
- Melihat performa dan pemilihan model terbaik
- Melakukan prediksi berbasis input fitur

Dengan adanya Docker, sistem ini dapat dideploy secara portable dan dapat diintegrasikan ke berbagai platform sistem informasi industri.
