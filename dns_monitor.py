#!/usr/bin/env python3

# dns_monitor.py
import dns.resolver
import time
import os
import argparse


# Store the keys
keys = set()

def fetch_txt_records(targethost):
    return dns.resolver.resolve(targethost, 'TXT')

def process_txt_records(records, substring):
    new_keys = set()
    found_new_key = False
    for rdata in records:
        for txt_string in rdata.strings:
            txt_string = txt_string.decode()
            if substring in txt_string:
                key = txt_string.split('=')[-1] if '=' in txt_string else None
                if key:
                    new_keys.add(key)
                    if key not in keys:
                        found_new_key = True
                        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Found new '{substring}' key '{key}' in TXT record")
    return new_keys, found_new_key

def monitor_dns(targethost, substring, d):
    global keys
    while True:
        try:
            records = fetch_txt_records(targethost)
            new_keys, found_new_key = process_txt_records(records, substring)
            keys = new_keys
            if not found_new_key:
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - No new keys found in this loop for {targethost}")
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(d)

if __name__ == "__main__":
    # Command-line arguments
    parser = argparse.ArgumentParser(description='Monitor DNS TXT records.')
    parser.add_argument('--targethost', type=str, default=os.getenv('TARGETHOSTNAME', 'futurestay.com'))
    parser.add_argument('--substring', type=str, default=os.getenv('SUBSTRING', 'google-site-verification'))
    parser.add_argument('--d', type=int, default=os.getenv('DELAY', 5))
    args = parser.parse_args()
    monitor_dns(args.targethost, args.substring, args.d)

