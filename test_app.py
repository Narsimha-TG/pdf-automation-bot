import os
import sys
import unittest
from pdf_processor import PDFProcessor

class TestPDFProcessor(unittest.TestCase):
    def setUp(self):
        self.dummy_pdf = 'test_sample.pdf'
        with open(self.dummy_pdf, 'wb') as f:
            f.write(b'%PDF-1.4 dummy header for testing')

    def tearDown(self):
        if os.path.exists(self.dummy_pdf):
            os.remove(self.dummy_pdf)
        if os.path.exists('test_out.json'):
            os.remove('test_out.json')

    def test_instantiation(self):
        proc = PDFProcessor(self.dummy_pdf)
        self.assertEqual(proc.file_path, self.dummy_pdf)

    def test_export(self):
        proc = PDFProcessor(self.dummy_pdf)
        success = proc.export_to_json('test_out.json')
        self.assertTrue(success)
        self.assertTrue(os.path.exists('test_out.json'))

if __name__ == '__main__':
    unittest.main()
