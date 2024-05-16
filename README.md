python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

http://127.0.0.1:8000/predict/




docs

cd docs/build
python -m http.server
http://localhost:8000



docker-compose down
docker-compose up --build
