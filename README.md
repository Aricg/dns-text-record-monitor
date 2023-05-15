# dns-text-record-monitor
monitor a domain name for the presence of site verification DNS TXT record

Site verification is the process of proving that you own or control a particular domain or website. It is often required to gain access to certain features or settings provided by web services or search engines. By adding a specific TXT record to your domain's DNS configuration, you demonstrate ownership or control of the domain to these services.

See a domains text records
```bash
dig +short TXT "$domain"
```

run the code locally with default
```bash
#clone repo
#create venv
pip install -r requirements.txt
./dns_monitor.py
```

run the code locally with custom arguments
```bash
#clone repo
#create venv
pip install -r requirements.txt
./dns_monitor.py --targethost=google.com --substring=docusign

```


run the code via docker
```bash

docker run -t -i ghcr.io/aricg/dns-text-record-monitor:latest

#Example output
2023-05-15 18:00:22 - Found new 'google-site-verification' key '5b2Ows2wRigUWdMsNX-LPNNo-wyRYULK6Gd2yvbTypQ' in TXT record
2023-05-15 18:00:22 - Found new 'google-site-verification' key 'SQ7PKFx3wTU6BmkOSX03TAidepYF1pZwfcf9F_FZSrg' in TXT record
2023-05-15 18:00:22 - Found new 'google-site-verification' key 'VGI_ot-3h14rDOnZIuMvMVYiR-YxO0VI4o1dMvzLyXM' in TXT record
2023-05-15 18:00:27 - No new keys found in this loop for futurestay.com
```

run the code with custom variables (google.com, delay 10 seconds)
```bash

docker run -t -i \
-e TARGETHOSTNAME=google.com \
-e SUBSTRING=google-site-verification \
-e DELAY=10 \
ghcr.io/aricg/dns-text-record-monitor:latest
```
