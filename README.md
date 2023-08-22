

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
$ pip install -r requirements.txt
```

### Usage
Import into python project
```python
from johndoe import JohnDoe

# Create a JohnDoe instance
jd = JohnDoe()

# print JSON to terminal
print(jd.json())
```
or from the command line
```bash
$ python3 -m johndoe 
```

### Example output:
```json
{
    "gender": "f",
    "name": "Lilly-ann Painter",
    "age": 69,
    "documents": false,
    "nino": "LM 39 92 35 C",
    "email": "Lilly-ann.Painter@hotmail.com",
    "address": {
        "house_number": 291,
        "street": "Broadway",
        "area": "Hammersmith and Fulham",
        "postcode": "NW10 5AZ"
    },
    "birthday": "20/04/1954",
    "banking": {
        "bank": "LLOYDS BANK PLC",
        "sort_code": "43-68-65",
        "account_number": 26228720,
        "card_number": "5573 5757 2200 9728",
        "provider": "Mastercard",
        "expiry_date": "11/31",
        "cvv": "437"
    },
    "ip_address": "146.80.23.90",
    "mobile_number": {
        "number": "07802451005",
        "provider": "O2"
    },
    "driving_license": "PAINT5920499RT 40"
}
```


## Upcoming Features
- Document creation
  - Generate bank card and national identity card images
- AI image creation (re-integration)
- More PII
  - Work history
  - Online accounts / passwords
  - Education
  - and more