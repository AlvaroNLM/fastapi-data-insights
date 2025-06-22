import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

# Function to analize the csv
def analyze_csv(file) -> dict:
    """
    Perform basic exploratory data analysis on a CSV file.

    Parameters:
    - file: A file-like object (uploaded CSV)

    Returns:
    - Dictionary with dataset shape, column names, data types, missing values,
      descriptive statistics, and a base64-encoded correlation plot image.
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file)

    # Collect basic dataset information
    summary = {
        "shape": df.shape,  # Number of rows and columns
        "columns": list(df.columns),  # Column names
        "missing_values": df.isnull().sum().to_dict(),  # Missing values per column
        "dtypes": df.dtypes.astype(str).to_dict(),  # Data types of each column
        "describe": df.describe(include='all').to_dict()  # Descriptive stats
    }

    # Prepare correlation matrix plot for numeric columns
    plot_buffer = io.BytesIO()  # In-memory buffer to store the plot image

    # Compute correlation between numerical columns
    corr = df.select_dtypes(include='number').corr()

    # Create heatmap with seaborn
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.tight_layout()

    # Save the plot to the buffer as PNG
    plt.savefig(plot_buffer, format='png')
    plt.close()  # Close plot to free memory
    plot_buffer.seek(0)

    # Encode the plot image in base64 to include in JSON
    img_base64 = base64.b64encode(plot_buffer.read()).decode('utf-8')

    # Add image to the response dictionary
    summary["correlation_plot"] = img_base64

    return summary
