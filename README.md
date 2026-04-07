# 🤖 AI-Powered Data Analysis Agent

A production-ready REST API that accepts any CSV dataset, analyzes it using OpenAI GPT-4o, and returns actionable AI-generated insights.

## 🌐 Live Demo
Tableau Dashboard: https://public.tableau.com/app/profile/hans.stewart/viz/AIDataAnalysisAgent-PortfolioProject/AI-PoweredAirTravelAnalysisDashboard

## 🛠️ Tech Stack
- Python 3.14 — Core language
- Flask — REST API framework
- OpenAI GPT-4o — AI analysis engine
- Pandas — Data processing
- Tableau Public — Data visualization
- Docker — Containerization
- GCP Cloud Run — Cloud deployment

## 🚀 Features
- REST API endpoint that accepts any CSV file
- AI-powered data analysis using GPT-4o
- Returns structured insights in JSON format
- Interactive Tableau dashboard visualization
- Deployed on Google Cloud Platform

## 📦 Installation

1. Clone the repository
git clone https://github.com/HansStewart/ai-data-agent.git
cd ai-data-agent

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add your API key
Create a .env file and add:
OPENAI_API_KEY=your_key_here

5. Run the app
python main.py

## 🧪 API Usage

Health Check:
GET http://localhost:8080/
Returns: AI Data Analysis Agent is running!

Analyze a Dataset:
POST http://localhost:8080/analyze
Upload a CSV file and get back AI insights

Example Response:
{
  "status": "success",
  "rows": 12,
  "columns": ["Month", "1958", "1959", "1960"],
  "insights": "Key findings: Strong upward trend across all years..."
}

## 📊 How It Works
CSV Upload → Flask API → Pandas Processing → GPT-4o Analysis → JSON Insights → Tableau Visualization

## 🏗️ Project Structure
ai-data-agent/
├── app/
│   ├── __init__.py      - Flask app factory
│   ├── agent.py         - OpenAI GPT-4o integration
│   └── routes.py        - REST API endpoints
├── main.py              - Application entry point
├── requirements.txt     - Python dependencies
├── Dockerfile           - Container configuration
└── README.md            - Project documentation

## 👤 Author
Hans Stewart
GitHub: https://github.com/HansStewart
Tableau: https://public.tableau.com/app/profile/hans.stewart