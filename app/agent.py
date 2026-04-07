from openai import OpenAI
from dotenv import load_dotenv
import os

# Load your API key from .env file
load_dotenv()

# Connect to OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_data(df):
    """
    Takes a pandas DataFrame and uses OpenAI to analyze it.
    Returns a string of insights.
    """
    
    # Create a summary of the data to send to OpenAI
    summary = f"""
    Dataset Overview:
    - Rows: {len(df)}
    - Columns: {list(df.columns)}
    - Data Types: {df.dtypes.to_dict()}
    - First 5 rows:
    {df.head().to_string()}
    
    Basic Statistics:
    {df.describe().to_string()}
    
    Missing Values:
    {df.isnull().sum().to_dict()}
    """
    
    # Ask OpenAI to analyze the data
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are an expert data analyst. 
                Analyze the dataset provided and give clear, 
                actionable insights. Include:
                1. Key patterns and trends
                2. Notable statistics
                3. Any data quality issues
                4. Business recommendations
                Keep your response clear and beginner-friendly."""
            },
            {
                "role": "user",
                "content": f"Please analyze this dataset:\n{summary}"
            }
        ],
        max_tokens=1000
    )
    
    # Extract and return the AI's response
    return response.choices[0].message.content