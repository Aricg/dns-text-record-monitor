#!/usr/bin/env python3

import dns.resolver
import time
import os
import argparse

# Command-line arguments
parser = argparse.ArgumentParser(description='Monitor DNS TXT records.')
parser.add_argument('--hostname', type=str, default=os.getenv('HOSTNAME', 'futurestay.com'))
parser.add_argument('--substring', type=str, default=os.getenv('SUBSTRING', 'google-site-verification'))
parser.add_argument('--d', type=int, default=os.getenv('DELAY', 5))
args = parser.parse_args()

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
                        key = txt_string.split('=')[-1] if '=' in txt_string else None
                        if key:
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

monitor_dns(args.hostname, args.substring, args.d)
