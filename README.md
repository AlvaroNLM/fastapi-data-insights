# fastapi-data-insights
FastAPI-based REST API for automated exploratory data analysis.

1. Create virtual environment (optional but recommended)

``python -m venv venv``
``source venv/bin/activate   # On Windows use: venv\Scripts\activate``

2. Install dependencies

``pip install -r requirements.txt``

3. Run the API with Uvicorn

``uvicorn app.main:app --reload``

4. Test it locally

* Open your browser at: http://localhost:8000/docs
* Or use curl:
    * curl -X POST "http://localhost:8000/analyze/" \
        * -H "accept: application/json" \
        * -H "Content-Type: multipart/form-data" \
        * -F "file=@your_file.csv"