import os

file = "app.py"

# FIX: add encoding="utf-8"
with open(file, "r", encoding="utf-8") as f:
    content = f.read()

# Check if it's a Streamlit app
if "streamlit" in content:
    print("Running as Streamlit app...")
    os.system(f"streamlit run {file}")
else:
    print("Running as normal Python script...")
    os.system(f"python {file}")