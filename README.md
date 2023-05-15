# DNS Text Record Monitor

This script continuously monitors a domain name for the presence of specified DNS TXT records. The typical use case is for site verification, where you need to prove that you own or control a particular domain or website. This proof is often required to gain access to certain features or settings provided by web services or search engines. By adding a specific TXT record to your domain's DNS configuration, you demonstrate ownership or control of the domain to these services.

## Usage

### Viewing a Domain's Text Records

To see the current text records of a domain, use the following command:

```bash
dig +short TXT "$domain"
```

### Running the Code Locally

#### With Default Arguments

1. Clone this repository.
2. Create a virtual environment (optional but recommended).
3. Install the necessary dependencies:
```bash
pip install -r requirements.txt
```
markdown
Copy code
4. Run the script:
```bash
./dns_monitor.py
```

#### With Custom Arguments

1. Clone this repository.
2. Create a virtual environment (optional but recommended).
3. Install the necessary dependencies:
```bash
pip install -r requirements.txt
4. Run the script with custom arguments:
```

```bash
./dns_monitor.py --targethost=google.com --substring=docusign
```
### Running the Code via Docker

You can also run the script in a Docker container:

```bash
docker run -t -i ghcr.io/aricg/dns-text-record-monitor:latest
```
This will execute the script with the default arguments.

### Customizing Script Execution in Docker

You can customize the script execution by setting environment variables:

```bash
docker run -t -i
-e TARGETHOSTNAME=google.com
-e SUBSTRING=google-site-verification
-e DELAY=10
ghcr.io/aricg/dns-text-record-monitor:latest
```
In this example, the script will monitor the `google.com` domain for the presence of `google-site-verification` TXT records and will perform the check every 10 seconds.

## Example Output

```bash
2023-05-15 18:00:22 - Found new 'google-site-verification' key '5b2Ows2wRigUWdMsNX-LPNNo-wyRYULK6Gd2yvbTypQ' in TXT record
2023-05-15 18:00:22 - Found new 'google-site-verification' key 'SQ7PKFx3wTU6BmkOSX03TAidepYF1pZwfcf9F_FZSrg' in TXT record
2023-05-15 18:00:22 - Found new 'google-site-verification' key 'VGI_ot-3h14rDOnZIuMvMVYiR-YxO0VI4o1dMvzLyXM' in TXT record
2023-05-15 18:00:27 - No new keys found in this loop for futurestay.com
```

In this example, the script found new keys for `google-site-verification` in the TXT records of the domain `futurestay.com`. After a delay, it checked again and found no new keys.

