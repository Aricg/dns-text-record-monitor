#!/usr/bin/env python3

import dns.resolver
import time
import os

# You can replace these with environment variables or command line arguments
hostname = "futurestay.com"
substring = "google-site-verification"
d = 5

# Store the keys
keys = set()

def monitor_dns(hostname, substring, d):
    global keys
    while True:
        try:
            new_keys = set()
            found_new_key = False
            answers = dns.resolver.resolve(hostname, 'TXT')
            for rdata in answers:
                for txt_string in rdata.strings:
                    txt_string = txt_string.decode()
                    if substring in txt_string:
                        key = txt_string.split('=')[-1]
                        new_keys.add(key)
                        if key not in keys:
                            found_new_key = True
                            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Found new '{substring}' key '{key}' in TXT record of {hostname}")
            keys = new_keys
            if not found_new_key:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - No new keys found in this loop for {hostname}")
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(d)

monitor_dns(hostname, substring, d)

