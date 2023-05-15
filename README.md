# dns-text-record-monitor
monitor a domain name for the presence of site verification DNS TXT record

Site verification is the process of proving that you own or control a particular domain or website. It is often required to gain access to certain features or settings provided by web services or search engines. By adding a specific TXT record to your domain's DNS configuration, you demonstrate ownership or control of the domain to these services.

See a domains text records
```bash
dig +short TXT "$domain"
```


