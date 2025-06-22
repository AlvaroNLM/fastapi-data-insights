# from libraries
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, Response
# from files
from app.analysis import analyze_csv

# Create a FastAPI instance
app = FastAPI(title="CSV Analyzer API")

# Define an endpoint to upload and analyze a CSV file
@app.post("/analyze/summary")
async def analyze(file: UploadFile = File(...)):
    """
    Receives a CSV file via HTTP POST, performs basic analysis, and returns results as JSON.
    
    Parameters:
    - file (UploadFile): The uploaded CSV file.

    Returns:
    - JSON object containing dataset statistics, missing values, data types, and a correlation heatmap.
    """
    
    # Check if the uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        return JSONResponse(
            status_code=400,
            content={"error": "Only CSV files are supported."}
        )

    # Run the analysis function on the uploaded file
    analysis, _ = analyze_csv(file.file)
    # Return the results as JSON
    return analysis

@app.post("/analyze/correlation-plot") 
async def analyzetoplot(file: UploadFile = File(...)):
    """
    Receives a CSV file via HTTP POST, performs basic analysis, and returns results as JSON.
    
    Parameters:
    - file (UploadFile): The uploaded CSV file.

    Returns:
    - JSON object containing dataset statistics, missing values, data types, and a correlation heatmap.
    """
    
    # Check if the uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        return JSONResponse(
            status_code=400,
            content={"error": "Only CSV files are supported."}
        )

    # Run the analysis function on the uploaded file
    _, corr_plot = analyze_csv(file.file)
    
    # Return the results as JSON
    return Response(content=corr_plot, media_type="image/png")
