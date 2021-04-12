# palvelinVT_LT

## Asennus:
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Käynnistä
uvicorn app.main:app --reload --port 3000