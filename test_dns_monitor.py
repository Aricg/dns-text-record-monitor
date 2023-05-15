#!/usr/bin/env python3

# test_dns_monitor.py
import unittest
from unittest.mock import patch, MagicMock
from dns_monitor import process_txt_records

class TestDNSMonitor(unittest.TestCase):

    @patch('dns_monitor.fetch_txt_records')
    def test_process_txt_records(self, mock_fetch_txt_records):
        # Simulate multiple Rdata objects
        mock_rdata1 = MagicMock()
        mock_rdata1.strings = [b'google-site-verification=abc123']
        mock_rdata2 = MagicMock()
        mock_rdata2.strings = [b'google-site-verification=def456']

        # Return a list of mock Rdata objects
        mock_fetch_txt_records.return_value = [mock_rdata1, mock_rdata2]

        new_keys, found_new_key = process_txt_records(mock_fetch_txt_records.return_value, 'google-site-verification')
        
        self.assertEqual(new_keys, {'abc123', 'def456'})
        self.assertTrue(found_new_key)

if __name__ == "__main__":
    unittest.main()

