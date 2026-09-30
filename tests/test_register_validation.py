"""Regression tests for the storage defects found during repository review."""
import csv
import importlib.util
import io
import unittest
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'scripts/validate_registers.py'
spec=importlib.util.spec_from_file_location('validator',path)
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class CSVStorageTests(unittest.TestCase):
    def test_quoted_comma(self):
        _,rows=v.parse_table('id,note\nA,"a,b"\n')
        self.assertEqual(rows[0]['note'],'a,b')
    def test_multiline(self):
        _,rows=v.parse_table('id,note\nA,"one\ntwo"\nB,three\n')
        self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['note'],'one\ntwo')
    def test_escaped_quote(self):
        _,rows=v.parse_table('id,note\nA,"a ""quote"""\n')
        self.assertEqual(rows[0]['note'],'a "quote"')
    def test_surplus_blank_rejected(self):
        with self.assertRaises(ValueError):v.parse_table('id,note\nA,,text\n')
    def test_short_row_rejected(self):
        with self.assertRaises(ValueError):v.parse_table('id,note\nA\n')
    def test_duplicate_header_rejected(self):
        with self.assertRaises(ValueError):v.parse_table('id,id\nA,B\n')
    def test_unclosed_quote_rejected(self):
        with self.assertRaises(csv.Error):v.parse_table('id,note\nA,"bad\n')
    def test_duplicate_identifier_rejected(self):
        with self.assertRaises(ValueError):v.unique([{'id':'A'},{'id':'A'}],'id','test')
    def test_blank_identifier_rejected(self):
        with self.assertRaises(ValueError):v.unique([{'id':''}],'id','test')
    def test_roundtrip(self):
        data=[{'id':'TSS-0047','note':'A, B\n"C"'}]
        s=io.StringIO(newline='');w=csv.DictWriter(s,['id','note'],lineterminator='\n');w.writeheader();w.writerows(data)
        self.assertEqual(v.parse_table(s.getvalue())[1],data)
    def test_multiple_references(self):
        self.assertEqual(v.references('SRC-001; SRC-198','SRC'),['SRC-001','SRC-198'])
    def test_source_parser_wrapper_rejected(self):
        with self.assertRaises(ValueError):v.parse_table('<PARSED SHEET>\nindex,id,note\n0,A,B\n')
    def test_complete_repository(self):
        self.assertEqual(v.validate()['structural_validation'],'PASS')

if __name__=='__main__':unittest.main()
