import argparse
import sys
from pdf_processor import PDFProcessor

def main():
    parser = argparse.ArgumentParser(description='Autonomous PDF Automation Processing Bot')
    parser.add_argument('--input', '-i', required=True, help='Path to input PDF file')
    parser.add_argument('--output', '-o', default='output.json', help='Path to export extracted JSON data')
    parser.add_argument('--mode', '-m', choices=['text', 'tables', 'all'], default='all', help='Extraction target')
    args = parser.parse_args()

    try:
        print(f'🔍 Loading PDF: {args.input}')
        processor = PDFProcessor(args.input)
        processor.export_to_json(args.output)
        print('🎉 Processing finished successfully.')
    except Exception as e:
        print(f'❌ Error during execution: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
