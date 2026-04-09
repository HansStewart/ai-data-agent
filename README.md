# 🤖 AI Data Agent

    

An AI-powered data analysis agent that accepts any CSV dataset, performs structural analysis using Pandas, and returns actionable insights via GPT-4o. Results are exported to a live Tableau Public dashboard.

**Live API:** `https://ai-data-agent-559169459241.us-east1.run.app`  
**Live Dashboard:** [Tableau Public — Air Travel Analysis](https://public.tableau.com/app/profile/hans.stewart)

***

## Architecture

```
CSV Upload (multipart/form-data)
        │
        ▼
┌─────────────────────────────────┐
│         Flask REST API          │
│         POST /analyze           │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│         Pandas Analysis         │
│  dtypes · nulls · describe()    │
│  head() · shape · correlations  │
└─────────────┬───────────────────┘
              │  structured context summary
              ▼
┌─────────────────────────────────┐
│         OpenAI GPT-4o           │
│  patterns · anomalies · biz     │
│  recommendations · data quality │
└─────────────┬───────────────────┘
              │
              ▼
     JSON Insights + Tableau CSV Export
```

***

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Web Framework | Flask 3.0 + Gunicorn |
| Data Processing | Pandas |
| AI / LLM | OpenAI GPT-4o (`max_tokens=1000`) |
| Visualization | Tableau Public |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |

***

## API Reference

### `GET /`
Health check.

**Response:**
```json
{ "status": "healthy", "service": "AI Data Agent" }
```

***

### `POST /analyze`
Upload a CSV file and receive GPT-4o-powered insights.

**Request:** `multipart/form-data`
```
file: your_dataset.csv
```

**Response:**
```json
{
  "analysis": {
    "patterns": "...",
    "data_quality": "...",
    "statistics": "...",
    "business_recommendations": "..."
  },
  "summary": {
    "rows": 1000,
    "columns": 12,
    "null_count": 3
  }
}
```

***

### `POST /export`
Export analysis results as a Tableau-ready CSV.

**Response:** `text/csv` file download

***

## How It Works

1. **Ingestion** — CSV is received via multipart upload and loaded into a Pandas DataFrame
2. **Structural Analysis** — The agent extracts: row count, column names, dtypes, `.describe()`, `.head()`, null value counts
3. **Context Building** — All extracted metadata is formatted into a detailed text summary
4. **GPT-4o Reasoning** — The summary is sent with a system prompt instructing GPT-4o to identify patterns, flag anomalies, assess data quality, and return business recommendations
5. **Export** — Results are returned as JSON and optionally exported as a Tableau-compatible CSV

***

## Local Setup

```bash
git clone https://github.com/HansStewart/ai-data-agent.git
cd ai-data-agent
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
```

Run the server:
```bash
python main.py
```

Test it:
```bash
python test_api.py
```

***

## Project Structure

```
ai-data-agent/
├── app/
│   ├── agent.py          # GPT-4o analysis logic
│   └── routes.py         # Flask endpoints
├── main.py               # App entry point
├── prepare_tableau.py    # Tableau CSV prep
├── export_results.py     # Export utility
├── test_api.py           # API test suite
├── test_data.csv         # Sample dataset
├── tableau_data.csv      # Tableau-ready data
├── Dockerfile
└── requirements.txt
```

***

## Deployment

```bash
gcloud run deploy ai-data-agent \
  --source . \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated
```

***

## Part of the AI Agent Portfolio

| Agent | Description | Live URL |
|---|---|---|
| **AI Data Agent** | CSV analysis + GPT-4o insights | [↗](https://ai-data-agent-559169459241.us-east1.run.app) |
| RAG Document Intelligence | FAISS vector search + cited Q&A | [↗](https://rag-agent-559169459241.us-east1.run.app) |
| CRM Automation Agent | HubSpot + lead scoring + email gen | [↗](https://crm-agent-559169459241.us-east1.run.app) |
| Multi-Agent BI System | CrewAI 4-agent pipeline | [↗](https://multi-agent-559169459241.us-east1.run.app) |

**Author:** [Hans Stewart](https://github.com/HansStewart)