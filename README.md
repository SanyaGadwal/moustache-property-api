# Moustache Property API

This is a fast, Python-based API that finds the **nearest Moustache Escapes property** within a 50km radius of a user-provided location (even if the location has minor spelling errors).

### 🔧 Tech Stack
- Python 3.11
- FastAPI
- geopy
- fuzzywuzzy
- Uvicorn

### 📦 How to Run Locally

```bash
git clone https://github.com/SanyaGadwal/moustache-property-api.git
cd moustache-property-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
