# AI Data Agent

> A data analysis service that ingests structured files, transforms them with Python and Pandas, and layers AI interpretation on top of the underlying numerical output.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/ai-data-agent)

---

## What It Does

Python and Pandas handle the deterministic analysis work first — cleaning, filtering, aggregation, derived columns, and trend calculation. GPT-4o then takes the transformed output and explains what the numbers mean in business terms: summarizing patterns, flagging anomalies, and producing narrative decision support tied to the actual data.

The result is a clean analytical response payload ready for reporting tools, BI dashboards, and stakeholder summaries.

**Use cases:** internal BI workflows and analysis-heavy automation systems.

---

## Backend Workflow

**Step 1 — Data ingestion** `Input: Structured data files`
Accepts datasets or structured file payloads for analysis. Loads the source into a Python data-processing environment. Confirms the schema and prepares the dataset for transformation.

**Step 2 — Transformation layer** `Intermediate: Analysis-ready dataset`
Handles cleaning, filtering, derived columns, and aggregation logic using Pandas. Prepares numerical outputs suitable for trend and summary analysis. Creates a machine-readable analytical context for the model layer.

**Step 3 — AI interpretation** `Processing: Pattern explanation + summaries`
Summarizes trends, anomalies, and important data relationships using GPT-4o. Turns raw numerical outputs into narrative decision support. Produces AI-assisted insight tied directly to the transformed data.

**Step 4 — Delivery layer** `Output: Analytical response payload`
Packages outputs into API-ready structured results. Supports external dashboards, reporting tools, and stakeholder summaries. Acts as a reusable analysis endpoint across business workflows.

---

## Architecture Note

> **Computation layer** — Python and Pandas handle all deterministic analysis before the model is involved. The model never runs math — it interprets results that have already been computed.
>
> **Interpretation layer** — GPT-4o explains what the numbers mean in business terms, constrained by the actual computed output.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| Data Engine | Pandas, NumPy |
| AI Model | OpenAI GPT-4o |
| BI Integration | Tableau |
| Deployment | Google Cloud Run — us-east1 |

---

## Local Development

```bash
git clone https://github.com/HansStewart/ai-data-agent.git
cd ai-data-agent
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY to .env
python main.py
# Open http://localhost:8080
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | GPT-4o interpretation layer |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| AI Content Pipeline | [github.com/HansStewart/ai-content-pipeline](https://github.com/HansStewart/ai-content-pipeline) |
| Voice-to-CRM Agent | [github.com/HansStewart/voice-to-crm](https://github.com/HansStewart/voice-to-crm) |
| Pipeline Intelligence Agent | [github.com/HansStewart/pipeline-intelligence-agent](https://github.com/HansStewart/pipeline-intelligence-agent) |
| CRM Automation Agent | [github.com/HansStewart/crm-agent](https://github.com/HansStewart/crm-agent) |
| Multi-Agent BI System | [github.com/HansStewart/multi-agent](https://github.com/HansStewart/multi-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**
