
# JohnDoe 
This simple program creates near-realistic fake data for a fictional British subject. 

This data could be used to populate test environments with arbitrary user information.

## data:
+ **Name**
    + Forename
        + Random from a list of popular names in 2021
    + Surname
        + Random from a list of the most frequent UK surnames
+ **Age**
    + Random integer from 18 - 65
    + Birthday
        + current year - age = year born
        + 1 ~ current month = month born
+ **Phone Number**
    + Genuine UK prefixes and providers
    + Random suffixes
+ **Address**
    + House number 
        + Random integer from 1 - 500
    + Street names
        + Random from a list of the most frequent UK street names
    + Postcode and area 
        + Random but genuine - Meaning the specific postcode is in the listed area
+ **National Insurance Number**
    + UK format of _AB123456C_
+ **Bank Card Details**
    + Bank card numbers
        + Genuine first 6-digit account IDs and then 10 random numbers
    + Bank expiry dates and CVVs
        + Randomly generated integers
+ **Driving License**
    + UK formatted number with John Doe's information
+ **Email**
    + forename.surname@ random email provider with UK TLD
+ **IP Address**
    + Uses genuine UK IP blocks to create a random IP address within that range.

## Setup
1. Clone the repo into the desired location
```bash
$ git clone https://github.com/IanUmney/JohnDoe
```
2. Change into that directory
```bash
$ cd JohnDoe/
```
3. Import the _JohnDoe.py_ file into an existing program and call the JohnDoe().create() function
```python
from JohnDoe import JohnDoe

jd = JohnDoe().create()
```
This will return a dictionary with all the data for the fictional person. 
```python
{
    'mobile_number': '07945301576', 
    'ni_number': 'OB955001O', 
    'address': {
                'house_number': 401, 
                'street': 'Manchester Road', 
                'area': 'Richmond upon Thames', 
                'postcode': 'TW11 8YZ'
                }, 
    'name': 'Zachary Ramsey', 
    'bank_card': {
                'card_number': '5573573699040899', 
                'provider': 'Mastercard', 
                'expiry_date': '8/31', 
                'cvv': '803'
                }, 
    'age': '21', 
    'birthday': '27/06/2000', 
    'driving_license': 'Ramse00627099IP 60', 
    'email': 'Zachary.Ramsey@hotmail.co.uk'
}

```

You can pass `**kwargs` to the JohnDoe class to specify particular variables.
```python
jd = JohnDoe(name="Mike Smith", age=37).create()
print(jd)
```

```python
{
    'mobile_number': '07945301576', 
    'ni_number': 'OB955001O', 
    'address': {
                'house_number': 401, 
                'street': 'Manchester Road', 
                'area': 'Richmond upon Thames', 
                'postcode': 'TW11 8YZ'
                }, 
    'name': 'Mike Smith', 
    'bank_card': {
                'card_number': '5573573699040899', 
                'provider': 'Mastercard', 
                'expiry_date': '8/31', 
                'cvv': '803'
                }, 
    'age': 37, 
    'birthday': '27/06/2000', 
    'driving_license': 'Ramse00627099IP 60', 
    'email': 'Zachary.Ramsey@hotmail.co.uk'
}

```