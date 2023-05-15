#!/usr/bin/env python3

import dns.resolver
import time
import os

# You can replace these with environment variables or command line arguments
hostname = "futurestay.com"
substring = "google-site"
d = 5

def monitor_dns(hostname, substring, d):
    while True:
        try:
            answers = dns.resolver.resolve(hostname, 'TXT')
            for rdata in answers:
                for txt_string in rdata.strings:
                    if substring in txt_string.decode():
                        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Found '{substring}' in TXT record of {hostname}")
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(d)

monitor_dns(hostname, substring, d)
