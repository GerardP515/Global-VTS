"""Regression checks for the dated B12 patch, without freezing future research."""
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class B12RecheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patch=json.loads((ROOT/'research/stage2/b12_recheck_20260930/master_patch.json').read_text())
        cls.updates={r['tss_id']:r for r in cls.patch['records']}

    def test_exactly_b12(self):
        self.assertEqual(set(self.updates),{f'TSS-{i:04d}' for i in range(56,61)})

    def test_reuse_one_service(self):
        for n in (58,59,60):
            u=self.updates[f'TSS-{n:04d}']['changes']
            self.assertEqual(u['vts_id'],'VTS-0044')
            self.assertEqual(u['association_status'],'VTS only')

    def test_no_unproved_ijmuiden_coverage(self):
        for n in (56,57):
            u=self.updates[f'TSS-{n:04d}']['changes']
            self.assertEqual(u['association_status'],'Unresolved')
            self.assertEqual(u['vts_id'],'')
            self.assertEqual(u['candidate_vts_ids'],'VTS-0025')

    def test_reporting_distinction(self):
        for entry in self.updates.values():
            self.assertEqual(entry['changes']['vrs_id'],'')
            self.assertIn('not a statement that no statutory reporting duty exists',entry['changes']['reporting_boundary_basis'])

    def test_guards_and_precision(self):
        for r in self.updates.values():self.assertEqual(len(r['expected_record_sha256']),64)
        self.assertIn('exact edge unresolved',self.updates['TSS-0060']['changes']['vts_coverage_type'])
        self.assertIn('confirmed partial',self.updates['TSS-0058']['changes']['vts_coverage_type'].lower())

if __name__=='__main__':unittest.main()
