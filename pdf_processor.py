import os
import json
import pdfplumber
from pypdf import PdfReader
import pandas as pd

class PDFProcessor:
    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target PDF does not exist: {file_path}")
        self.file_path = file_path

    def extract_text(self) -> str:
        text_output = []
        with pdfplumber.open(self.file_path) as pdf:
            for page_idx, page in enumerate(pdf.pages, start=1):
                extracted = page.extract_text()
                if extracted:
                    text_output.append(f'--- Page {page_idx} ---\n' + extracted)
        return '\n\n'.join(text_output)

    def extract_tables(self) -> list:
        extracted_tables = []
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    if table and len(table) > 1:
                        headers = [str(col).strip() if col else f'col_{i}' for i, col in enumerate(table[0])]
                        df = pd.DataFrame(table[1:], columns=headers)
                        extracted_tables.append(df.to_dict(orient='records'))
        return extracted_tables

    def export_to_json(self, output_path: str):
        data = {
            'source_file': os.path.basename(self.file_path),
            'text': self.extract_text(),
            'tables': self.extract_tables()
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f'✅ Data exported successfully to: {output_path}')
