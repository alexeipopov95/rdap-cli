![](https://badgen.net/badge/icon/github?icon=github&label) ![](https://img.shields.io/badge/Python%20Version-3.8.5-blue) ![](https://img.shields.io/badge/release%20-1.0.0-black)

![](https://www.selectallfromdual.com/blog/wp-content/uploads/2019/11/rdap.jpg)

## About

RDAP - Registration Data Access Protocol is an Internet protocol standardized in 2015 and thought of as an evolution of WHOIS. This has a defined structure so that the data can be manipulated more easily at the programming level. The data type will be a Json.

This program is in charge of collecting all the relevant information related to a domain such as domain expiration date, nameservers, registration entity, domain registration date, if it is available to register or not.


## Utils
*Json TLD file:  [Json File](https://data.iana.org/rdap/dns.json)* \
*Rdap deployment:  [DATA](https://deployment.rdap.org/)* \
*Context format: [format](docs/outputs.md)*

## Requirements
Already exist a file called requirements.txt but for practical uses we are going to mention here too.


|PACKAGES|VERSION|COMMAND|DOCS|PyPI|
| ------------ | ------------ | ------------ | ------------ |------------ |
|Click|8.0.0|pip install click|[DOCS](https://click.palletsprojects.com/en/8.0.x/)|[PyPI](https://pypi.org/project/click/)|
|Python dateutil|2.8.1|pip install python-dateutil|[DOCS](https://dateutil.readthedocs.io/en/stable/)|[PyPI](https://pypi.org/project/python-dateutil/)|
|Requests|2.22.0|pip install requests|[DOCS](https://docs.python-requests.org/en/master/)|[PyPI](https://pypi.org/project/requests/)|
|Tldextract|3.1.0|pip install tldextract|[DOCS](https://github.com/john-kurkowski/tldextract)|[PyPI](https://pypi.org/project/tldextract/)|
|Validators|0.18.2|pip install validators|[DOCS](https://github.com/kvesteri/validators)|[PyPI](https://pypi.org/project/validators/)|
|PyYAML|5.4.1|pip install PyYAML|[DOCS](https://pyyaml.org/wiki/PyYAMLDocumentation)|[PyPI](https://pypi.org/project/PyYAML/)|
|Tabulate|0.8.9|pip install tabulate|[DOCS](https://github.com/astanin/python-tabulate)|[PyPI](https://pypi.org/project/tabulate/)|


## Features
- This tool gives you the ability to look up the registration data for domain names.
- It allows the detection of unregistered domains.
- Provide useful information whether for personal or work use.
- Replaces traditional whois.
- Allow you to save the payload into multiple format files such as '.json' or '.txt'.
- Allow you to check multiple domains at the same time using a specific file format.

## Guide
You can check the tutorial [HERE](docs/user_guide.md)
