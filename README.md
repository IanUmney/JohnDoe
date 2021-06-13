
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
+ **Phone Number**
    + UK format of "07" & 9 random numbers
+ **Address**
    + House number 
        + Random integer from 1 - 500
    + Street names
        + Random from a list of the most frequent UK street names
    + Postcode and area 
        + Random but genuine - Meaning the specific postcode is in the listed area
+ **National Insurance Number**
    + UK format of _AB12345678C_
+ **Bank card details**
    + Bank card numbers
        + Genuine first 6-digit account IDs and then 10 random numbers
    + Bank expiry dates and CVVs
        + Randomly generated integers

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
    'name': 'Frederick Elliot', 
    'address': '15 Church Lane, Stroud, GL13 9NG', 
    'phone_number': '07431876264', 
    'ni_number': 'OI761649A', 
    'bank_card': '5573577943354436 - Mastercard Expiry:12/26 CVV:601', 
    'age': '29'
}
```

You can pass `**kwargs` to the JohnDoe class to specify particular variables.
```python
jd = JohnDoe(name="Mike Smith", age=37).create()
print(jd)
```

```bash
{
    'name': 'Mike Smith', 
    'address': '117 The Green, Scarborough, YO21 1EY', 
    'phone_number': '07912271019', 
    'ni_number': 'HB442445E', 
    'bank_card': '5573578333733555 - Mastercard Expiry:5/25 CVV:779', 
    'age': 37
}
```