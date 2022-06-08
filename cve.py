import json
import requests

#URL to generate The top 30 vulnerabilites for gain information, code execution, gain privilege, or bypass somthing from cvedetails.com for CVSS's >=7
url = requests.get("http://www.cvedetails.com/json-feed.php?numrows=30&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=1&opov=0&opcsrf=0&opfileinc=0&opgpriv=1&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=1&opginf=1&opdos=0&orderby=3&cvssscoremin=7").json() 

for cve in url:
    print(json.dumps(cve, indent=4))
    print()



