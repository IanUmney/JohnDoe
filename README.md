
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
+ **Image**
    + Using https://generated.photos/ API, returns an AI image based on the details of John Doe.
    + Saves images into src/images with the file name of the John Doe you created. 
        + `/John Doe_portrait.jpg`
    + You must obtain an API key from https://generated.photos/ for this to work.
        + Free sign up and 50 free monthly requests.
    + **Enter the API key in the config.ini folder like this:**
```
[GeneratedPhotos]
API_KEY : Enter_Your_API_Here
```

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
```
name : Benjamin Pastor
age : 55
birthday : 09/02/1966
mobile_number : 
    number : 07660654789
    provider : 24 Seven Communications
address : 
    house_number : 409
    street : Church Street
    area : Wokingham
    postcode : RG5 3NP
email : Benjamin.Pastor@yahoo.co.uk
ip_address : 130.32.142.49
ni_number : AB812065R
bank_card : 
    card_number : 5573574826858015
    provider : Mastercard
    expiry_date : 5/25
    cvv : 309
driving_license : pasto60209699IN 30
```

You can pass `**kwargs` to the JohnDoe class to specify particular variables.
```python
jd = JohnDoe(name="Mike Smith", age=37).create()
```

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
### Example AI generated image
![Example AI generated image](https://github.com/IanUmney/JohnDoe/blob/main/src/images/Mike%20Smith_portrait.jpg?raw=true)

