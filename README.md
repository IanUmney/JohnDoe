<p align="left">
    <a href="https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tar.xz" alt="3.9.5">
        <img src="https://img.shields.io/badge/Python%20Version-3.9.5-blue"/></a>
    <a href="https://ubuntu.com/download/desktop/thank-you?version=20.04.2.0&architecture=amd64" alt="Ubuntu">
        <img src="https://img.shields.io/badge/Tested%20on-Ubunu%2020.04-orange"/></a>
    </p>

# JohnDoe 
This simple program creates near-realistic fake data for a fictional subject. 

This data could be used to populate test environments with arbitrary user information.

## Setup
1. Clone the repo into the desired location
```bash
$ git clone https://github.com/IanUmney/JohnDoe
```
2. Change into that directory
```bash
$ cd JohnDoe/
```

## Usage
Call the _JohnDoe.py_ file directly. This will print a dictionary-style output of the information.
```bash
python3 JohnDoe.py
```

### Importing the module
Import the _JohnDoe.py_ file into an existing program and call the .create() function.
```python
from JohnDoe import JohnDoe

jd = JohnDoe()
jd.create()
```

You can pass `**kwargs` to the JohnDoe object to specify particular variables.

```python
jd = JohnDoe(name="Mike Smith", age=22).create()
```
**Output from above command**
```
name : Mike Smith
age : 22
birthday : 21/05/1999
mobile_number
    number : 07735167188
    provider : Three
address
    house_number : 257
    street : Park Road
    area : Pembrokeshire
    postcode : SA61 1YG
email : Mike.Smith@hotmail.co.uk
ip_address : 213.253.175.72
ni_number : FC812154X
bank_card
    card_number : 5573576189231788
    provider : Mastercard
    expiry_date : 5/31
    cvv : 255
driving_license : smith90521999BJ 20
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Mike Smith_portrait.jpg
```

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
+ **Image**
    + Using https://generated.photos/ API, returns an AI image based on the details of John Doe.
    + Saves images into src/images with the file name of the John Doe you created. 
        + `/John Doe_portrait.jpg`
    + You must obtain an API key from https://generated.photos/ for this to work.
        + Free sign up and 50 free monthly requests.
## Including AI Generated Images
Enter your API key into the config.ini file to enable generation of faces.
```
[GeneratedPhotos]
API_KEY : Enter_Your_API_Here
```

## List of Keyword Arguments:
You can pass none or all of the keyword arguments for the `JohnDoe()` object.
```python
JohnDoe(name="Ian Thomas Umney", age=27, nationality="gb", gender="male") 
"""
name ---------- -> ---- String. Should include forename and surname at a minimum
age ----------- -> ---- Integer > 0
nationality --- -> ---- String. gb = Great Britain. de = Germany. Etc.
gender -------- -> ---- String. "male" / "m" or "female" / "f"
"""
```

### Example Results

**Mike Smith**
```
name : Mike Smith
age : 22
birthday : 21/05/1999
mobile_number
    number : 07735167188
    provider : Three
address
    house_number : 257
    street : Park Road
    area : Pembrokeshire
    postcode : SA61 1YG
email : Mike.Smith@hotmail.co.uk
ip_address : 213.253.175.72
ni_number : FC812154X
bank_card
    card_number : 5573576189231788
    provider : Mastercard
    expiry_date : 5/31
    cvv : 255
driving_license : smith90521999BJ 20
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Mike Smith_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Mike%20Smith_portrait.jpg?raw=true)


**Jack Peterson**
```
nationality : GB
name : Jack Peterson
age : 44
birthday : 17/06/1977
mobile_number
    number : 07537625268
    provider : Sound Advertising
address
    house_number : 265
    street : South Street
    area : Basingstoke and Deane
    postcode : RG21 3LQ
email : Jack.Peterson@gmail.co.uk
ip_address : 45.75.140.218
ni_number : UA718154E
bank_card
    card_number : 5573579597246203
    provider : Mastercard
    expiry_date : 5/23
    cvv : 391
driving_license : peter70617799AC 80
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Jack Peterson_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Jack%20Peterson_portrait.jpg?raw=true)


**Mohommed Martin**
```
nationality : GB
name : Mohammed Martin
age : 54
birthday : 23/02/1967
mobile_number
    number : 07600018185
    provider : Sound Advertising
address
    house_number : 33
    street : Park Road
    area : Wirral
    postcode : CH60 8QJ
email : Mohammed.Martin@msn.co.uk
ip_address : 194.183.102.107
ni_number : UF390955W
bank_card
    card_number : 5573579653322277
    provider : Mastercard
    expiry_date : 10/28
    cvv : 631
driving_license : marti60223799VK 80
image : /home/ian/Development/Python/Github/JohnDoe/src/images/Mohammed Martin_portrait.jpg
```
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Mohammed%20Martin_portrait.jpg?raw=true)