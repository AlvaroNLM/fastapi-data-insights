# from libraries
import io
# from files
from app.analysis import analyze_csv

def test_analysis_simple():
    """
    Simple test that checks if the analysis function returns expected keys for a basic CSV input.
    """
    # Create a simple CSV string
    csv_data = "a,b,c\n1,2,3\n4,5,6"

    # Pass it as a file-like object (StringIO)
    result = analyze_csv(io.StringIO(csv_data))

    # Assert that shape is correct and 'describe' is included
    assert "shape" in result
    assert result["shape"] == (2, 3)
