

# JohnDoe Documentation

The `JohnDoe` class generates synthetic personal information (PII) for testing environments. It creates mock details of a person, including name, age, address, phone number, email, and more.

## Class Overview

This class allows you to generate random personal information and related documents.


### Setup
1. Clone the repo into the desired location
```bash
$ git clone https://github.com/IanUmney/JohnDoe.git
```
2. Change into that directory
```bash
$ cd JohnDoe/
```
3. Install via pip
```bash
$ pip install .
```

### Usage
Import into python project
```python
from johndoe import JohnDoe

# Create a JohnDoe instance
jd = JohnDoe()

jd.create()
```
or from the command line
```bash
$ python3 -m johndoe --document
```

### Example output:
```json
{
    "gender": "m",
    "name": "Lucas Richards",
    "age": 35,
    "nino": "BD 59 71 22 Y",
    "email": "Lucas.Richards@yahoo.com",
    "address": {
        "house_number": 128,
        "street": "South Street",
        "area": "North Ayrshire",
        "postcode": "KA27 8BE"
    },
    "birthday": "18/01/1988",
    "banking": {
        "bank": "LLOYDS BANK PLC",
        "sort_code": "11-06-35",
        "account_number": 69450610,
        "card_number": "5573 5742 3918 7035",
        "provider": "Mastercard",
        "expiry_date": "12/22",
        "cvv": "260"
    },
    "ip_address": "188.125.93.31",
    "mobile_number": {
        "number": "07392985340",
        "provider": "Vodafone"
    },
    "driving_license": "RICHA8618899NJ 60"
}
```
#### National Identity Card
![generated_national_identity_card.jpg](src/national_identity_card/generated_national_identity_card.jpg)
#### National Insurance Number Card
![generated_national_insurance_card.jpg](src/national_insurance/nino_card.jpg)

