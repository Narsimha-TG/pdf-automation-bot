# PDF Automation Bot

An automated tool built by an Autonomous AI Agent workflow to extract text and tabular data from PDF files into structured JSON.

## Requirements
- Python 3.10+
- `pip install -r requirements.txt`

## Usage
```bash
# Extract everything to JSON
python main.py --input sample.pdf --output result.json

# Extract only tables
python main.py --input sample.pdf --mode tables --output tables.json
```
