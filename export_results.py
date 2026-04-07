from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os

# Load API key
load_dotenv()
print("🚀 Starting direct export (no server needed)...")

# Connect directly to OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the CSV
df = pd.read_csv('test_data.csv')
print(f"✅ CSV loaded! Shape: {df.shape}")

# Create summary
summary = f"""
Dataset Overview:
- Rows: {len(df)}
- Columns: {list(df.columns)}
- First 5 rows:
{df.head().to_string()}

Basic Statistics:
{df.describe().to_string()}
"""

print("📤 Sending to OpenAI directly...")

# Call OpenAI directly
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an expert data analyst. Analyze this dataset and give clear insights."
        },
        {
            "role": "user", 
            "content": f"Analyze this dataset:\n{summary}"
        }
    ],
    max_tokens=1000
)

insights = response.choices[0].message.content
print("✅ Got AI insights!")

# Save for Tableau
df.to_csv('tableau_data.csv', index=False)
print("✅ tableau_data.csv saved!")

# Save insights
with open('ai_insights.txt', 'w') as f:
    f.write(insights)
print("✅ ai_insights.txt saved!")

print("\n🤖 AI Insights Preview:")
print(insights[:500])
print("\n🎉 Export complete!")