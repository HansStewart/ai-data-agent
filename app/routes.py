from flask import Blueprint, request, jsonify
import pandas as pd
import io
from app.agent import analyze_data

# Create a blueprint (a section of your app)
main = Blueprint('main', __name__)

# Home route - just to test the API is running
@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "AI Data Analysis Agent is running!",
        "status": "healthy"
    })

# Main analysis route - accepts a CSV file and returns insights
@main.route('/analyze', methods=['POST'])
def analyze():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    # Check if it's a CSV file
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Please upload a CSV file"}), 400
    
    try:
        # Read the CSV file into a pandas DataFrame
        contents = file.read().decode('utf-8')
        df = pd.read_csv(io.StringIO(contents))
        
        # Send to AI agent for analysis
        insights = analyze_data(df)
        
        return jsonify({
            "status": "success",
            "rows": len(df),
            "columns": list(df.columns),
            "insights": insights
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500